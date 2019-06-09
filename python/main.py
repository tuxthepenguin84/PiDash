##Modules
from time import localtime, strftime
import fileinput
print('Refreshing BART data... ', end="")
from catchbart import catchBartOutput
print('DONE')
print('Refreshing Weather data... ', end="")
#from weather import weatherOutput
print('DONE')
print('Refreshing Stock & Currency data... ', end="")
from stockscurrencies import stocksCurrenciesOutput
print('DONE')

##Begin Script
scriptStart = '<script>\n'
scriptEnd = '</script>\n'
currentTime = ('\n'.join([
    'var currentTime = "' + strftime("%a, %b %d %I:%M %p", localtime()) + '";',
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
                                      catchBartOutput + \
                                      stocksCurrenciesOutput + \
#                                      weatherOutput + \
                                      scriptEnd)
            outfile.write(eachLine)
        else:
            outfile.write(eachLine)
    fileinput.close()
outfile.close()

##Functionality to add
#BART load factor
#Radar animated
#Send message
