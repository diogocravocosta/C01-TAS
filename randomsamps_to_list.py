#lists for latent parameters and characteristics 
latent_parameters_lists = [[],[],[],[],[],[],[],[]]
characteristics_lists = [[],[],[],[],[],[]]

#open the file

with open('random_samples.txt', "r") as file:
    sample_count = -1
    for line in file:
        line = line.strip()
        if line.startswith('Sample'):
            #Start of a new Sample
            sample_count += 1 