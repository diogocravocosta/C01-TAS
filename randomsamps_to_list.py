def samples_to_list(path):# path like 'random_samples.txt'
    #lists for latent parameters and characteristics 
    latent_parameters_lists = [[],[],[],[],[],[],[],[]]
    characteristics_lists = [[],[],[],[],[],[]]

    #open the file

    with open(path, "r") as file:
        sample_count = -1
        for line in file:
            line = line.strip()
            if line.startswith('Sample'):
                #Start of a new Sample
                sample_count += 1 
            elif line.startswith('latent parameters:'):
                for i in range(8):
                    latent_param = float(next(file).strip())
                    latent_parameters_lists[i].append(latent_param)
            elif line.startswith('maxcamb_position'):
                characteristics_lists[0].append(float(line.split(":")[1].strip()))
            elif line.startswith('maxcamb'):
                characteristics_lists[1].append(float(line.split(":")[1].strip()))
            elif line.startswith('LE_angle'):
                characteristics_lists[2].append(float(line.split(":")[1].strip()))
            elif line.startswith('TE_angle'):
                characteristics_lists[3].append(float(line.split(":")[1].strip()))
            elif line.startswith('thickness_to_chord'):
                characteristics_lists[4].append(float(line.split(":")[1].strip()))
            elif line.startswith('max_thickness_position'):
                characteristics_lists[5].append(float(line.split(":")[1].strip()))
    file.close()
    #Print/use lists as needed

    #print('Latent Parameters:')
    #for i, latent_list in enumerate(latent_parameters_lists):
    #    print(f"Latent PA")
    return latent_parameters_lists, characteristics_lists