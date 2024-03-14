import matplotlib.pyplot as plt
import random
from output_data_cleaner import get_output_airfoil_data

sample_n = random.randint(0,9999) # chooses a random airfoil sample to look at
# sample_n = 0  # uncomment and enter specific sample number you wanna look at

x_vals = []
y_vals = []


samples, latent_parameters = get_output_airfoil_data(True, sample_n)

for coordinate_pair_i in range(0, len(samples[1])):
    x_vals.append(samples[1][coordinate_pair_i][0])
    y_vals.append(samples[1][coordinate_pair_i][1])

print(samples[0])


# yes i randomize the color of each airfoil that is plotted.
# yes that is unnecessary
# i don't care, it's pretty
colors = ['b','g','r','c','m','y','pink','purple','orange','maroon']


plt.figure(figsize=(15,4))
plt.plot(x_vals, y_vals, '-o', color=random.choice(colors), markersize=4)

plt.title("Airfoil Sample " + str(sample_n))
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='black')

plt.show()