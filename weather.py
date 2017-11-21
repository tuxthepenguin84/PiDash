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
wFullURL = wAPIURL + wAPIKey + '/conditions/q/' + wState + '/' + wCity + '.json'

##Weather Underground script
#Get JSON data from WU
wJSONData = requests.get(wFullURL).json()
wWeather = wJSONData['current_observation']['weather']
wTemp = wJSONData['current_observation']['temp_f']
wPrecip = wJSONData['current_observation']['precip_today_in']
wWind = wJSONData['current_observation']['wind_mph']
wHumidity = wJSONData['current_observation']['relative_humidity']

#Print all JSON data for testing
if debug == 1:
    pprint(wJSONData)

#Final variables
weatherOutput = ('\n'.join([
    'var wWeather = "' + str(wWeather) + '";',
    'var wTemp = "' + "Currently " + str(wTemp) + " F" + '";',
    'var wPrecip = "' + str(wPrecip) + " inches" + '";',
    'var wWind = "' + str(wWind) + " mph " + '";',
    'var wHumidity = "' + str(wHumidity) + '";',
    '\n',
    ]))
