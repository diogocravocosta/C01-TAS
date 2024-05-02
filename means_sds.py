from new_data_cleaner import get_new_airfoil_data
import matplotlib.pyplot as plt
import random

samples, latent_parameters = get_new_airfoil_data()

samples = samples[1:]
latent_parameters = latent_parameters[1:]

# print(latent_parameters)

lp_means = [-1.33056071,-0.0250866,0.18143471,0.51776701,0.53480923,-0.02748315,-0.00849687,0.11793799]

lp_1 = [item[0] for item in latent_parameters][:100]
lp_2 = [item[1] for item in latent_parameters]
lp_2 = [item for item in lp_2 if item != lp_means[1]]
lp_3 = [item[2] for item in latent_parameters]
lp_3 = [item for item in lp_2 if item != lp_means[2]]
lp_4 = [item[3] for item in latent_parameters]
lp_4 = [item for item in lp_2 if item != lp_means[3]]
lp_5 = [item[4] for item in latent_parameters]
lp_5 = [item for item in lp_2 if item != lp_means[4]]
lp_6 = [item[5] for item in latent_parameters]
lp_6 = [item for item in lp_2 if item != lp_means[5]]
lp_7 = [item[6] for item in latent_parameters]
lp_7 = [item for item in lp_2 if item != lp_means[6]]
lp_8 = [item[7] for item in latent_parameters]
lp_8 = [item for item in lp_2 if item != lp_means[7]]

# print(lp_2)

plot_samples = [[],[],[],[],[],[],[],[]]

for i in range(0,8):
    if i == 0:
        plot_samples[i].append(samples[0])
        plot_samples[i].append(samples[50])
        plot_samples[i].append(samples[99])
    if i == 1:
        plot_samples[i].append(samples[100])
        plot_samples[i].append(samples[150])
        plot_samples[i].append(samples[199])
    if i == 2:
        plot_samples[i].append(samples[200])
        plot_samples[i].append(samples[250])
        plot_samples[i].append(samples[299])
    if i == 3:
        plot_samples[i].append(samples[300])
        plot_samples[i].append(samples[350])
        plot_samples[i].append(samples[399])
    if i == 4:
        plot_samples[i].append(samples[400])
        plot_samples[i].append(samples[450])
        plot_samples[i].append(samples[499])
    if i == 5:
        plot_samples[i].append(samples[500])
        plot_samples[i].append(samples[550])
        plot_samples[i].append(samples[599])
    if i == 6:
        plot_samples[i].append(samples[600])
        plot_samples[i].append(samples[650])
        plot_samples[i].append(samples[699])
    if i == 7:
        plot_samples[i].append(samples[700])
        plot_samples[i].append(samples[750])
        plot_samples[i].append(samples[799])

print(plot_samples[0][2])

# the 0 means the 1st latent parameter, the 2 means the highest value
# if you were to do [0][0] you would get the lowest value (i.e. mean) of latent parameter 1

check_lp = 7     # this is one lESS than the latent parameter than youre trynna get

x_vals_0 = []
y_vals_0 = []

x_vals_1 = []
y_vals_1 = []

x_vals_2 = []
y_vals_2 = []

for coordinate_pair_i in range(0, len(plot_samples[check_lp][0])):
    x = plot_samples[check_lp][0][coordinate_pair_i][0]
    y = plot_samples[check_lp][0][coordinate_pair_i][1]
    x_vals_0.append(x)
    y_vals_0.append(y)

for coordinate_pair_i in range(0, len(plot_samples[0][1])):
    x = plot_samples[check_lp][1][coordinate_pair_i][0]
    y = plot_samples[check_lp][1][coordinate_pair_i][1]
    x_vals_1.append(x)
    y_vals_1.append(y)

for coordinate_pair_i in range(0, len(plot_samples[0][2])):
    x = plot_samples[check_lp][2][coordinate_pair_i][0]
    y = plot_samples[check_lp][2][coordinate_pair_i][1]
    x_vals_2.append(x)
    y_vals_2.append(y)



plt.plot(x_vals_0, y_vals_0, '-o', color='red', markersize=4, label='mean')
# plt.plot(x_vals_1, y_vals_1, '-o', color='blue', markersize=4, label='middle')
plt.plot(x_vals_2, y_vals_2, '-o', color='green', markersize=4, label='max')

ax = plt.gca()
ax.set_aspect('equal', adjustable='box')

plt.legend()

plt.grid()
plt.show()