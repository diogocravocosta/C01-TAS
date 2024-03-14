import numpy as np
import math
from Readline import xyvalues

from numpy.polynomial import Polynomial
import warnings


x_list = []
y_list = []

def camber(sample): # returns:   polynomial for camber line,   x value of max camb,   max camb,   LE angle (rad),   TE angle (rad)
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
    eq = eq.replace("+-", "-")

    #eq_deriv = str(z[1]) + " +" + str(z[0]*2) + "*x"     derivative
    #eq_deriv = eq_deriv.replace("+-", "-")

    x_maxcamb = -1*z[1]/(z[0]*2)    #root of derivative
    maxcamb = z[2] + z[1]*x_maxcamb + z[0]*(x_maxcamb**2)  #root of derivative used in eq

    LE_angle = np.arctan(  z[1] + z[0]*2*0  )     #arctan in radians of derivative at x = 0 & x = 1
    TE_angle = np.arctan(  z[1] + z[0]*2*1  )
    return eq, x_maxcamb, maxcamb, LE_angle, TE_angle