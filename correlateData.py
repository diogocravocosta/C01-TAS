import numpy as np
import math
from Readline import xyvalues
import scipy

from camber import camber
from input_data_cleaner import get_input_data
from numpy.polynomial import Polynomial
import warnings


file1 = open("data.txt", "a")


xlist = [] #parameters
ylist = [] #characteristic


min = 400
max = min + 200

def correlateData(characteristic, Parameter, File):
    filelen = 10000
    if File == 0: #"output"
        return 1
    elif File == 1: #"input"
        _,_,_,A = get_input_data()
        filelen = len(A)
        for i in range(min, max): #range(len(A)):
            xlist.append(A[i][Parameter])
    else:
        return False

    if characteristic < 6:
        for i in range(min, max):
            #r = 5
            B = camber(i,File)
            ylist.append(B[characteristic])


    for i in range(0,len(ylist)):
        file1.write(str(xlist[i])+","+str(ylist[i])+"\n")

    print("done")
    #return 8 #xlist[1],ylist[1]




file1.close()


finalDat = []
def dataToArray():
    file2 = open("data.txt", "r")
    content = file2.readlines()
    for i in range(len(content)):
        finalDat.append(content[i][:content[i].find(",")] , content[i][content[i].find(",")+1:])
    return finalDat
    file2.close()