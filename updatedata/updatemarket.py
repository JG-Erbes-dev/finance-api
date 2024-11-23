import os
import pandas as pd
import yfinance as yf
from django.apps import apps
from django.db.models import Min
from dotenv import load_dotenv
from tvDatafeed import TvDatafeed, Interval
from marketdata.models import BrStock, UsStock, BrRealEstate, UsEtf, Crypto, BrTreasure, Stats
from search.models import BrStock as BrStock_S, UsStock as UsStock_S, BrRealEstate as BrRealEstate_S, UsEtf as UsEtf_S, Crypto as Crypto_S, BrTreasure as BrTreasure_S


load_dotenv()

username = os.getenv('username')
password = os.getenv('password')
print(f'Username: {username}, Password: {password}')

MODELS_TO_SEARCH = [
    {'model': BrStock_S, 'is_brazilian': True, 'save_model': BrStock},
    {'model': UsStock_S, 'is_brazilian': False, 'save_model': UsStock},
    {'model': UsEtf_S, 'is_brazilian': False, 'save_model': UsEtf},
]

def log_message(message):
    """Função para logar mensagens."""
    print(message)

def get_marketdata():
    """
    Função para atualizar os dados de Ações (Br e Us) e US ETFs.
    Se o banco estiver vazio, adicionará todos os dados. Se o banco tiver com dados, irá comparar e
    atualizar registros que estão diferentes e adicionar novos registros conforme avanço de datas.
    """
    for model_hist in MODELS_TO_SEARCH:
        search_model = model_hist['model']
        is_brazilian = model_hist['is_brazilian']
        save_model = model_hist['save_model']

        instances = search_model.objects.all()

        if instances.exists():
            for instance in instances:
                ticker_symbol = instance.ticker + '.SA' if is_brazilian else instance.ticker
                try:
                    historico = yf.Ticker(ticker_symbol).history(period='max', interval='1d', timeout=20)
                    historico = historico.reset_index()
                    historico['Date'] = historico['Date'].dt.date

                    existing_entries = save_model.objects.filter(ticker_id=instance.id).values('date', 'price', 'volume', 'id')
                    existing_data = {(entry['date']): (entry['id'], entry['price'], entry['volume']) for entry in existing_entries}

                    bulk_create = []
                    bulk_update = []

                    for _, row in historico.iterrows():
                        date = row['Date']
                        new_price = round(row['Close'], 2)
                        new_volume = row['Volume']

                        if date in existing_data:
                            existing_id, current_price, current_volume = existing_data[date]
                            if current_price != new_price or current_volume != new_volume:
                                model_entry = save_model(
                                    id=existing_id,
                                    date=date,
                                    ticker_id=instance.id,
                                    price=new_price,
                                    volume=new_volume
                                )
                                bulk_update.append(model_entry)
                                log_message(f'Atualizado: {ticker_symbol} - Data: {date}, Preço: {new_price}, Volume: {new_volume}')
                        else:
                            model_entry = save_model(
                                date=date,
                                ticker_id=instance.id,
                                price=new_price,
                                volume=new_volume
                            )
                            bulk_create.append(model_entry)
                            log_message(f'Criado: {ticker_symbol} - Data: {date}, Preço: {new_price}, Volume: {new_volume}')

                    if bulk_create:
                        save_model.objects.bulk_create(bulk_create)
                    if bulk_update:
                        save_model.objects.bulk_update(bulk_update, ['price', 'volume'])

                    if not bulk_create and not bulk_update:
                        log_message(f'Nada a fazer para {ticker_symbol}.')
                        continue

                except Exception as e:
                    log_message(f'Erro ao coletar dados para {ticker_symbol}: {e}')
                    input('Pressione Enter para continuar para o próximo ativo...')

