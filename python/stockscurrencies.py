##Modules
import json
from pprint import pprint
import requests
from secrets import *

##Variables
debug = 0
#Alpha Vantage variables
avAPIURL = 'https://www.alphavantage.co/query?'
 

##Alpha Vantage script
#Get JSON data from AV
avCCSymbol = ['BTC','ETH','LTC']
avFunction = 'DIGITAL_CURRENCY_INTRADAY'
allCurrencyIntra = []
for eachCCSymbol in avCCSymbol:
    currency = []
    avFullURL = avAPIURL + 'function=' + avFunction + '&symbol=' + eachCCSymbol + '&market=USD' + '&apikey=' + avAPIKey
    avJSONData = requests.get(avFullURL).json()
    lastRefresh = avJSONData['Meta Data']['7. Last Refreshed']
    currentAll = avJSONData['Time Series (Digital Currency Intraday)'][lastRefresh]
    currentPrice = "%.2f" % float(currentAll['1a. price (USD)'])
    currency.append(currentPrice)
    allCurrencyIntra.append(currency)

avSMSymbol = ['ZNGA', 'MCK']
avFunction = 'TIME_SERIES_INTRADAY'
allStockIntra = []
for eachSMSymbol in avSMSymbol:
    stock = []
    avFullURL = avAPIURL + 'function=' + avFunction + '&symbol=' + eachSMSymbol + '&interval=1min' + '&apikey=' + avAPIKey
    avJSONData = requests.get(avFullURL).json()
    lastRefresh = avJSONData['Meta Data']['3. Last Refreshed']
    currentAll = avJSONData['Time Series (1min)'][lastRefresh]
    currentPrice = "%.2f" % float(currentAll['1. open'])
    stock.append(currentPrice)
    allStockIntra.append(stock)

#Print all JSON data for testing
if debug == 1:
    print(allCurrencyIntra)
    print(allStockIntra)

#Final variables
stocksCurrenciesOutput = ('\n'.join([
    'var btcPrice = "' + "$ " + str(allCurrencyIntra[0][0]) + '";',
    'var ethPrice = "' + "$ " + str(allCurrencyIntra[1][0]) + '";',
    'var ltcPrice = "' + "$ " + str(allCurrencyIntra[2][0]) + '";',
    'var zngaPrice = "' + "$ " + str(allStockIntra[0][0]) + '";',
    'var mckPrice = "' + "$ " + str(allStockIntra[1][0]) + '";',
    '\n',
    ]))
