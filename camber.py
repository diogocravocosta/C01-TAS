import numpy as np
import math
from Readline import xyvalues
import scipy

from input_data_cleaner import get_input_data
from numpy.polynomial import Polynomial
import warnings

x_list = []
y_list = []


x = -1000 * np.ones(250)
y = -1000 * np.ones(250)
z = np.array([0,0,0,0,0,0,0,0])
deriv = np.array([0,0,0,0,0,0,0])

def camber(sample,RandOrInput): # returns:   polynomial for camber line,   x value of max camb,   max camb,   LE angle (rad),   TE angle (rad)
        # Random data: 0  input data: 1
    finalval = -1
    for k in range(len(x)):
        if x[k] != -1000: 
            x[k] = -1000
            y[k] = -1000

    if RandOrInput == 0:
        for i in range(1,101,1):
            x1,y1 = xyvalues(sample,i)
            _,y2 = xyvalues(sample,200-i)
            x_list.append(x)
            y_list.append((y1+y2)/2)

    elif RandOrInput == 1:
        _,_,A,_ = get_input_data()
        xy = A[sample][1:]
        for i in range(0,int((len(xy)-1)/2)+1):
            x1,y1 = xy[i]
            _,y2 = xy[len(xy)-i-1]
            x[i] = x1
            y[i] = (y1+y2)/2
            #x_list.append(x)
            #y_list.append((y1+y2)/2)     
            finalval = int((len(xy)-1)/2)
    else:
        return False

    #x = np.array(x_list)
    #y = np.array(y_list)
    z = np.polyfit(x[:finalval+1], y[:finalval+1], 7)
    eq = str(z[7]) + " + " + str(z[6]) + "*x + " + str(z[5]) + "*x^2 + " + str(z[4]) + "*x^3 + " + str(z[3]) + "*x^4 + " + str(z[2]) + "*x^5 + " + str(z[1]) + "*x^6 + " + str(z[0]) + "*x^7"
    eq = eq.replace("+ -", "- ")

    #for k in range(7):
    #    deriv[k] = z[k]*(7-k)
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