def get_br_real_estate_data():
    """
    Função para atualizar os dados de FIIs pelo Tradingview.
    Se o banco estiver vazio, adicionará todos os dados. Se o banco tiver com dados, irá comparar e
    atualizar registros que estão diferentes e adicionar novos registros conforme avanço de datas.
    """
    tv = TvDatafeed(username, password)

    instances = BrRealEstate_S.objects.all()

    if instances.exists():
        for instance in instances:
            ticker_symbol = instance.ticker
            print(ticker_symbol)
            try:
                historico = tv.get_hist(symbol=ticker_symbol, exchange='BMFBOVESPA', interval=Interval.in_daily, n_bars=5000)
                historico = historico.reset_index()
                historico['datetime'] = historico['datetime'].dt.date

                historico = historico[['datetime', 'close', 'volume']]
                historico = historico.rename(columns={'datetime': 'date', 'close': 'price'})

                existing_entries = BrRealEstate.objects.filter(ticker_id=instance.id).values('id', 'date', 'price', 'volume')
                existing_data = {entry['date']: (entry['id'], entry['price'], entry['volume']) for entry in existing_entries}

                bulk_create = []
                bulk_update = []

                for _, row in historico.iterrows():
                    new_date = row['date']
                    new_price = round(row['price'], 2)
                    new_volume = row['volume']

                    if new_date in existing_data:
                        existing_id, current_price, current_volume = existing_data[new_date]
                        if current_price != new_price or current_volume != new_volume:
                            model_entry = BrRealEstate(
                                id=existing_id,
                                date=new_date,
                                ticker_id=instance.id,
                                price=new_price,
                                volume=new_volume
                            )
                            bulk_update.append(model_entry)
                            log_message(f'Atualizado: {ticker_symbol} - Data: {new_date}, Preço: {new_price}, Volume: {new_volume}')
                    else:
                        model_entry = BrRealEstate(
                            date=new_date,
                            ticker_id=instance.id,
                            price=new_price,
                            volume=new_volume
                        )
                        bulk_create.append(model_entry)
                        log_message(f'Criado: {ticker_symbol} - Data: {new_date}, Preço: {new_price}, Volume: {new_volume}')

                if bulk_create:
                    BrRealEstate.objects.bulk_create(bulk_create)
                if bulk_update:
                    BrRealEstate.objects.bulk_update(bulk_update, ['price', 'volume'])

                if not bulk_create and not bulk_update:
                    log_message(f'Nada a fazer para {ticker_symbol}.')
                    continue

            except Exception as e:
                log_message(f'Erro ao coletar dados para {ticker_symbol}: {e}')
                input('Pressione Enter para continuar para o próximo ativo...')

def get_crypto_data():
    """
    Função para atualizar os dados de Criptomoedas.
    Se o banco tiver vazio, adicionará todos os dados. Se o banco tiver com dados, irá comparar e
    atualizar registros que estão diferentes. E adicionar novos registros conforme avanço de datas.
    """
    instances = Crypto_S.objects.all()

    if not instances.exists():
        log_message(f'Tabela {Crypto_S.__name__} está vazia. Coletando dados para todos os registros.')

    if instances.exists():
        for instance in instances:
            ticker_symbol = instance.ticker + '-USD'
            try:
                historico = yf.Ticker(ticker_symbol).history(period='max', interval='1d')
                historico = historico.reset_index()
                historico['Date'] = historico['Date'].dt.date

                existing_entries = Crypto.objects.filter(ticker_id=instance.id).values('id', 'date', 'price', 'volume')
                existing_data = {entry['date']: (entry['id'], entry['price'], entry['volume']) for entry in existing_entries}

                bulk_create = []
                bulk_update = []

                for _, row in historico.iterrows():
                    new_date = row['Date']
                    new_price = round(row['Close'], 2)
                    new_volume = row['Volume']

                    if new_date in existing_data:
                        existing_id, current_price, current_volume = existing_data[new_date]
                        if current_price != new_price or current_volume != new_volume:
                            model_entry = Crypto(
                                id=existing_id,
                                date=new_date,
                                ticker_id=instance.id,
                                price=new_price,
                                volume=new_volume
                            )
                            bulk_update.append(model_entry)
                            log_message(f'Atualizado: {ticker_symbol} - Data: {new_date}, Preço: {new_price}, Volume: {new_volume}')
                    else:
                        model_entry = Crypto(
                            date=new_date,
                            ticker_id=instance.id,
                            price=new_price,
                            volume=new_volume
                        )
                        bulk_create.append(model_entry)
                        log_message(f'Criado: {ticker_symbol} - Data: {new_date}, Preço: {new_price}, Volume: {new_volume}')

                if bulk_create:
                    Crypto.objects.bulk_create(bulk_create)
                if bulk_update:
                    Crypto.objects.bulk_update(bulk_update, ['price', 'volume'])

                if not bulk_create and not bulk_update:
                    log_message(f'Nada a fazer para {ticker_symbol}.')
                    continue

            except Exception as e:
                log_message(f'Erro ao coletar dados para {ticker_symbol}: {e}')
                input('Pressione Enter para continuar para o próximo ativo...')

