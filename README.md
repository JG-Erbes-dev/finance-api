
# finance-api

API Rest ainda em desenvolvimento para obtenção de dados econômicos e dados de ativos financeiros.
A API conta scripts e commands para atualização dos dados de forma diária de forma automatizada. (automatização ainda não implementada)

Os dados foram retirados das fontes:<br>
B3<br>
BCB<br>
Coinmarketdata<br>
Fred<br>
Tradingview<br>
Tesouro Direto<br>
YFinance<br>

<h1 align="center"> 
    :construction:  Projeto em construção  :construction:
</h1>

## Ferramentas
API feita em Django e Django Rest Framework

## Etiquetas
![Static Badge](https://img.shields.io/badge/License-MIT-orange?style=plastic)
![Static Badge](https://img.shields.io/badge/Framework-Django-green?style=plastic)
![Static Badge](https://img.shields.io/badge/Language-Python-blue?style=plastic)
![Static Badge](https://img.shields.io/badge/Django-Rest%20Framework-red?style=plastic)


## Dados Econômicos
Até o momento possui rotas para:<br>

1- Taxa de Juros Brasileira - interest-rate/br/<br>
2- Taxa de Juros dos Estados Unidos - interest-rate/us/<br>
3- CDI Brasileiro Diário - cdi/br/<br>
4- CDI Brasileiro Acumulado - cdi/br/cumulative/<br>
5- Inflação Brasileira Mensal - inflation/br/<br>
6- Inflação Brasileira Acumulada - inflation/br/cumulative/<br>
7- Inflação dos Estados Unidos Acumulada - inflation/us/<br>
8- Taxa de Câmbio Dólar x Real - exchange/dollar-rate/<br>
9- Ìndice amplo de Commodities - commodities/price/<br>


## Dados Financeiros
Até o momento possui rotas para dados diários:<br>

1- Ações Brasileiras - stock/br/<br>
2- Ações dos Estados Unidos - stock/us/<br>
3- FIIs Brasileiros - realestate/br/<br>
4- Etfs dos Estados Unidos - etf/us/<br>
5- Criptomoedas - crypto/<br>
6- Tesouro Direto Brasileiro - treasure/br/<br>

## Eventos Corporativos
Até o momento possui rotas para dados diários:<br>

1- Ações Brasileiras - events/stock/br/<br>
2- Ações dos Estados Unidos - events/stock/us/<br>
3- FIIs Brasileiros - events/realestate/br/<br>
4- Etfs dos Estados Unidos - events/etf/us/<br>


# Estatísticas e Informações
Rotas feitas para facilitar consulta de dados de ativos e períodos existentes.<br>
Até o momento possui rotas para:<br>

## 1- Estatísticas Gerais da API - stats/
![alt text](images/image.png)

## 2- Ações Brasileiras - stats/stock/br/
![alt text](images/image-1.png)

## 3- Ações dos Estados Unidos - stats/stock/us/
![alt text](images/image-2.png)

## 4- FIIs Brasileiros - stats/realestate/br/
![alt text](images/image-3.png)

## 5- Etfs dos Estados Unidos - stats/etf/us/
![alt text](images/image-4.png)

## 6- Criptomoedas - stats/crypto/
![alt text](images/image-5.png)

## 7- Tesouro Direto Brasileiro - stats/treasure/br/
![alt text](images/image-6.png)


# Ainda falta implementar:
Módulos em fase de estudo e estruturação do planejamento:<br>

1- Métricas de Valuation<br>
2- Dados dos Balanços<br>
