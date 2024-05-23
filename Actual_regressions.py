#code to run the regressions for all of the chatacteristic and latent parameters combinations and generate the plots
from randomsamps_to_list import samples_to_list, samples_to_list_symmetric
from plot_generator import generate
import csv
import numpy as np
from regression import regression

latent_parameters_lists, characteristics_lists = samples_to_list('InputRegressdata.txt')
latent_parameters_lists_symmetric, characteristics_lists_symmetric = samples_to_list_symmetric('InputRegressdata.txt')

r_csv_values=[]
for param in range(8):
    r_param_values = []
    for char in range(6):


        parlist = []
        charlist = []
        if char <= 1:
            parlist = latent_parameters_lists_symmetric[param]
            charlist = characteristics_lists_symmetric[char]
        else:
            parlist = latent_parameters_lists[param]
            charlist = characteristics_lists[char]

        parlist = np.array(parlist)
        charlist = np.array(charlist)
        parlist = (parlist - np.mean(parlist))/ np.std(parlist)
        charlist = (charlist - np.mean(charlist))/ np.std(charlist)
        generate(parlist , charlist,"Latent Parameter "+ str(param)+" and characteristic "+ str(char), "Latent Parameter "+ str(param), "Characteristic "+ str(char))
        r_vals = []
        
        ybar = np.mean(charlist)
        sstot = 0
        for i in range(len(charlist)):
            sstot += (charlist[i] - ybar)**2

        for i in range(3):
            r_vals.append(regression(parlist,charlist, i+1)[-1])
        nice_r = min(r_vals)

        really_nice_r = 1 - (nice_r / sstot)

        r_param_values.append(really_nice_r)
    r_csv_values.append(r_param_values)

#normalize r^2 (for some godforsaken reason)
lst = [[],[],[],[],[],[]]
def normalize(X):
    X_normalized = (X - np.mean(X)) / np.std(X)
    return X_normalized

for i in range(8):
    for c in range(6):
        lst[c].append(r_csv_values[i][c]) 
r_0 = list(np.array(lst[0]))
r_1 = list(np.array(lst[1]))
r_2 = list(np.array(lst[2]))
r_3 = list(np.array(lst[3]))
r_4 = list(np.array(lst[4]))
r_5 = list(np.array(lst[5]))

r_csv_values_mk2 = []

r_csv_values_mk2.append(r_0)
r_csv_values_mk2.append(r_1)
r_csv_values_mk2.append(r_2)
r_csv_values_mk2.append(r_3)
r_csv_values_mk2.append(r_4)
r_csv_values_mk2.append(r_5)

csv_file_path = 'r_values_outputs.csv'

with open(csv_file_path, mode='w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)
    # Write data to the CSV file
    writer.writerows(r_csv_values_mk2) #x is latent parameters, Y is characteristics












#   latent_parameters_lists, characteristics_lists = samples_to_list('Regressdata.txt')
#   
#   r_csv_values=[]
#   for param in range(8):
#       r_param_values = []
#       for char in range(6):
#           generate(latent_parameters_lists[param],characteristics_lists[char],"Latent Parameter "+ str(param)+" and characteristic "+ str(char), "Latent Parameter "+ str(param), "Characteristic "+ str(char))
#           r_vals = []
#           for i in range(3):
#               r_vals.append(regression(latent_parameters_lists[param],characteristics_lists[char], i+1)[-1])
#           nice_r = min(r_vals)
#           r_param_values.append(nice_r)
#       r_csv_values.append(r_param_values)
#   
#   csv_file_path = 'r_values_outputs.csv'
#   
#   with open(csv_file_path, mode='w', newline='') as file:
#       # Create a csv.writer object
#       writer = csv.writer(file)
#       # Write data to the CSV file
#       writer.writerows(r_csv_values) #x is latent parameters, Y is characteristics
#   
#   