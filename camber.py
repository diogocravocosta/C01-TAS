import numpy as np
import math
from Readline import xyvalues

from numpy.polynomial import Polynomial
import warnings

x_list = []
y_list = []

def camber(sample): # returns:   polynomial for camber line,   x value of max camb,   max camb,   LE angle (rad),   TE angle (rad)

    for i in range(1,101,1):
        x,y1 = xyvalues(sample,i)
        _,y2 = xyvalues(sample,200-i)
        x_list.append(x)
        y_list.append((y1+y2)/2)

    x = np.array(x_list)
    y = np.array(y_list)
    z = np.polyfit(x, y, 7)
    eq = str(z[7]) + " + " + str(z[6]) + "*x + " + str(z[5]) + "*x^2 + " + str(z[4]) + "*x^3 + " + str(z[3]) + "*x^4 + " + str(z[2]) + "*x^5 + " + str(z[1]) + "*x^6 + " + str(z[0]) + "*x^7"
    eq = eq.replace("+ -", "- ")

    deriv = np.polyder(np.poly1d(z))
    rootlist = np.roots(deriv)
    x_maxcamb = -1
    maxcamb = -1
    for root in rootlist:
        string = str(root)
        complexnt = string.find("0j") # real-valued root
        if complexnt != -1 and float(string[1:complexnt-1]) > 0 and float(string[1:complexnt-1]) < 1:
            tempx_maxcamb = float(string[1:complexnt-1])
            tempmaxcamb = z[7] + z[6]*tempx_maxcamb + z[5]*(tempx_maxcamb**2) + z[4]*(tempx_maxcamb**3) + z[3]*(tempx_maxcamb**4) + z[2]*(tempx_maxcamb**5) + z[1]*(tempx_maxcamb**6) + z[0]*(tempx_maxcamb**7)  #root of derivative used in eq
            if tempmaxcamb > maxcamb: # ensure highest camber peak is chosen, not just the last
                x_maxcamb = tempx_maxcamb
                maxcamb = tempmaxcamb

    deriv_0 = z[6]
    deriv_1 = z[6] + 2*z[5] + 3*z[4] + 4*z[3] + 5*z[2] + 6*z[1] + 7*z[0]  
    LE_angle = np.arctan(  deriv_0  )     # arctan in radians of derivative at x = 0 & x = 1
    TE_angle = np.arctan(  deriv_1  )

    return eq, x_maxcamb, maxcamb, LE_angle, TE_angle