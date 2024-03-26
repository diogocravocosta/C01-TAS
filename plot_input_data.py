import matplotlib.pyplot as plt
import random
from input_data_cleaner import get_input_data

x_vals = []
y_vals = []


airfoil_tags, airfoil_names, split_data, latent_parameters = get_input_data()

airfoil_n = random.randint(0,1618)

# uncomment the following line and enter in any airfoil's tag if you're looking for a specific one
# airfoil_n = airfoil_tags.index('ea81006')

# this for loop just rewrites the split_data coordinates and makes it into an x and y list instead of just 1 super long list
for coordinate_pair_i in range(0, len(split_data[airfoil_n])):
    x_vals.append(split_data[airfoil_n][coordinate_pair_i][0])
    y_vals.append(split_data[airfoil_n][coordinate_pair_i][1])

# i'm not sure why, but from the above code the first x and y coordinate values are always some completely irrelevant random numbers
# that aren't even a part of the original coordinates. so i just use .pop(0) to get rid of that first element from both lists since idk how to prevent it
# being there in the first place
x_vals.pop(0)
y_vals.pop(0)

# yes i randomize the color of each airfoil that is plotted.
# yes that is unnecessary
# i don't care, it's pretty
colors = ['b','g','r','c','m','y','pink','purple','orange','maroon']

plt.figure(figsize=(15,4))
plt.plot(x_vals, y_vals, '-o', color=random.choice(colors), markersize=4)


plt.title(airfoil_tags[airfoil_n] + ', ' + airfoil_names[airfoil_n])
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='black')

print(x_vals)
print('===========================================================================')
print(y_vals)

plt.show()