import os
import re
import numpy as np
import detect_positive

result_matrix = np.ones((20,20))*(-1)
folder = 'output_fullyconnected'

name = os.listdir(folder)
for filename in name:
    pattern = "\d+"
    matches = re.findall(pattern, filename)
    match = int(matches[0])
    # print(filename)
    col = match//20
    raw = match%20
    real_solution_num = detect_positive.returen_result_FC(folder+'/{}'.format(filename))
    result_matrix[col,raw] = real_solution_num
    print(result_matrix)

np.savetxt("positive_real_FC.txt", result_matrix, fmt = '%d', delimiter = ',')