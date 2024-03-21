import characteristics_determination as cd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
def regression(x,y,degree):
    if degree in ['linear', "Linear", 'lineaire', 'LINEAR', 'John Cena']:
        #Values = np.array([x,y])
        parameters = sp.stats.linregress(x,y)
        
        



