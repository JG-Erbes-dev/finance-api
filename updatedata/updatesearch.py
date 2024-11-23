import os
import pandas as pd
import requests
import logging
import yfinance as yf
from datetime import datetime
from django.db import transaction
from search.models import BrStock, UsStock, BrRealEstate, UsEtf, Crypto, BrTreasure
from bs4 import BeautifulSoup
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('X-CMC_PRO_API_KEY')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

MODELS_TO_UPDATE = [
    {'model': UsStock},
    {'model': UsEtf},
]

def save_csv_data_to_db(csv_file_path, model):
    try:
        data = pd.read_csv(csv_file_path, sep=';')

        if not data.empty:
            with transaction.atomic():
                records_to_update = []
                records_to_create = []

                for _, row in data.iterrows():
                    ticker = row['ticker'].strip()
                    name = row['name'].strip()

                    instance = model.objects.filter(ticker=ticker).first()
                    if instance:
                        if instance.name != name:
                            instance.name = name
                            records_to_update.append(instance)
                    else:
                        records_to_create.append(model(ticker=ticker, name=name))

                if records_to_create:
                    model.objects.bulk_create(records_to_create)
                    logging.info(f'{len(records_to_create)} registros criados com sucesso.')
                if records_to_update:
                    model.objects.bulk_update(records_to_update, ['name'])
                    logging.info(f'{len(records_to_update)} registros atualizados com sucesso.')
        else:
            logging.warning('O arquivo CSV está vazio.')
    except Exception as e:
        logging.error(f'Ocorreu um erro ao ler o arquivo CSV: {e}')

def fetch_crypto_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {'start': '1', 'limit': '100', 'convert': 'USD'}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_key}

    try:
        response = requests.get(url, headers=headers, params=parameters)
        response.raise_for_status()

        data = response.json()

        if 'data' in data and data['data']:
            with transaction.atomic():
                records_to_update = []
                records_to_create = []

                for crypto in data['data']:
                    ticker = crypto['symbol']
                    name = crypto['name']

                    instance = Crypto.objects.filter(ticker=ticker).first()
                    if instance:
                        if instance.name != name:
                            instance.name = name
                            records_to_update.append(instance)
                    else:
                        records_to_create.append(Crypto(ticker=ticker, name=name))

                if records_to_create:
                    Crypto.objects.bulk_create(records_to_create)
                    logging.info(f'{len(records_to_create)} criptomoedas criadas com sucesso.')
                if records_to_update:
                    Crypto.objects.bulk_update(records_to_update, ['name'])
                    logging.info(f'{len(records_to_update)} criptomoedas atualizadas com sucesso.')
        else:
            logging.warning('Nenhuma criptomoeda encontrada na resposta da API.')
    except requests.HTTPError as http_err:
        logging.error(f'Erro HTTP ao acessar a API: {http_err}')
    except Exception as e:
        logging.error(f'Ocorreu um erro ao coletar dados de criptomoedas: {e}')

def save_treasure_csv_data_to_db(csv_file_path):
    try:
        data = pd.read_csv(csv_file_path, sep=';')

        if not data.empty:
            with transaction.atomic():
                records_to_create = []

                for _, row in data.iterrows():
                    title_type = row['Tipo Titulo'].strip()
                    maturity = datetime.strptime(row['Data Vencimento'], "%d/%m/%Y").date()
                    title = f"{title_type} {maturity.year}"

                    if not BrTreasure.objects.filter(title=title, maturity=maturity).exists():
                        records_to_create.append(
                            BrTreasure(title_type=title_type, title=title, maturity=maturity)
                        )

                if records_to_create:
                    BrTreasure.objects.bulk_create(records_to_create)
                    logging.info(f'{len(records_to_create)} registros de Tesouro Direto criados com sucesso.')
        else:
            logging.warning('O arquivo CSV do Tesouro Direto está vazio.')
    except Exception as e:
        logging.error(f"Ocorreu um erro ao ler o arquivo CSV: {e}")

def update_sector_and_industry():
    for model_info in MODELS_TO_UPDATE:
        model = model_info['model']

        instances = model.objects.all()

        with transaction.atomic():
            records_to_update = []

            for instance in instances:
                ticker_symbol = instance.ticker
                try:
                    ticker_info = yf.Ticker(ticker_symbol).info
                    new_sector = ticker_info.get('sector', '')
                    new_industry = ticker_info.get('industry', '')

                    if instance.sector != new_sector or instance.industry != new_industry:
                        instance.sector = new_sector
                        instance.industry = new_industry
                        records_to_update.append(instance)
                except Exception as e:
                    logging.error(f'Erro ao coletar dados para {ticker_symbol}: {e}')

            if records_to_update:
                model.objects.bulk_update(records_to_update, ['sector', 'industry'])
                logging.info(f'{len(records_to_update)} registros de {model.__name__} atualizados.')

def update_category():
    instances = UsEtf.objects.all()

    with transaction.atomic():
        records_to_update = []

        for instance in instances:
            ticker_symbol = instance.ticker
            try:
                ticker_info = yf.Ticker(ticker_symbol).info
                new_category = ticker_info.get('category', '')

                if instance.category != new_category:
                    instance.category = new_category
                    records_to_update.append(instance)
            except Exception as e:
                logging.error(f'Erro ao coletar dados para {ticker_symbol}: {e}')

        if records_to_update:
            UsEtf.objects.bulk_update(records_to_update, ['category'])
            logging.info(f'{len(records_to_update)} registros de UsEtf atualizados.')

def download_and_save_csv(csv_url, local_file_path, original_file_name):
    """
    Baixa o arquivo CSV do Tesouro Direto e o salva localmente.

    Args:
        csv_url (str): A URL do arquivo CSV.
        local_file_path (str): O caminho local onde o CSV será salvo como BrTreasure.csv.
        original_file_name (str): O nome original do arquivo que será baixado.
    """
    try:
        response = requests.get(csv_url)
        response.raise_for_status()

        if os.path.exists(local_file_path):
            os.remove(local_file_path)
            logging.info(f'Arquivo existente removido: {local_file_path}')

        temp_file_path = os.path.join(os.path.dirname(
            local_file_path), original_file_name)

        with open(temp_file_path, 'wb') as f:
            f.write(response.content)

        logging.info("Arquivo CSV do Tesouro Direto baixado com sucesso.")

        os.rename(temp_file_path, local_file_path)
        logging.info(f'Arquivo renomeado para: {local_file_path}')

    except Exception as e:
        logging.error(f"Erro ao baixar o arquivo CSV: {e}")

csv_url = 'https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv'
local_file_path = 'BrTreasure.csv'
original_file_name = 'PrecoTaxaTesouroDireto.csv'

def execute_all():
    """
    Executa as funções para coletar dados e salvar no banco de dados.
    """
    fetch_crypto_data()
    download_and_save_csv(csv_url, local_file_path, original_file_name)
    save_treasure_csv_data_to_db('BrTreasure.csv')
    save_csv_data_to_db('BrStocks.csv', BrStock)
    save_csv_data_to_db('UsStocks.csv', UsStock)
    save_csv_data_to_db('BrRealEstate.csv', BrRealEstate)
    save_csv_data_to_db('UsEtf.csv', UsEtf)
    update_sector_and_industry()
    update_category()
