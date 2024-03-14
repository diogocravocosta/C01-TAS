# Max camber
from output_data_cleaner import get_output_airfoil_data
def camber(sample_num):
    samples, latent_parameters = get_output_airfoil_data(one_value = True, sample_num = sample_num) #assigns the dataset to the samples variable
    return samples, latent_parameters
print(camber(5))
    


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