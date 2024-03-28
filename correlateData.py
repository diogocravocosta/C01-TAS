import numpy as np
import math
from Readline import xyvalues
import scipy

from camber import camber
from input_data_cleaner import get_input_data
from numpy.polynomial import Polynomial
import warnings

from thickness_characteristics_extractor import random_thickness_to_chord, input_thickness_to_chord

#xlist = [] #parameters
#ylist = [] #characteristic

#def correlateData(characteristic, Parameter, File):
#    filelen = 10000
#    if File == 0: #"output"
#        return 1
#    elif File == 1: #"input"
#        _,_,_,A = get_input_data()
#        filelen = len(A)
#        for i in range(min, max): #range(len(A)):
#            xlist.append(A[i][Parameter])
#    else:
#        return False
#
#    if characteristic < 6:
#        for i in range(min, max):
#            #r = 5
#            B = camber(i,File)
#            ylist.append(B[characteristic])
#
#
#    for i in range(0,len(ylist)):
#        file1.write(str(xlist[i])+","+str(ylist[i])+"\n")
#
#    print("done")
#    #return 8 #xlist[1],ylist[1]



#def correlateData():
    #filelen = 10000
    #if File == 0: #"output"
    #    return 1
    #elif File == 1: #"input"
    #    _,_,_,A = get_input_data()
    #    filelen = len(A)
    #    for i in range(min, max): #range(len(A)):
    #        xlist.append(A[i][Parameter])
    #else:
    #    return False

    #if characteristic < 6:
    #    for i in range(min, max):
    #        #r = 5
    #        B = camber(i,File)
    #        ylist.append(B[characteristic])



    #for i in range(0,len(ylist)):
    #    file1.write(str(xlist[i])+","+str(ylist[i])+"\n")



file1 = open("Regressdata.txt", "a")

min = 0
max = min + 20

def correlateData():

    for num in range(min, max):
        _,_,_,A = get_input_data()
        B,C,D,E,F = camber(num,1)
        G,H = input_thickness_to_chord(num)

        line = str(num) + A[num] + "(" + C + "," + D + "," + E + "," + F + "," + G + "," + H + ")"

        file1.write(line+"\n")

    print("done")



# Characteristic index
    
# 0 - x_maxcamb
# 1 - maxcamb
# 2 - LE_angle
# 3 - TE_angle
# 4 - thickness_to_chord
# 5 - thickness_pos



correlateData()


file1.close()






#finalDat = []
#def dataToArray():
#    file2 = open("Regressdata.txt", "r")
#    content = file2.readlines()
#    for i in range(len(content)):
#        finalDat.append(content[i][:content[i].find(",")] , content[i][content[i].find(",")+1:])
#    return finalDat
#    file2.close()