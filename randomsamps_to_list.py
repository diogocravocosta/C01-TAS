def samples_to_list(path):# path like 'random_samples.txt'
    #lists for latent parameters and characteristics 
    latent_parameters_lists = [[],[],[],[],[],[],[],[]]
    characteristics_lists = [[],[],[],[],[],[]]

    #open the file

    with open('random_samples.txt', 'r') as file:
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
                characteristic_value = line.split(":")[1].strip()
                if not characteristic_value:
                    characteristic_value = next(file).strip()
                characteristics_lists[0].append(float(characteristic_value))
            # Check for other characteristics in the same way
    file.close()
    #Print/use lists as needed

    #print('Latent Parameters:')
    #for i, latent_list in enumerate(latent_parameters_lists):
    #    print(f"Latent PA")
    return latent_parameters_lists, characteristics_lists