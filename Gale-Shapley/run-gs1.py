#!/usr/bin/python
# Naol Legesse
# Script used to run gs1
# help was provided by Trent Deylor

immport os

for i in range(100,2001,100):
    os.system('python ./gs1.py {} >> data.txt'.format(i))

#The fit model will display results and plot graph
os.system('/usr/bin/gunplot -persist model.gpt')
