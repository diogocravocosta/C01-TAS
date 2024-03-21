#determines characteristics of airfoil samples
from input_data_cleaner import get_input_data
import thickness-characteristics-extractor as tc
import numpy as np
airfoil_tags, airfoil_names, split_data = get_input_data() #retrieves input airfoil tag, name and its coordinates & latent parameters
def t_c_list_input():
    airfoil_tags, airfoil_names, split_data = get_input_data() #retrieves input airfoil tag, name and its coordinates & latent parameters
    t_c_list = []
    for i in range(0,len(split_data)):
        t_c = tc.input_thickness_to_chord(i)[0]
        t_c_list.append(t_c)
    return t_c_list
def t_c_list_random():
    samples, latent_parameters = get_output_airfoil_data() #retrieves input airfoil tag, name and its coordinates & latent parameters
    t_c_output_list = []
    for i in range(0,len(samples)):
        output_t_c = tc.random_thickness_to_chord(i)[0]
        t_c_output_list.append(output_t_c)
    return t_c_output_list
def t_c_position_input():
    airfoil_tags, airfoil_names, split_data = get_input_data()
    x_list = [] 
    for i in range(0,len(split_data)):
        x = tc.input_thickness_to_chord(i)[1]
        x_list.append(x)
    return x_list
def t_c_position_random():
    samples, latent_parameters = get_output_airfoil_data() #retrieves input airfoil tag, name and its coordinates & latent parameters
    x_output_list = []
    for i in range(0,len(samples)):
        x_output = tc.random_thickness_to_chord(i)[1]
        X_output_list.append(x_output)
    return x_output_list









        




