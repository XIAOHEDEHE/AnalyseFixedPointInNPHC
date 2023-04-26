import os
import re
import numpy as np

name = os.listdir('output_fullyconnected')
for file_name in name:
    file = open('output_fullyconnected/'+file_name)
    file_context = file.readlines()
    file.close()
    file_context_num = np.array([])

    # a_num = [1,4,8,9,12,13,17,18,22,23,25,26,30,31,34,35,39,40,42,43,44,45,46,47]
    a_num = [1,5,9,10,14,15,18,19,20,21,22,23]
    # Process the data, deletet information in file except the result, and convert initial information to
    # numpy array data type. Then reshape the data.
    for i in range(len(file_context)):
        if file_context[i].startswith('('):
            file_context[i] = file_context[i].replace('(','')
            file_context[i] = file_context[i].replace(')','')
            file_context[i] = file_context[i].replace('\n','j')
            file_context[i] = file_context[i].replace(' ','')
            file_context[i] = file_context[i].replace(',-','+')
            file_context[i] = file_context[i].replace(',','+')
            
            file_context_num = np.append(file_context_num,file_context[i])
    file_context_num = file_context_num.reshape([-1,24])
    
    real_solution = np.array([])  
    for i in range(file_context_num.shape[0]):
        real_label = 1
        positive_label = 1
        for j in range(len(file_context_num[i])):
            if complex(file_context_num[i][j]).imag != 0:
                real_label = 0
                positive_label = 0
                break
            if j in a_num:
                continue
            elif complex(file_context_num[i][j]).real < 0 or complex(file_context_num[i][j]).real > 1:
                positive_label = 0
        if positive_label == 1:
            real_solution = np.append(real_solution,file_context_num[i])
    np.savetxt('output_FC_real/'+file_name,real_solution,fmt = '%s',delimiter=',')
    print(real_solution)
