from regression import regression
import matplotlib.pyplot as plt
import numpy as np



def generate(x,y,Title, x_label, y_label):
    regress_linear = regression(x,y,1)
    regress_quadratic = regression(x,y,2)
    regress_cubic = regression(x,y,3)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(x,y, c="midnightblue", s = 3)
    x_array = np.linspace(x[0],x[-1], len(x)*2)
    y_array_linear = regress_linear[0] * x_array + regress_linear[1]
    y_array_quadratic = regress_quadratic[0] * x_array**2 + regress_quadratic[1] * x_array + regress_quadratic[2]
    y_array_cubic = regress_cubic[0] * x_array**3 + regress_cubic[1] * x_array**2 + regress_cubic[2]*x_array + regress_cubic[3]
    #ax.text(x[0], y[-1], 'Linear Regression: y = ' + str(round(regress_linear[0], 4)) + 'x + ' + str(round(regress_linear[1], 4)) + ' | R^2 = ' + str(round(regress_linear[2][0], 4)), color = "lime")
    #ax.text(x[0],y[-1]-1, 'Quadratic Regression: y = ' + str(round(regress_quadratic[0], 4)) +'x**2 +' + str(round(regress_quadratic[1], 4)) + 'x +' + str(round(regress_quadratic[2], 4)) +  ' | R^2 = ' + str(round(regress_quadratic[3], 4)) , fontsize = 10, color = 'red')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(Title)
    ax.plot(x_array, y_array_linear, label = "Linear $R^2$ ="+ str(round(regress_linear[2][0], 4)) + '| y = ' + str(round(regress_linear[0], 4)) + 'x + ' + str(round(regress_linear[1], 4)), linewidth = 3)
    ax.plot(x_array, y_array_quadratic, label = "Quadratic $R^2$ =" + str(round(regress_quadratic[3], 4)) + '| y = ' + str(round(regress_quadratic[0], 4)) +'$x**2$ +' + str(round(regress_quadratic[1], 4)) + 'x +' + str(round(regress_quadratic[2], 4)), linewidth = 3)
    ax.plot(x_array, y_array_cubic, label = "Cubic $R^2$ ="+ str(round(regress_cubic[4], 4)) + '| y = ' + str(round(regress_cubic[0], 4)) +'$x**3$ +'+ str(round(regress_cubic[1], 4)) +'$x**2$ +' + str(round(regress_cubic[2], 4)) + 'x +' + str(round(regress_cubic[3], 4)), linewidth = 3)
    ax.legend()
    plt.savefig("plot_images/"+Title +'.png')


#x = np.linspace(0,10, 10)
#y = x + x**3
#generate(x,y, "NOT Test Plot", "x", "y")
