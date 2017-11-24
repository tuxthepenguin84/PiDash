##Modules
import json
from pprint import pprint
import requests
from secrets import *

##Variables
debug = 0
#Weather Underground variables
wAPIURL = 'http://api.wunderground.com/api/'
wState = 'CA'
wCities = ['San Francisco', 'Walnut Creek']
allWeatherData = []

##Weather Underground script
#Get JSON data from WU
for eachCity in wCities:
    wCity = []
    wFullURL = wAPIURL + wAPIKey + '/conditions/q/' + wState + '/' + eachCity + '.json'
    wJSONData = requests.get(wFullURL).json()
    
    #Print all JSON data for testing
    if debug == 1:
        pprint(wJSONData)
        
    wWeather = wJSONData['current_observation']['weather']
    wTemp = wJSONData['current_observation']['temp_f']
    wPrecip = wJSONData['current_observation']['precip_today_in']
    wWind = wJSONData['current_observation']['wind_mph']
    wHumidity = wJSONData['current_observation']['relative_humidity']
    wCity.append(wWeather)
    wCity.append(wTemp)
    wCity.append(wPrecip)
    wCity.append(wWind)
    wCity.append(wHumidity)
    allWeatherData.append(wCity)

#Final variables
weatherOutput = ('\n'.join([
    'var wCity1 = "' + str(wCities[0]) + '";',
    'var wWeather1 = "' + str(allWeatherData[0][0]) + '";',
    'var wTemp1 = "' + str(allWeatherData[0][1]) + " F" + '";',
    'var wPrecip1 = "' + str(allWeatherData[0][2]) + " in" + '";',
    'var wWind1 = "' + str(allWeatherData[0][3]) + " mph " + '";',
    'var wHumidity1 = "' + str(allWeatherData[0][4]) + '";',
    'var wCity2 = "' + str(wCities[1]) + '";',
    'var wWeather2 = "' + str(allWeatherData[1][0]) + '";',
    'var wTemp2 = "' + str(allWeatherData[1][1]) + " F" + '";',
    'var wPrecip2 = "' + str(allWeatherData[1][2]) + " in" + '";',
    'var wWind2 = "' + str(allWeatherData[1][3]) + " mph " + '";',
    'var wHumidity2 = "' + str(allWeatherData[1][4]) + '";',
    '\n',
    ]))
