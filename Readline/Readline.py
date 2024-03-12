import numpy as np
import math


f = open("Random_samples.txt", "r") 
content = f.readlines()

newsample = ""
currentsamples = 0
for i in range(0,len(content)):
    currentline = content[i]
    if currentline.find("[[") != -1:
        newsample = newsample + "N" + str(currentsamples) + "L" + str(i)
        currentsamples += 1


def xyvalues(sample, line):
    relevantstring = newsample[newsample.find("N"+str(sample)):newsample.find("N"+str(sample+1))]
    samplestart = relevantstring[ relevantstring.find("L")+1:]
    samplestart
    line = line + int(samplestart) - 1
    lineStr = content[line]
    xval = float(lineStr[3:17])
    yval = float(lineStr[18:33])
    return xval, yval

#print(xyvalues(2,2))