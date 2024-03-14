# Max camber
from output_data_cleaner import get_airfoil_data
#def max_camber():
    #for j in range(len(data)):
        #if abs(data[j][1]/2) >= maximum:
            #maximum = data[j][1]
    #return maximum

# Location of max camber
#def x_max():
    #maximum = 0
    #max_index = 0
    #for j in range(len(data)):
        #if data[j][1] >= maximum:
            #maximum = data[j][1]
            #max_index = j
    #return data[max_index][0]

def camber():
    samples, latent parameters = get_airfoil_data(one_value = True, sample_num = 5) #assigns the dataset to the samples variable
    


    