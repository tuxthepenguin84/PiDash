##Modules
import fileinput
import time
from catchbart import catchBartOutput
from weather import weatherOutput
from weatherforecast import weatherForecastOutput
from stockscurrencies import stocksCurrenciesOutput

##Begin Script
scriptStart = '<script>\n'
scriptEnd = '</script>\n'
currentTime = ('\n'.join([
    'var currentTime = "' + str(time.ctime()) + '";',
    '\n',
    ]))

#Clear index.html
open('../html/index.html', 'w').close()
#Reopen index.html with Append
with open('../html/index.html', 'a') as outfile:
    for eachLine in fileinput.FileInput('../html/index-custom-base.html'):
        if "</head>" in eachLine:
            eachLine=eachLine.replace(eachLine,eachLine + scriptStart + \
                                      currentTime + \
                                      weatherOutput + \
                                      weatherForecastOutput + \
                                      stocksCurrenciesOutput + \
                                      catchBartOutput + \
                                      scriptEnd)
            outfile.write(eachLine)
        else:
            outfile.write(eachLine)
    fileinput.close()
outfile.close()

##Functionality to add
#BART load factor
#Radar animated
#Time stamp
#Send message
