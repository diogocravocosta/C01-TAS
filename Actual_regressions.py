#code to run the regressions for all of the chatacteristic and latent parameters combinations and generate the plots
from randomsamps_to_list import samples_to_list
from plot_generator import generate


latent_parameters_lists, characteristics_lists = samples_to_list('Regressdata.txt')
for param in range(8):
    for char in range(6): 
        generate(latent_parameters_lists[param],characteristics_lists[char],"Latent Parameter "+ str(param)+" and characteristic "+ str(char), "Latent Parameter "+ str(param), "Characteristic "+ str(char))

