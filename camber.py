import numpy as np
import math
from Readline import xyvalues

from numpy.polynomial import Polynomial
import warnings


x_list = []
y_list = []

def camber(sample):
    x,y1 = xyvalues(sample,1)
    _,y2 = xyvalues(sample,199)
    x_list.append(x)
    y_list.append((y1+y2)/2)

    for i in range(10,100,10):
        x,y1 = xyvalues(sample,i)
        _,y2 = xyvalues(sample,200-i)
        x_list.append(x)
        y_list.append((y1+y2)/2)

    x = np.array(x_list)
    y = np.array(y_list)
    z = np.polyfit(x, y, 2)
    eq = str(z[2]) + " +" + str(z[1]) + "*x +" + str(z[0]) + "*x^2"
    eq_deriv = str(z[1]) + " +" + str(z[0]*2) + "*x"
    
    eq = eq.replace("+-", "-")
    eq_deriv = eq_deriv.replace("+-", "-")

    #find root of derivative except doesn't work
    if z[0] != 0:
        x_maxcamb = -1*z[1]/(z[0]*2)
        maxcamb = z[2] + z[1]*x_maxcamb + z[0]*(x_maxcamb)^2


    return eq, eq_deriv, x_maxcamb, maxcamb

print(camber(0))