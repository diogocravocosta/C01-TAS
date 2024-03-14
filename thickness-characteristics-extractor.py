#program to extract certain parameters of an airfoil, as described in Chacteristics-list.md

from output_data_cleaner import get_airfoil_data

def random_thickness_to_chord(sample_num): #returns the thickness to chord from a certain airfoil IN THE LIST OF THE RANDOM ONES, sample_num is the sample number of the airfoil
    samples, latent_parameters = get_airfoil_data(one_value= True, sample_num = sample_num) # gets the airfoil data and latent parameters (I dont really need latent parameters but we ball)
    thickness_to_chord = 0 #this parameter will store the t/c 
    thickness_pos = 0 #this will store the position of max thickness to chord
    for i in range(samples):
        thickness = abs(samples[i,1] - samples[-i,1]) #calculates the absolute value of the y coordinates of the difference
        if thickness > thickness_to_chord:
            thickness_to_chord = thickness #basically stores the highest difference, which is what we want
            thickness_pos = samples[i,0] #stores the location where it was found
    return thickness_to_chord, thickness_pos


