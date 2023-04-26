import re
import numpy as np


def print_reslut(file_name):
    
    file = open(file_name)
    file_context = file.readlines()
    file.close()
    file_context_num = np.array([])
    
    real_solve = 0
    positive_real_solve = 0
    a_num = [1,4,8,9,12,13,17,18,22,23,25,26,30,31,34,35,39,40,42,43,44,45,46,47]
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
    file_context_num = file_context_num.reshape([-1,48])
    solve = file_context_num.shape[0]

    for i in range(file_context_num.shape[0]):
        real_label = 1
        positive_label = 1
        for j in range(len(file_context_num[i])):
            # print(file_context_num[i][j])
            if complex(file_context_num[i][j]).imag != 0:
                real_label = 0
                positive_label = 0
                break
            if j in a_num:
                continue
            elif complex(file_context_num[i][j]).real < 0 or complex(file_context_num[i][j]).real > 1:
                positive_label = 0
        if real_label == 1:
            real_solve = real_solve + 1
        if positive_label == 1:
            positive_real_solve = positive_real_solve + 1
    print('Positive real solve : {}'.format(positive_real_solve))

def returen_result(file_name):
    
    file = open(file_name)
    file_context = file.readlines()
    file.close()
    file_context_num = np.array([])
    
    real_solve = 0
    positive_real_solve = 0
    a_num = [1,4,8,9,12,13,17,18,22,23,25,26,30,31,34,35,39,40,42,43,44,45,46,47]
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
    file_context_num = file_context_num.reshape([-1,48])
    solve = file_context_num.shape[0]

def returen_result_FC(file_name):
    
    file = open(file_name)
    file_context = file.readlines()
    file.close()
    file_context_num = np.array([])
    
    real_solve = 0
    positive_real_solve = 0
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
    solve = file_context_num.shape[0]

    for i in range(file_context_num.shape[0]):
        real_label = 1
        positive_label = 1
        for j in range(len(file_context_num[i])):
            # print(file_context_num[i][j])
            if complex(file_context_num[i][j]).imag != 0:
                real_label = 0
                positive_label = 0
                break
            if j in a_num:
                continue
            elif complex(file_context_num[i][j]).real < 0 or complex(file_context_num[i][j]).real > 1:
                positive_label = 0
        if real_label == 1:
            real_solve = real_solve + 1
        if positive_label == 1:
            positive_real_solve = positive_real_solve + 1
    return positive_real_solve
    # print('Positive real solve : {}'.format(positive_real_solve))

def return_real(file_name):
    with open(file_name,'r') as file:
        for line in file:
            if re.search(r'The # of real roots =', line):
                num = re.search(r'\d+$',line)
                num = int(num.group())
                return num
