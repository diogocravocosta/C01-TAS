#import characteristics_determination as cd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
def regression(x,y,degree):
    if degree in ['linear', "Linear", 'lineaire', 'LINEAR', 'John Cena', 1, 'one']:
        #Values = np.array([x,y])
        parameters = sp.stats.linregress(x,y)
        response = []
        response.append(parameters[0])
        response.append(parameters[1])
        response.append(parameters[2]) #R is the pearson correlation coefficient which represents best fit if R^2 is close to one
    return response
x = [1,2,3,4]
y = [2,4,6,8]
regress = regression(x,y,1)
print(regress)




        
        



