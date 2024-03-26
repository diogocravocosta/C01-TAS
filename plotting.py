import numpy as np
import math
import matplotlib as plt
from input_data_cleaner import get_input_data
from output_data_cleaner import get_output_airfoil_data

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


def plotter(list_choice,n_latent): # n_latent is the index of the latent parameter to be extracted, 0 is example. list_choice is 0 if you want the latent of input data, 1 output, any other value if you want both
  extracted_input_elements = extract_nth_elements(input, n_latent)
  extracted_output_elements = extract_nth_elements(output,n_latent)
  list = []
  if list_choice == 0 :
       list=extracted_input_elements
       
  elif list_choice == 1 :
       list=extracted_output_elements
  else :
      list= extracted_input_elements + extracted_output_elements
  return list 

# NEED TO ADD THE FEATURES IN THIS FUNCTION ABOVE, SO THAT THE FUNCTION WILL PLOT, WORKING ON CURRENTLY :)
 






       



 
        

        


    


#to be updated
def plotting(list_1,list_2): 

    plt.scatter(list_1,list_2)

    #Label your plots 
    #plt.xlabel('') 
    #plt.ylabel('')

    plt.show()











