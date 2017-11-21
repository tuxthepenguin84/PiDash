##Modules
import json
from pprint import pprint
import requests
from secrets import *
import urllib.parse

##Variables
debug = 0
#Weather Underground variables
wAPIURL = 'http://api.wunderground.com/api/'
wState = 'CA'
wCity = 'Walnut_Creek'
wFullURL = wAPIURL + wAPIKey + '/forecast/q/' + wState + '/' + wCity + '.json'

##Weather Underground script
#Get JSON data from WU
wJSONData = requests.get(wFullURL).json()
finalForecast = []
for eachDay in wJSONData['forecast']['simpleforecast']['forecastday'][1:4]:
    forecast = []
    forecast.append(eachDay['date']['weekday'])
    forecast.append(eachDay['conditions'])
    forecast.append(eachDay['high']['fahrenheit'])
    forecast.append(eachDay['low']['fahrenheit'])
    forecast.append(eachDay['qpf_allday']['in'])
    forecast.append(eachDay['avewind']['mph'])
    forecast.append(eachDay['avehumidity'])
    finalForecast.append(forecast)

#Print all JSON data for testing
if debug == 1:
    pprint(wJSONData)

#Final variables
weatherForecastOutput = ('\n'.join([
    'var w1Day = "' + str(finalForecast[0][0]) + '";',
    'var w1Conditions = "' + str(finalForecast[0][1]) + '";',
    'var w1Temp = "' + "High " + str(finalForecast[0][2]) + " F" + " | " + " Low " + str(finalForecast[0][3]) + " F" + '";',
    'var w1QPF = "' + str(finalForecast[0][4]) + " inches" + '";',
    'var w1Wind = "' + str(finalForecast[0][5]) + " mph" + '";',
    'var w1Humidity = "' + str(finalForecast[0][6]) + "%" + '";',
    'var w2Day = "' + str(finalForecast[1][0]) + '";',
    'var w2Conditions = "' + str(finalForecast[1][1]) + '";',
    'var w2Temp = "' + "High " + str(finalForecast[1][2]) + " F" + " | " + " Low " + str(finalForecast[1][3]) + " F" + '";',
    'var w2QPF = "' + str(finalForecast[1][4]) + " inches" + '";',
    'var w2Wind = "' + str(finalForecast[1][5]) + " mph" + '";',
    'var w2Humidity = "' + str(finalForecast[1][6]) + "%" + '";',
    'var w3Day = "' + str(finalForecast[2][0]) + '";',
    'var w3Conditions = "' + str(finalForecast[2][1]) + '";',
    'var w3Temp = "' + "High " + str(finalForecast[2][2]) + " F" + " | " + " Low " + str(finalForecast[2][3]) + " F" + '";',
    'var w3QPF = "' + str(finalForecast[2][4]) + " inches" + '";',
    'var w3Wind = "' + str(finalForecast[2][5]) + " mph" + '";',
    'var w3Humidity = "' + str(finalForecast[2][6]) + "%" + '";',
    '\n',
    ]))
