##Modules
import datetime
import json
from pprint import pprint
import re
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
alexisWalk = 3 #Number of minutes walking from Alexis's car to station
samWalk = 6 #Number of minutes walking from Sam's car to station
allTrains = []
alexisTrain = []
samTrain = []
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
gJSONData = requests.get(gFullURL).json()
#Get JSON data from BART
bJSONData = requests.get(bFullURL).json()

#Print all JSON data for testing
if debug == 1:
    pprint(gJSONData)
    pprint(bJSONData)

#Get Google Maps travel time and convert to minutes
gDurationSecs = gJSONData['routes'][0]['legs'][0]['duration_in_traffic']['value']
gDurationMins = int(round(gDurationSecs/60,0))

#Time from the house to the station
samTravelTime = gDurationMins + samWalk
alexisTravelTime = gDurationMins + alexisWalk

#Gather all train departures
for eachDestination in bJSONData['root']['station'][0]['etd']:
    for eachMinute in (eachDestination['estimate']):
        train = []
        if eachMinute['minutes'] != 'Leaving':
            train.append(int(eachMinute['minutes']))
            train.append(int(eachMinute['delay']))
            allTrains.append(train)

#Sort train data by soonest departure time
allTrains = sorted(allTrains)

#Find next train for each person
for eachTrain in allTrains:
    if eachTrain[0] > alexisTravelTime:
        alexisTrain = eachTrain[0:2]
        break
for eachTrain in allTrains:
    if eachTrain[0] > samTravelTime:
        samTrain = eachTrain[0:2]
        break

#Time left to leave is soonest departing train minus travel time to staion from the house
samTimeLeftToLeave = samTrain[0] - samTravelTime
alexisTimeLeftToLeave = alexisTrain[0] - alexisTravelTime
currentTime = datetime.datetime.now()
samLeaveAt = datetime.datetime.time(currentTime + datetime.timedelta(minutes=samTimeLeftToLeave)).strftime('%I:%M %p')
alexisLeaveAt = datetime.datetime.time(currentTime + datetime.timedelta(minutes=alexisTimeLeftToLeave)).strftime('%I:%M %p')
#Fix leading 0 in time
samLeaveAt = re.sub(r'^0','',samLeaveAt)
alexisLeaveAt = re.sub(r'^0','',alexisLeaveAt)

#Get amount of time the train is delayed
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
    'var alexisLeaveAt = "' + str(alexisLeaveAt) + '";',
    'var samLeaveAt = "' + str(samLeaveAt) + '";',
    'var alexisLeaveBy = "' + 'within ' + str(alexisTimeLeftToLeave) + ' minutes' + '";',
    'var samLeaveBy = "' + 'within ' + str(samTimeLeftToLeave) + ' minutes' + '";',
    'var alexisDelay = "' + str(alexisTrain[1]) + '";',
    'var samDelay = "' + str(samTrain[1]) + '";',
    '\n',
    ]))

