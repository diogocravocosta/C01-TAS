#program to extract certain parameters of an airfoil, as described in Chacteristics-list.md

from output_data_cleaner import get_output_airfoil_data
from input_data_cleaner import get_input_data

def random_thickness_to_chord(sample_num): #returns the thickness to chord from a certain airfoil IN THE LIST OF THE RANDOM ONES, sample_num is the sample number of the airfoil
    sample_num += 1 #because for some reason it is rigged
    samples, latent_parameters = get_output_airfoil_data(one_value= True, sample_num = sample_num) # gets the airfoil data and latent parameters (I dont really need latent parameters but we ball)
    thickness_to_chord = 0 #this parameter will store the t/c 
    thickness_pos = 0 #this will store the position of max thickness to chord
    for i in range(int(len(samples[0])/2)): #divided by 2 to make sure we do not analyse the same point twice
        thickness = abs(samples[0][i][1] - samples[0][-i-1][1]) #calculates the absolute value of the y coordinates of the difference
        if thickness > thickness_to_chord:
            thickness_to_chord = thickness #basically stores the highest difference, which is what we want
            thickness_pos = samples[0][i][0] #stores the location where it was found
    return thickness_to_chord, thickness_pos


def input_thickness_to_chord(sample_num): #returns the thickness to chord from a certain airfoil IN THE LIST OF THE RANDOM ONES, sample_num is the sample number of the airfoil

    #code from nabihah to extract the airfoil's characteristics
    airfoil_tags, airfoil_names, split_data = get_input_data() # gets the airfoil data and latent parameters (I dont really need latent parameters but we ball)
    airfoil_n = sample_num
    x_vals = []
    y_vals = []
    for coordinate_pair_i in range(0, len(split_data[airfoil_n])):
        x_vals.append(split_data[airfoil_n][coordinate_pair_i][0])
        y_vals.append(split_data[airfoil_n][coordinate_pair_i][1])
    x_vals.pop(0)
    y_vals.pop(0)


    thickness_to_chord = 0 #this parameter will store the t/c 
    thickness_pos = 0 #this will store the position of max thickness to chord
    for i in range(int(len(x_vals)/2)): #divided by 2 to make sure we do not analyse the same point twice
        thickness = abs(y_vals[i] - y_vals[-i-1]) #calculates the absolute value of the y coordinates of the difference
        if thickness > thickness_to_chord:
            thickness_to_chord = thickness #basically stores the highest difference, which is what we want
            thickness_pos = x_vals[i] #stores the location where it was found
    return thickness_to_chord, thickness_pos


#print(input_thickness_to_chord(4))
#print(get_output_airfoil_data(one_value= True, sample_num = 1)[0][0][1][0])
