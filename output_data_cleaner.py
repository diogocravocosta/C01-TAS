
# THIS FILE DOESN'T REALLY NEED ANY EDITING SO BE CAREFUL WHEN YOU TOUCH STUFF THANKS ;)

# could all of this have been done in way less lines of code? maybe. but don't be mean to me i tried my best

def get_output_airfoil_data(one_value, sample_num): # the one_value thing is just so we can use this function either to print out ALL the samples vs. if we want to get it for just one sample (i.e. while plotting)

   # reading data file
   with open('datasets/Random_samples.dat', 'r') as file:
      data = file.readlines()

   samples = []
   latent_parameters = []

   # separating samples & latent parameters

   if one_value == True:
      for i in range(sample_num, sample_num+2): #don't touch this
         prev_n = ((i - 1) * 201) + 1
         n = (i * 201) - 1
         samples.append(data[prev_n:n])
         latent_parameters.append(data[((i - 1) * 201)])
   else:
      for i in range(0,10001):  # change the 0 to get a different starting sample, change the 10001 to get a different ending sample (required ending number + 2)
         prev_n = ((i - 1) * 201) + 1
         n = (i * 201) - 1
         samples.append(data[prev_n:n])
         latent_parameters.append(data[((i - 1) * 201)])

   # cleaning up latent parameters.
   # the latent parameters are now of the following format:
   # [[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
   # here each number (1,2,...,8) is a latent parameter
   # each list of numbers ([(1,2,...,8)]) is a list of the latent parameters for a sample
   # FOR EXAMPLE to get the latent parameters of sample 0 get latent_parameters[0]
   # FOR EXAMPLE to get the second latent parameter of sample 0 get latent_parameters[0][1]

   for j in range(0, len(latent_parameters)):
      latent_parameters[j] = latent_parameters[j].strip('\n').split(' ')

      # get rid of empty ''
      latent_parameters[j] = list(filter(None, latent_parameters[j]))

      # get rid of items that are just brackets
      latent_parameters[j] = [x for x in latent_parameters[j] if x != '[']
      latent_parameters[j] = [x for x in latent_parameters[j] if x != ']']

      # get rid of brackets INSIDE of strings (hugging the numbers)
      for m in range(0, len(latent_parameters[j])):
         if latent_parameters[j][m].startswith('['):
            latent_parameters[j][m] = latent_parameters[j][m][1:]
         if latent_parameters[j][m].startswith('[['):
            latent_parameters[j][m] = latent_parameters[j][m][2:]
         if latent_parameters[j][m].endswith(']'):
            latent_parameters[j][m] = latent_parameters[j][m][:-1]
         if latent_parameters[j][m].endswith(']]'):
            latent_parameters[j][m] = latent_parameters[j][m][:-2]

         # convert every number to an actual number and not just a string
         latent_parameters[j][m] = float(latent_parameters[j][m])

   # cleaning up the coordinates data for each of the samples
   cleaned_samples = []
   for sample in samples:
      clean_sample = []
      for s in sample:
         cleaned_string = s.replace('[', '').replace(']', '').replace('\n', '').strip()
         # converting all to a float :)
         num_list = list(map(float, cleaned_string.split()))
         clean_sample.append(num_list)
      cleaned_samples.append(clean_sample)

   samples = cleaned_samples

   return samples, latent_parameters




# uncomment the following to get a printout of the samples / latent parameters


<<<<<<< Updated upstream
# samples, latent_parameters = get_output_airfoil_data(True, 0) # keep this as False, doesn't matter what the number is so just keep 0
#
# print(latent_parameters[1]) # just add the [1] at the end ok trust me
=======
# samples, latent_parameters = get_output_airfoil_data(False, 0) # keep this as False, doesn't matter what the number is so just keep 0
#
# print(samples)
>>>>>>> Stashed changes

# print(samples)
# print(latent_parameters)



