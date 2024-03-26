from output_data_cleaner import get_output_airfoil_data

_, unsorted_lps = get_output_airfoil_data(False, 0)

# print(unsorted_lps)

lps = [[]]*8

for sample_i in range(0, len(unsorted_lps)):
    for param in range(0, len(lps)):
        lps[param].append(unsorted_lps[sample_i][param])

