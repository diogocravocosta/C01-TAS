from randomsamps_to_list import samples_to_list
from plot_generator import generate


latent_parameters_lists, characteristics_lists = samples_to_list('Regressdata.txt')

generate(latent_parameters_lists[0],characteristics_lists,"First Latent Parameter and Max Camber Position Relation", "Latent Parameter", "$\frac{x}{c}$")
