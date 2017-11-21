##Modules
import json
from pprint import pprint
import requests
from secrets import *
import urllib.parse

##Variables
debug = 0
#Google variables
gAPIURL = 'https://maps.googleapis.com/maps/api/directions/json?'
gDestination = 'Lafayette Bart Station'
gDepartTime = 'now'
gFullURL = gAPIURL + \
                  'origin=' + urllib.parse.quote_plus(gOrigin) + \
                  '&destination=' + urllib.parse.quote_plus(gDestination) + \
                  '&departure_time=' + gDepartTime + \
                  '&traffic_model=best_guess'+ \
                  '&key=' + gAPIKey

#BART variables
bSamWalkingFactor = 6 #Number of minutes walking from Sam's car to station
bAlexisWalkingFactor = 2 #Number of minutes walking from Alexis's car to station
bAPIURL = 'http://api.bart.gov/api/etd.aspx?'
bStation = 'lafy'
bFullURL = bAPIURL + \
                'cmd=etd' + \
                '&orig=' + bStation + \
                '&key=' + bAPIKey + \
                '&dir=s' + \
                '&json=y'

##Begin script
#Get JSON data from Google
gJSONData = requests.get(gFullURL).json() #Possible to limit/filter data here?
gDurationSecs = gJSONData['routes'][0]['legs'][0]['duration_in_traffic']['value']
gDurationMins = int(round(gDurationSecs/60,0))
#Time from the house to the station
samHouseToStationTime = gDurationMins + bSamWalkingFactor
alexisHouseToStationTime = gDurationMins + bAlexisWalkingFactor

#Get JSON data from BART
bJSONData = requests.get(bFullURL).json()
allTrains = []
alexisTrain = []
samTrain = []
for eachDestination in bJSONData['root']['station'][0]['etd']:
    for eachMinute in (eachDestination['estimate']):
        train = []
        if eachMinute['minutes'] != 'Leaving':
            train.append(int(eachMinute['minutes']))
            train.append(int(eachMinute['delay']))
            allTrains.append(train)

#Sort train data by soonest departure time
allTrains = sorted(allTrains)

#Find next train
for eachTrain in allTrains:
    if eachTrain[0] > alexisHouseToStationTime:
        alexisTrain = eachTrain[0:2]
        break
for eachTrain in allTrains:
    if eachTrain[0] > samHouseToStationTime:
        samTrain = eachTrain[0:2]
        break

#Print all JSON data for testing
if debug == 1:
    pprint(gJSONData)
    pprint(bJSONData)
    
#Time left to leave is soonest departing train minus travel time to staion from the house
samTimeLeftToLeave = samTrain[0] - samHouseToStationTime
alexisTimeLeftToLeave = alexisTrain[0] - alexisHouseToStationTime

if (alexisTrain[1] == 0):
    alexisTrain.insert(1, 'None')
elif (alexisTrain[1] >= 900):
    alexisTrain.insert(1, '> 15 minutes')
elif (alexisTrain[1] >= 600):
    alexisTrain.insert(1, '10-15 minutes')
elif (alexisTrain[1] >= 300):
    alexisTrain.insert(1, '5-10 minutes')
elif (alexisTrain[1] >= 60):
    alexisTrain.insert(1, '1-5 minutes')
elif (alexisTrain[1] >= 1):
    alexisTrain.insert(1, '< 1 minute')

if (samTrain[1] == 0):
    samTrain.insert(1, 'None')
elif (samTrain[1] >= 900):
    samTrain.insert(1, '> 15 minutes')
elif (samTrain[1] >= 600):
    samTrain.insert(1, '10-15 minutes')
elif (samTrain[1] >= 300):
    samTrain.insert(1, '5-10 minutes')
elif (samTrain[1] >= 60):
    samTrain.insert(1, '1-5 minutes')
elif (samTrain[1] >= 1):
    samTrain.insert(1, '< 1 minute')

#Format data into HTML for pickup by main.py
catchBartOutput = ('\n'.join([
    'var alexisNextTrain = "' + str(alexisTrain[0]) + ' minutes' + '";',
    'var samNextTrain = "' + str(samTrain[0]) + ' minutes' + '";',
    'var alexisLeaveBy = "' + str(alexisTimeLeftToLeave) + ' minutes' + '";',
    'var samLeaveBy = "' + str(samTimeLeftToLeave) + ' minutes' + '";',
    'var alexisDelay = "' + str(alexisTrain[1]) + '";',
    'var samDelay = "' + str(samTrain[1]) + '";',
    '\n',
    ]))

