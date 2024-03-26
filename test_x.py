import numpy as np
from output_data_cleaner import get_output_airfoil_data

_, unsorted_lps = get_output_airfoil_data(False, 0)

# lps = [[]]*8
#
# for sample_i in range(0, len(unsorted_lps)):
#     for param in range(0, len(lps)):
#         lps[param].append(unsorted_lps[sample_i][param])

def n_parameters_list (n1, n2): # n1 is the first latent parameter you wanna look at, n2 is the second one you wanna compare
    return [[data_point[n1], data_point[n2]] for data_point in unsorted_lps][1:]

n_parameters_list = X = np.array(n_parameters_list(1, 2))

print(X)
