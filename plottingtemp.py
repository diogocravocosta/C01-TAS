import numpy as np
import math
import matplotlib as plt
from input_data_cleaner import get_input_data
from output_data_cleaner import get_output_airfoil_data
from camber import camber
def extract_nth_elements(nested_list, n): # Extracts the nth element from each sub-list within the nested list and forms a new list with these elements.
    
   # Parameters:
   # - nested_list: List[List[any]], the outer list containing inner lists.
   # - n: int, the index of the element to extract from each inner list.

    # Returns:
    #  - List[any]: A new list composed of the nth element from each inner list.
    
    # Use list comprehension to extract the nth element from each sub-list,
    # including error handling for sub-lists that are too short (shoudn't be a problem)
    return [sub_list[n] for sub_list in nested_list if len(sub_list) > n]



# ignore the a,b,c stuff (trying to access latent from inpnut data function)
a,b,c,input = get_input_data()
a,output = get_output_airfoil_data(False, 0)

#this under is for camber features lists

def latentlistmaker(list_choice,n_latent):
   if list_choice ==1:
      listfinal= extract_nth_elements(input, n_latent)  
   else:
      listfinal=extract_nth_elements(output,n_latent)
   return listfinal


def camberlistmaker(list_choice):
    latent_list = latentlistmaker(list_choice, 1)

    # Initialize lists to store the extracted values
    x_maxcamb = []
    maxcamb = []
    le_angle = []
    te_angle = []

    # Loop over each item in your latent list
    for i in range(len(latent_list)):
        # Call camber with i and list_choice, assuming these are the correct parameters
        camber_values = camber(i, list_choice)

        # Now, append each value to the appropriate list
        x_maxcamb.append(camber_values[0])
        maxcamb.append(camber_values[1])
        le_angle.append(camber_values[2])
        te_angle.append(camber_values[3])
    print(x_maxcamb)
    return x_maxcamb, maxcamb, le_angle, te_angle
     
camberlistmaker(1)



