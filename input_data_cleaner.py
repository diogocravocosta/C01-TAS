



def get_input_data():
    with open('datasets/Airfoil_LatentRepresentation_Coor.dat', 'r') as file:
        data = file.readlines()

    split_data = []
    temp_list = []
    for i in range(0,len(data)):
        line = data[i].strip()
        if '###' in line:
            temp_list.append(line)
            split_data.append(temp_list)
            temp_list = []
        else:
            temp_list.append(line)
    split_data.append(temp_list)

    split_data = list(filter(None, split_data))

    airfoil_tags = []
    airfoil_names = []
    latent_parameters = []

    for i in range(0, len(split_data)):

        airfoil_data = split_data[i] # just so i can reference each item in split_data (i.e. split_data[i]) as airfoil_data so i don't forget what it means in the end.
        # airfoil_data is the data of one (currently being looked at in the for loop) airfoil.

        # getting the names and tags of the airfoils in different lists
        airfoil_tags.append(airfoil_data[0])
        airfoil_names.append(airfoil_data[1])


        # getting rid of the names and tags of the airfoils from the coordinates list
        airfoil_data = airfoil_data[2:]

        if len(airfoil_data) >= 1:
            airfoil_data.pop()

        for j in range(0, len(airfoil_data)):

            if j == 0:
                airfoil_data[j] = airfoil_data[j].replace('[', '').replace(']', '').replace('\n', '').strip().split('\t')
                airfoil_data[j] = list(filter(None, airfoil_data[j]))
                airfoil_data[j] = list(map(float, airfoil_data[j]))
                latent_parameters.append(airfoil_data[j])

            else:

                airfoil_data[j] = list(filter(None, airfoil_data[j].replace('[', '').replace(']', '').replace('\n','').strip().split(' ')))
                airfoil_data[j] = list(map(float, airfoil_data[j]))

        split_data[i] = airfoil_data # i just did this so i could write split_data[i] more intuitively as airfoil_data so my brain would understand what's going on, see first comment in this main for loop


    return airfoil_tags, airfoil_names, split_data, latent_parameters

# airfoil_tags, airfoil_names, split_data, latent_parameters = get_input_data()
#
# print(len(airfoil_names))