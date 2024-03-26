from regression import regression
import matplotlib.pyplot as plt
import numpy as np



def generate(x,y,Title, x_label, y_label):
    regress_linear = regression(x,y,1)
    regress_quadratic = regression(x,y,2)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(x,y, c="midnightblue", s = 1)
    x_array = np.linspace(x[0],x[-1], len(x)*2)
    y_array_linear = regress_linear[0] * x_array + regress_linear[1]
    y_array_quadratic = regress_quadratic[0] * x_array**2 + regress_quadratic[1] * x_array + regress_quadratic[2]
    #ax.text(x[0], y[-1], 'Linear Regression: y = ' + str(round(regress_linear[0], 4)) + 'x + ' + str(round(regress_linear[1], 4)) + ' | R^2 = ' + str(round(regress_linear[2][0], 4)), color = "lime")
    #ax.text(x[0],y[-1]-1, 'Quadratic Regression: y = ' + str(round(regress_quadratic[0], 4)) +'x**2 +' + str(round(regress_quadratic[1], 4)) + 'x +' + str(round(regress_quadratic[2], 4)) +  ' | R^2 = ' + str(round(regress_quadratic[3], 4)) , fontsize = 10, color = 'red')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(Title)
    ax.plot(x_array, y_array_linear, label = "Linear $R^2$ ="+ str(round(regress_linear[2][0], 4)))
    ax.plot(x_array, y_array_quadratic, label = "Quadratic $R^2$ ="+ str(round(regress_quadratic[3], 4)))
    ax.legend()
    plt.savefig("plot_images/"+Title +'.png')


#x = [1,3,5,7,9,11,13,14]
#y = [45,56,76,13,125,49,87,1]
#generate(x,y, "Test Plot", "x", "y")