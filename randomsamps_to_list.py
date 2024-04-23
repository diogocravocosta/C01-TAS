def samples_to_list(path):
    # Initialize lists for latent parameters and characteristics 
    latent_parameters_lists = [[], [], [], [], [], [], [], []]
    characteristics_lists = [[], [], [], [], [], []]
    #skip = 0
    # Open the file
    with open(path, 'r') as file:
        sample_count = -1
        for line in file:
            #skip = True
            line = line.strip()
            if line.startswith(('maxcamb_position', 'maxcamb', 'LE_angle', 'TE_angle', 'thickness_to_chord', 'max_thickness_position')):
                characteristic_name, characteristic_value = line.split(":")
                characteristic_value = characteristic_value.strip()
                if not characteristic_value:
                    characteristic_value = next(file).strip()
                # Determine the index of the characteristic within characteristics_lists
                if characteristic_name == 'maxcamb_position':
                    char_index = 0
                    #if float(characteristic_value) > -1.01 and float(characteristic_value) < -0.99 and char_val == 0:
                        #skip = True
                        #continue
                elif characteristic_name == 'maxcamb': #and char_val == 1:
                    #if float(characteristic_value) > -1.01 and float(characteristic_value) < -0.99:
                        #characteristic_value = 0
                    char_index = 1
                elif characteristic_name == 'LE_angle': # and char_val == 2:
                    char_index = 2
                elif characteristic_name == 'TE_angle': #and char_val == 3:
                    char_index = 3
                elif characteristic_name == 'thickness_to_chord': #and char_val == 4:
                    char_index = 4
                elif characteristic_name == 'max_thickness_position': #and char_val == 5:
                    char_index = 5
                characteristics_lists[char_index].append(float(characteristic_value))
            elif line.startswith('Sample'):
                sample_count += 1
            elif line.startswith('latent parameters:'): # and skip == False:
                for i in range(8):
                    latent_param = float(next(file).strip())
                    latent_parameters_lists[i].append(latent_param)

    # Return the lists
    return latent_parameters_lists, characteristics_lists



def samples_to_list_symmetric(path):
    # Initialize lists for latent parameters and characteristics 
    latent_parameters_lists = [[], [], [], [], [], [], [], []]
    characteristics_lists = [[], [], [], [], [], []]

    # Open the file
    with open(path, 'r') as file:
        sample_count = -1
        for line in file:
            line = line.strip()
            if line.startswith('Sample'):
                sample_count += 1
            elif line.startswith('latent parameters:'):
                for i in range(8):
                    latent_param = float(next(file).strip())
                    latent_parameters_lists[i].append(latent_param)
            elif line.startswith(('maxcamb_position', 'maxcamb', 'LE_angle', 'TE_angle', 'thickness_to_chord', 'max_thickness_position')):
                characteristic_name, characteristic_value = line.split(":")
                characteristic_value = characteristic_value.strip()
                if not characteristic_value:
                    characteristic_value = next(file).strip()
                # Determine the index of the characteristic within characteristics_lists
                if characteristic_name == 'maxcamb_position':
                    char_index = 0
                elif characteristic_name == 'maxcamb':
                    char_index = 1
                elif characteristic_name == 'LE_angle':
                    char_index = 2
                elif characteristic_name == 'TE_angle':
                    char_index = 3
                elif characteristic_name == 'thickness_to_chord':
                    char_index = 4
                elif characteristic_name == 'max_thickness_position':
                    char_index = 5

                if char_index == 0 and float(characteristic_value) < -1.01 or float(characteristic_value) > -0.99:
                    characteristics_lists[char_index].append(float(characteristic_value))

                elif char_index == 1:
                    if float(characteristic_value) < -1.01 or float(characteristic_value) > -0.99:
                        characteristics_lists[char_index].append(float(characteristic_value))
                    else:
                        for i in range(8):
                            latent_parameters_lists[i].pop                      
                
                #characteristics_lists[1][char_index].append(float(characteristic_value))

                #if char_index == 1 and characteristic_value == -1:
                #    characteristics_lists[0].pop
                #    characteristics_lists[1].pop
                #    for i in range(8):
                #        latent_parameters_lists[i].pop

    # Return the lists
    return latent_parameters_lists, characteristics_lists