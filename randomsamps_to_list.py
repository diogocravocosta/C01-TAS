def samples_to_list(path):
    # Initialize lists for latent parameters and characteristics 
    latent_parameters_lists = [[], [], [], [], [], [], [], []]
    characteristics_lists = [[], [], [], [], [], []]
    skip = 0
    # Open the file
    with open(path, 'r') as file:
        sample_count = -1
        for line in file:
            if skip >0:
                skip -= 1
                continue
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
                    if characteristic_value == -1:
                        skip = 11
                        continue
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
                
                characteristics_lists[char_index].append(float(characteristic_value))

    # Return the lists
    return latent_parameters_lists, characteristics_lists