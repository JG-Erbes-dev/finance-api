import os
import yfinance as yf
import requests
from dotenv import load_dotenv
from datetime import datetime
from bcb import sgs
from econdata.models import BrInterestRate, UsInterestRate, BrCDI, CumulativeBrCDI, BrInflation, CumulativeBrInflation, UsInflation, DollarExchangeRate, CommodityPrice
from django.db import transaction


load_dotenv()
api_key = os.getenv('FRED_API_KEY')

def bulk_save_to_db(model, data):
    """
    Salva ou atualiza registros no banco de dados em bulk.
    """
    create_objects = []
    update_objects = []
    log_messages = []

    existing_records = model.objects.filter(date__in=[item['date'] for item in data])
    existing_records_dict = {record.date: record for record in existing_records}

    for item in data:
        date = item['date']
        value = item['value']
        obj = existing_records_dict.get(date)

        if obj:
            if obj.value != value:
                obj.value = value
                update_objects.append(obj)
                log_messages.append(f"Atualizado: Data: {date}, Novo Valor: {value}")
            else:
                log_messages.append(f"Valor já atualizado: Data: {date}, Valor: {value}")
        else:
            create_objects.append(model(date=date, value=value))
            log_messages.append(f"Salvando novo registro: Data: {date}, Valor: {value}")

    with transaction.atomic():
        if create_objects:
            model.objects.bulk_create(create_objects)
        if update_objects:
            model.objects.bulk_update(update_objects, ['value'])

    for message in log_messages:
        print(message)

def get_br_interest_rate():
    """
    Coleta a taxa Selic e salva no banco de dados.
    """
    selic_data = sgs.get(11, start='1995-01-01')
    data = [{'date': index.strftime('%Y-%m-%d'), 'value': row[0]} for index, row in selic_data.iterrows()]
    bulk_save_to_db(BrInterestRate, data)

def get_us_interest_rate():
    """
    Coleta a taxa de juros dos EUA e salva no banco de dados.
    """
    series_id = 'FEDFUNDS'
    start_date = '1995-01-01'
    url = f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&start_date={start_date}&end_date=latest&file_type=json'

    response = requests.get(url)
    if response.status_code == 200:
        interest_data = response.json()
        data = [{'date': obs['date'], 'value': float(obs['value'])} for obs in interest_data['observations']]
        bulk_save_to_db(UsInterestRate, data)
    else:
        print(f"Erro ao coletar dados: {response.status_code}")

def get_br_cdi():
    """
    Coleta a taxa CDI e salva no banco de dados.
    """
    cdi_data = sgs.get(12, start='1995-01-01')
    data = [{'date': index.strftime('%Y-%m-%d'), 'value': row[0]} for index, row in cdi_data.iterrows()]
    bulk_save_to_db(BrCDI, data)

def get_sum_cum_br_cdi():
    """
    Coleta o CDI acumulado e salva no banco de dados.
    """
    cdi_data = sgs.get(4391, start='1995-01-01')
    data = [{'date': index.strftime('%Y-%m-%d'), 'value': row[0]} for index, row in cdi_data.iterrows()]
    bulk_save_to_db(CumulativeBrCDI, data)

def get_inflation_br():
    """
    Coleta a inflação do Brasil e salva no banco de dados.
    """
    inflation_data = sgs.get(433, start='1995-01-01')
    data = [{'date': index.strftime('%Y-%m-%d'), 'value': row[0]} for index, row in inflation_data.iterrows()]
    bulk_save_to_db(BrInflation, data)

def get_cum_inflation_br():
    """
    Coleta a inflação acumulada do Brasil e salva no banco de dados.
    """
    inflation_data = sgs.get(13522, start='1995-01-01')
    data = [{'date': index.strftime('%Y-%m-%d'), 'value': row[0]} for index, row in inflation_data.iterrows()]
    bulk_save_to_db(CumulativeBrInflation, data)

def get_us_inflation():
    """
    Coleta a inflação dos EUA e salva no banco de dados.
    """
    series_id = 'CPIAUCSL'
    start_date = '1995-01-01'
    url = f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&start_date={start_date}&end_date=latest&file_type=json'

    response = requests.get(url)
    if response.status_code == 200:
        inflation_data = response.json()
        data = [{'date': obs['date'], 'value': float(obs['value'])} for obs in inflation_data['observations']]
        bulk_save_to_db(UsInflation, data)
    else:
        print(f"Erro ao coletar dados: {response.status_code}")

def get_exchange_rate():
    """
    Coleta a taxa de câmbio (USD/BRL) e salva no banco de dados.
    """
    exchange_data = sgs.get(1, start='1995-01-01')
    data = [{'date': index.strftime('%Y-%m-%d'), 'value': row[0]} for index, row in exchange_data.iterrows()]
    bulk_save_to_db(DollarExchangeRate, data)

def get_commodities_index():
    """
    Coleta o índice de commodities e salva no banco de dados.
    """
    start_date = '1995-01-01'
    gsci_index = yf.download("GD=F", start=start_date, end=datetime.now().strftime('%Y-%m-%d'))
    data = [{'date': index.strftime('%Y-%m-%d'), 'value': round(row['Close'])} for index, row in gsci_index.iterrows()]
    bulk_save_to_db(CommodityPrice, data)

def execute_all():
    """
    Executa as funções para coletar dados e salvar no banco de dados.
    """
    get_br_interest_rate()
    get_us_interest_rate()
    get_br_cdi()
    get_sum_cum_br_cdi()
    get_inflation_br()
    get_cum_inflation_br()
    get_us_inflation()
    get_exchange_rate()
    get_commodities_index()
