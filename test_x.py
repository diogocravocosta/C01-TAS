import numpy as np
from output_data_cleaner import get_output_airfoil_data
import matplotlib.pyplot as plt


xy_coordinates, _ = get_output_airfoil_data(False, 0)

y_coordinates = []

for i in range(0, len(xy_coordinates)):
    y_coordinates.append([])
    for j in range(0, len(xy_coordinates[i])):
        y_coordinates[i].append(xy_coordinates[i][j][1])

