import os
import re
import numpy as np
import detect_positive

result_matrix = np.ones((20,20))
folder = 'output_fullyconnected'

name = os.listdir(folder)
for filename in name:
    pattern = "\d+"
    matches = re.findall(pattern, filename)
    match = int(matches[0])
    col = match//20
    raw = match%20
    real_solution_num = detect_positive.return_real(folder+'/{}'.format(filename))
    result_matrix[col,raw] = real_solution_num

np.savetxt("real_FC.txt", result_matrix, fmt = '%d', delimiter = ',')