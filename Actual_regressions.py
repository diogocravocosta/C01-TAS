#code to run the regressions for all of the chatacteristic and latent parameters combinations and generate the plots
from randomsamps_to_list import samples_to_list, samples_to_list_symmetric
from plot_generator import generate
import csv
from regression import regression
latent_parameters_lists, characteristics_lists = samples_to_list('Regressdata.txt')
latent_parameters_lists_symmetric, characteristics_lists_symmetric = samples_to_list_symmetric('Regressdata.txt')

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

        generate(parlist , charlist,"Latent Parameter "+ str(param)+" and characteristic "+ str(char), "Latent Parameter "+ str(param), "Characteristic "+ str(char))
        r_vals = []
        for i in range(3):
            r_vals.append(regression(latent_parameters_lists[param],characteristics_lists[char], i+1)[-1])
        nice_r = min(r_vals)
        r_param_values.append(nice_r)
    r_csv_values.append(r_param_values)

csv_file_path = 'r_values_outputs.csv'

with open(csv_file_path, mode='w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)
    # Write data to the CSV file
    writer.writerows(r_csv_values) #x is latent parameters, Y is characteristics












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