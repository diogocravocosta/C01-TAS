import numpy as np
import math

f = open("Random_samples.txt", "r") 
content = f.readlines()

def xyvalues(sample, line):   
    lineStr = content[line+sample*201]
    if line > 0 and line < 200 and sample < 10000:
        xval = float(lineStr[3:17])
        yval = float(lineStr[18:33])    
        return xval, yval
    else:
        return False
 
def random_latentval(sample, latent):
    lineStr = content[(sample-1)*201]
    if latent > 0 and latent < 9 and sample < 10000:
        start = 0
        for i in range(latent):
            start = lineStr[start+2:].find(".") + start + 2
        stop = lineStr[start:].find(" ")
        sample = float(lineStr[start-2:start+stop])  
        return sample
    else:
        return False
    
#print(xyvalues(0,100))
"""   BETA: this code was written before realising each sample has exactly 199 datapoints smh
kilian lied

newsample = ""
currentsamples = 0
for i in range(0,len(content)):
    currentline = content[i]
    if currentline.find("[[") != -1:
        newsample = newsample + "N" + str(currentsamples) + "L" + str(i)
        currentsamples += 1

#newsample is a string of format N[sample number]L[first dataline of sample]
#looks like: N0L1N1L202N2L403

def xyvalues(sample, line):
    relevantstring = newsample[newsample.find("N"+str(sample)):newsample.find("N"+str(sample+1))] 
    samplestart = relevantstring[ relevantstring.find("L")+1:]
    
    next_relevantstring = newsample[newsample.find("N"+str(sample+1)):newsample.find("N"+str(sample+2))]
    next_samplestart = next_relevantstring[next_relevantstring.find("L")+1:]

    if sample == 9998:
        samplestart = 2009599
        next_samplestart = 2009800
    elif sample == 9999:
        samplestart = 2009800
        next_samplestart = 2010001
    
    line = line + int(samplestart) -1
    if line > int(next_samplestart) - 3 or line - int(samplestart) < 0 : #returns False if a line outside the specified sample is summoned
        return False
    else:

        lineStr = content[line]
        xval = float(lineStr[3:17])
        yval = float(lineStr[18:33])
        return xval, yval
"""