import re
import numpy as np

file_name = 'error-correcting\out.txt'
file = open(file_name)
file_context = file.readlines()
file.close()
file_context_num = np.array([])

f1 = np.array([0,24])
f2 = np.array([5,12])
f3 = np.array([8,17,29])
f4 = np.array([20,32])


for i in range(len(file_context)):
    if file_context[i].startswith('('):
        file_context[i] = file_context[i].replace('(','')
        file_context[i] = file_context[i].replace(')','')
        file_context[i] = file_context[i].replace('\n','j')
        file_context[i] = file_context[i].replace(' ','')
        file_context[i] = file_context[i].replace(',-','+')
        file_context[i] = file_context[i].replace(',','+')
        
        file_context_num = np.append(file_context_num,file_context[i])
file_context_num = file_context_num.reshape([-1,45])

for x in file_context_num[1]:
    print(complex(x).real)

# for i in range(file_context_num.shape[0]):
#     result_positive = np.array([])
#     result_passive = np.array([])
#     p1 = 1
#     p2 = 1
#     p3 = 1
#     p4 = 1
#     p10 = 1
#     p20 = 1
#     p30 = 1
#     p40 = 1
#     for j in f1:
#         p1 = p1*complex(file_context_num[i][j]).real
#         p10 = p10*(1- complex(file_context_num[i][j]).real)
#     temp = p1+p10
#     p1 = p1/temp
#     p10 = p10/temp
#     result_positive = np.append(result_positive,p1)
#     result_passive = np.append(result_passive,p10)
#     for j in f2:
#         p2 = p2*complex(file_context_num[i][j]).real
#         p20 = p20*(1- complex(file_context_num[i][j]).real)
#     temp = p2+p20
#     p2 = p2/temp
#     p20 = p20/temp
#     result_positive = np.append(result_positive,p2)
#     result_passive = np.append(result_passive,p20)
#     for j in f3:
#         p3 = p3*complex(file_context_num[i][j]).real
#         p30 = p30*(1- complex(file_context_num[i][j]).real)
#     temp = p3+p30
#     p3 = p3/temp
#     p30 = p30/temp
#     result_positive = np.append(result_positive,p3)
#     result_passive = np.append(result_passive,p30)
#     for j in f4:
#         p4 = p4*complex(file_context_num[i][j]).real
#         p40 = p40*(1- complex(file_context_num[i][j]).real)
#     temp = p4+p40
#     p4 = p4/temp
#     p40 = p40/temp
#     result_positive = np.append(result_positive,p4)
#     result_passive = np.append(result_passive,p40)
#     print(result_positive)
#     print(result_passive)
    
