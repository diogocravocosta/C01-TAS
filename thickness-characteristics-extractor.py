#program to extract certain parameters of an airfoil, as described in Chacteristics-list.md

from output_data_cleaner import get_airfoil_data

def thickness_to_chord(sample_num): #returns the thickness to chord from a certain airfoil, sample_num is the sample number of the airfoil
    samples, latent_parameters = get_airfoil_data(one_value= True, sample_num = 1)
    return samples, latent_parameters
