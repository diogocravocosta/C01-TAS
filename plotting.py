import numpy as np
import math
import matplotlib as plt
from input_data_cleaner import get_input_data

def extract_nth_elements(nested_list, n): # Extracts the nth element from each sub-list within the nested list and forms a new list with these elements.
    
   # Parameters:
   # - nested_list: List[List[any]], the outer list containing inner lists.
   # - n: int, the index of the element to extract from each inner list.

    # Returns:
    #  - List[any]: A new list composed of the nth element from each inner list.
    
    # Use list comprehension to extract the nth element from each sub-list,
    # including error handling for sub-lists that are too short
    return [sub_list[n] for sub_list in nested_list if len(sub_list) > n]



# ignore the a,b,c stuff (trying to access latent from inpnut data function)
a,b,c,nested_list = get_input_data()
n = 0  # Index of the latent parameter to be extracted, 0 is example
extracted_elements = extract_nth_elements(nested_list, n)
print(extracted_elements)  


#to be updated
def plotting(list_1,list_2): 

    plt.scatter(list_1,list_2)

    #Label your plots 
    #plt.xlabel('') 
    #plt.ylabel('')

    plt.show()











