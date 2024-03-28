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

    #  lists to store values
    x_maxcamb = []
    maxcamb = []
    le_angle = []
    te_angle = []

    # Loop over each item in latent list
    for i in range(len(latent_list)):
        # Call camber with i and list_choice being either 0 or 1
        camber_values = camber(i, list_choice)

        #append each value to the list
        x_maxcamb.append(camber_values[1])
        maxcamb.append(camber_values[2])
        le_angle.append(camber_values[3])
        te_angle.append(camber_values[4])

    return x_maxcamb, maxcamb, le_angle, te_angle

print(camber(5,0))

'''
def camberlistmaker(feature,list_choice): #LIST CHOICE 1 MEANS INPUT, 0 MEANS OUTPUT/RANDOM DATA
   list_feature=[]
   if list_choice==1:
      for i in range (0,len(latentlistmaker(1,1))):
         for j in range (1,5):
            list_feature.append(camber((i,1)[j]))
   else: 
      for i in range (0,len(latentlistmaker(0,1))):
         for j in range (1,5):
            list_feature.append(camber((i,0)[j]))
   
   x_maxcamb = list_feature[0::4]
   maxcamb = list_feature[1::4]
   le_angle = list_feature[2::4]
   te_angle = list_feature[3::4]
   return x_maxcamb, maxcamb, le_angle, te_angle

'''


   
                                







#def plotter(list_choice,n_latent,feature): # n_latent is the index of the latent parameter to be extracted, 0 is example. list_choice is 0 if you want the latent of input data, 1 output, any other value if you want both
#  extracted_input_elements = extract_nth_elements(input, n_latent)
#  extracted_output_elements = extract_nth_elements(output,n_latent)
  
#  camber_features =[]
  #if list_choice == 0 :
 #   list=extracted_input_elements
 #   for i in range (0,len(list)):
 #      for j in range (1,5):
 #           camber_features.append(camber((i,1)[j])
       
#  elif list_choice == 1 :
#    list = extracted_output_elements
#       for i in range (0,len(list)):
 #        for j in range (1,5):
 #           camber_features.append(camber((i,0)[j])
  #else :
  #    list= extracted_input_elements + extracted_output_elements
  #    for i in range (0,len(extracted_input_elements)):
  #       for j in range (1,5):
  #          camber_features.append(camber((i,1)[j])
 #     for k in range (0, len(extracted_output_elements)):
 #        for l in range (1,5):
 #          camber_features.append(camber(k,0)[l])
 #return camber_features

#x_maxcamb = camber_features[0::4]
#maxcamb = camber_features[1::4]
#le_angle = camber_features[2::4]
#te_angle = camber_features[3::4] 
  
 # plt.scatter(list,feature)
   



# NEED TO ADD THE FEATURES IN THIS FUNCTION ABOVE, SO THAT THE FUNCTION WILL PLOT, WORKING ON CURRENTLY :)





  


    

#plt.scatter(list_1,list_2)

    #Label your plots 
    #plt.xlabel('') 
    #plt.ylabel('')

 #   plt.show()


       



 
        

        


    




    











