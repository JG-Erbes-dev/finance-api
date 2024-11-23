import yfinance as yf
import pandas as pd
from corporateevents.models import BrStock, UsStock, BrRealEstate, UsEtf
from search.models import BrStock as BrStock_S, UsStock as UsStock_S, BrRealEstate as BrRealEstate_S, UsEtf as UsEtf_S


MODELS_TO_SEARCH = [
    {'model': BrStock_S, 'is_brazilian': True, 'save_model': BrStock},
    {'model': UsStock_S, 'is_brazilian': False, 'save_model': UsStock},
    {'model': BrRealEstate_S, 'is_brazilian': True, 'save_model': BrRealEstate},
    {'model': UsEtf_S, 'is_brazilian': False, 'save_model': UsEtf},
]

def log_message(message):
    """Função para logar mensagens."""
    print(message)

def get_corporate_events():
    """
    Função para atualizar os eventos corporativos de Ações Br e Us, FIIs e US ETFs.
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
                    dividends = yf.Ticker(ticker_symbol).dividends.reset_index()
                    dividends['Date'] = dividends['Date'].dt.date
                    dividends['Dividends'] = round(dividends['Dividends'],2)

                    splits = yf.Ticker(ticker_symbol).splits.reset_index()
                    splits['Date'] = splits['Date'].dt.date

                    dividends['event_type'] = 'dividendo'
                    splits['event_type'] = splits['Stock Splits'].apply(lambda x: 'desdobramento' if x > 1 else 'agrupamento')

                    dividends = dividends.rename(columns={'Date': 'event_date', 'Dividends': 'value'})
                    splits = splits.rename(columns={'Date': 'event_date', 'Stock Splits': 'value'})

                    events = pd.concat([dividends[['event_date', 'event_type', 'value']],
                                        splits[['event_date', 'event_type', 'value']]])

                    events = events.sort_values(by='event_date').reset_index(drop=True)

                    existing_entries = save_model.objects.filter(ticker_id=instance.id).values('event_date', 'event_type', 'value')
                    existing_data = {(entry['event_date']): (entry['id'], entry['event_type'], entry['value']) for entry in existing_entries}

                    bulk_create = []
                    bulk_update = []

                    for _, row in events.iterrows():
                        event_date = row['event_date']
                        new_event = row['event_type']
                        new_value = round(row['value'], 2)

                        if event_date in existing_data:
                            existing_id, current_event, current_value = existing_data[event_date]
                            if current_event != new_event or current_value != new_value:
                                model_entry = save_model(
                                    id=existing_id,
                                    event_date=event_date,
                                    ticker_id=instance.id,
                                    event_type=new_event,
                                    value=new_value
                                )
                                bulk_update.append(model_entry)
                                log_message(f'Atualizado: {ticker_symbol} - Data: {event_date}, Evento: {new_event}, Valor: {new_value}')
                        else:
                            model_entry = save_model(
                                event_date=event_date,
                                ticker_id=instance.id,
                                event_type=new_event,
                                value=new_value
                            )
                            bulk_create.append(model_entry)
                            log_message(f'Criado: {ticker_symbol} - Data: {event_date}, Evento: {new_event}, Valor: {new_value}')

                    if bulk_create:
                        save_model.objects.bulk_create(bulk_create)
                    if bulk_update:
                        save_model.objects.bulk_update(bulk_update, ['event_type', 'value'])

                    if not bulk_create and not bulk_update:
                        log_message(f'Nada a fazer para {ticker_symbol}.')
                        continue

                except Exception as e:
                    log_message(f'Erro ao coletar dados para {ticker_symbol}: {e}')
                    input('Pressione Enter para continuar para o próximo ativo...')

def execute_all():
    """
    Executa as funções para coletar dados e salvar no banco de dados.
    """
    get_corporate_events()