def get_br_treasure_data():
    """
    Função para atualizar os dados do Tesouro Direto BR.
    Se o banco tiver vazio, adicionará todos os dados. Se o banco tiver com dados, irá comparar e
    atualizar registros que estão diferentes. E adicionar novos registros conforme avanço de datas.
    """
    instances = BrTreasure_S.objects.all()

    if not instances.exists():
        log_message(f'Tabela {BrTreasure_S.__name__} está vazia. Coletando dados para todos os registros.')

    if instances.exists():
        try:
            data = pd.read_csv('BrTreasure.csv', sep=';')
            data['Data Base'] = pd.to_datetime(data['Data Base'], format="%d/%m/%Y").dt.date
            data['Data Vencimento'] = pd.to_datetime(data['Data Vencimento'], format="%d/%m/%Y").dt.date
            data['Taxa Compra Manha'] = data['Taxa Compra Manha'].str.replace(',', '.').astype(float)
            data['PU Compra Manha'] = data['PU Compra Manha'].str.replace(',', '.').astype(float)

            for instance in instances:
                try:
                    title_type = instance.title_type
                    maturity = instance.maturity

                    filtered_data = data[(data['Tipo Titulo'] == title_type) & (data['Data Vencimento'] == maturity)]

                    if not filtered_data.empty:
                        log_message(f'Processando dados para o título: {instance.title}')

                        existing_entries = BrTreasure.objects.filter(title=instance)
                        existing_entries_dict = {entry.date: entry for entry in existing_entries}

                        bulk_create = []
                        bulk_update = []

                        for _, row in filtered_data.iterrows():
                            new_date = row['Data Base']
                            new_profitability = row['Taxa Compra Manha']
                            new_price = row['PU Compra Manha']

                            if new_date in existing_entries_dict:
                                existing_entry = existing_entries_dict[new_date]

                                if existing_entry.price != new_price or existing_entry.profitability != new_profitability:
                                    existing_entry.profitability = new_profitability
                                    existing_entry.price = new_price
                                    bulk_update.append(existing_entry)
                                    log_message(f'Atualizado: {instance.title} Data: {new_date}, Preço: {new_price}, Taxa: {new_profitability}')
                            else:
                                new_entry = BrTreasure(
                                    date=new_date,
                                    title=instance,
                                    profitability=new_profitability,
                                    price=new_price
                                )
                                bulk_create.append(new_entry)
                                log_message(f'Criado: {instance.title} Data: {new_date}, Preço: {new_price}, Taxa: {new_profitability}')

                        if bulk_create:
                            print(f'Inserindo registros para {instance.title}: {bulk_create}')
                            BrTreasure.objects.bulk_create(bulk_create)

                        if bulk_update:
                            print(f'Atualizando registros para {instance.title}: {bulk_update}')
                            BrTreasure.objects.bulk_update(bulk_update, ['profitability', 'price'])

                        if not bulk_create and not bulk_update:
                            log_message(f'Nada a fazer para {instance.title}.')
                    else:
                        log_message(f'Sem dados para o título {instance.title}.')

                except Exception as e:
                    log_message(f'Erro ao processar o título {instance.title}: {e}')
                    input('Pressione Enter para continuar para o próximo título...')

            print('Função get_br_treasure_data() finalizada.')

        except Exception as e:
            log_message(f'Erro ao processar o arquivo CSV: {e}')

def coletar_e_salvar_dados():
    app_label = 'marketdata'
    models = apps.get_app_config(app_label).get_models()
    
    for model in models:
        model_name = model._meta.model_name

        if hasattr(model, 'ticker_id'):
            tickers = model.objects.values('ticker_id').annotate(min_date=Min('date')).distinct()

            for ticker in tickers:
                data_mais_antiga = model.objects.filter(ticker_id=ticker['ticker_id'], date=ticker['min_date']).first()
                
                if data_mais_antiga:
                    Stats.objects.create(
                        ticker=data_mais_antiga.ticker,
                        data_inicio=data_mais_antiga.date,
                        model=model_name
                    )
                    print(f'{data_mais_antiga.ticker} - {data_mais_antiga.date} salvos com sucesso!')

        elif hasattr(model, 'title_id'):
            titles = model.objects.values('title_id').annotate(min_date=Min('date')).distinct()

            for title in titles:
                data_mais_antiga = model.objects.filter(title_id=title['title_id'], date=title['min_date']).first()
                
                if data_mais_antiga:
                    Stats.objects.create(
                        ticker=data_mais_antiga.title,
                        data_inicio=data_mais_antiga.date,
                        model=model_name
                    )
                    print(f'{data_mais_antiga.title} - {data_mais_antiga.date} salvos com sucesso!')

def execute_all():
    """
    Executa as funções para coletar dados e salvar no banco de dados.
    """
    get_marketdata()
    get_crypto_data()
    get_br_treasure_data()
    get_br_real_estate_data()
    coletar_e_salvar_dados()
