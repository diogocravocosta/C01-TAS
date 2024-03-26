#import characteristics_determination as cd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
fig = plt.figure()
ax = fig.add_subplot()
def quadratic(x ,a, b, c):
    y = a*x**2 + b*x + c
    return y

def regression(x,y,degree):
    if degree in ['linear', "Linear", 'lineaire', 'LINEAR', 'John Cena', 1, 'one']:
        #Values = np.array([x,y])
        parameters = np.polyfit(x,y,1,full=True)
        response = []
        response.append(parameters[0][0])
        response.append(parameters[0][1])
        response.append(parameters[1]) #R is the pearson correlation coefficient which represents best fit if R^2 is close to one
    elif degree in ['Quadratic', 'quadratic', 2, 'two', 'second order']:
        Values = np.polyfit(x,y,2, full=True)
        Result = Values[0]
        Residuals = Values[1]
        response = []
        response.append(Result[0])
        response.append(Result[1])
        response.append(Result[2])
        response.append(Residuals[0])



    return response

#x = [1,2,3,4]
#y = [4,8,12,16]
#regress = regression(x,y,1)
#print(regress)
#ax.scatter(x,y)
#x_array = np.arange(x[0],x[-1], 0.0001)
#y_array = regress[0] * x_array**2 + regress[1] * x_array + regress[2]
#ax.text(x[0],y[-1], 'Regression: y = ' + str(round(regress[0], 4)) +'x**2 +' + str(round(regress[1], 4)) + 'x +' + str(round(regress[2], 4)) +  ' | R^2 = ' + str(round(regress[3], 4)) , fontsize = 10, color = 'red')
#y_array = regress[0] * x_array + regress[1]
#ax.text(x[0], y[-1], 'Regression: y = ' + str(round(regress[0], 4)) + 'x + ' + str(round(regress[1], 4)) + ' | R^2 = ' + str(round(regress[2][0], 4)))
#ax.plot(x_array, y_array, 'purple')

#plt.show()





        
        




#import characteristics_determination as cd
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot()
def quadratic(x ,a, b, c):
    y = a*x**2 + b*x + c
    return y

def regression(x,y,degree):
    if degree in ['linear', 'Linear', 'lineaire', 'LINEAR', 'John Cena', 1, 'one']:
        #Values = np.array([x,y])
        parameters = np.polyfit(x,y,1,full=True)
        response = []
        response.append(parameters[0][0])
        response.append(parameters[0][1])
        response.append(parameters[1]) #R is the pearson correlation coefficient which represents best fit if R^2 is close to one
    elif degree in ['Quadratic', 'quadratic', 2, 'two', 'second order']:
        Values = np.polyfit(x,y,2, full=True)
        Result = Values[0]
        Residuals = Values[1]
        response = []
        response.append(Result[0])
        response.append(Result[1])
        response.append(Result[2])
        response.append(Residuals[0])
    #elif degree in ['Cubic', 'cubic', 3, 'three']:
        #Value = np.polyfit(x,y,3, full = True)
        #Results = Value[0]
        #Residual = Value[1]
        #response = []
        #response.append(Results[0])
        #response.append(Results[1])
        #response.append(Results[2])
        #response.append(Results[3])
        #response.append(Residual[0])
        #print(Value)



    return response

x = [1,2,3,4]
y = [1,8,27,100]
regress = regression(x,y,3)
print(regress)
ax.scatter(x,y)
x_array = np.arange(x[0],x[-1], 0.0001)
y_array = regress[0] * x_array**3 + regress[1] * x_array**2 + regress[2] * x_array + regress[3]
#ax.text(x[0],y[-1], 'Regression: y = ' + str(round(regress[0], 4)) +'$x^3$ +' + str(round(regress[1], 4)) + '$x^2$ +' + str(round(regress[2], 4)) +  ' | R^2 = ' + str(round(regress[3], 4)) , fontsize = 10, color = 'red')
#y_array = regress[0] * x_array**2 + regress[1] * x_array + regress[2]
#ax.text(x[0],y[-1], 'Regression: y = ' + str(round(regress[0], 4)) +'x**2 +' + str(round(regress[1], 4)) + 'x +' + str(round(regress[2], 4)) +  ' | R^2 = ' + str(round(regress[3], 4)) , fontsize = 10, color = 'red')
#y_array = regress[0] * x_array + regress[1]
#ax.text(x[0], y[-1], 'Regression: y = ' + str(round(regress[0], 4)) + 'x + ' + str(round(regress[1], 4)) + ' | R^2 = ' + str(round(regress[2][0], 4)))
ax.plot(x_array, y_array, 'purple')

plt.show()





        
        



