import os
import re
import math
import numpy as np

name = os.listdir('output_FC_real')
for file_name in name:
# 打开文件提取内容
    file = open('output_FC_real/'+file_name)
    file_context = file.readlines()
    file.close()

    mse_store = np.array([])
    mse_output = np.array([])
    # 输出结果中各个U的顺序
    neighbor_message = np.array([[2,3,4],[0,6,7],[8,11,12],[13,16,17]])
    possibility = np.array([])

    # 将file_context中的字符串类型转化为实数类型，去除它的虚数部分，之后将其存储在mse_store中
    file_context_real = np.array([])
    for line in file_context:
        file_context_real = np.append(file_context_real,complex(line).real)
    file_context_real = file_context_real.reshape((-1,24))

    pattern = r'\d+'
    number = re.findall(pattern,file_name)
    theta = -2+0.2*(int(number[0])//20)
    
    
    for i in range(file_context_real.shape[0]):
        for j in range(neighbor_message.shape[0]):
            temp_possitive = 1
            temp_negative = 1
            for message in neighbor_message[j]:
                temp_possitive = temp_possitive*file_context_real[i][message]
                temp_negative = temp_negative*(1-file_context_real[i][message])
            temp_negative = temp_negative*math.exp(-theta)
            temp_possitive = temp_possitive*math.exp(theta)
            if (temp_possitive+temp_negative) != 0 :
                temp = temp_possitive/(temp_possitive+temp_negative)
            possibility = np.append(possibility,temp)
    possibility = possibility.reshape(-1,4)
        

    # 计算MSE
    for i in range(file_context_real.shape[0]):
        mse_output = np.append(mse_output,np.mean(possibility[i]*2-1))
        
    np.savetxt('MSE_FC/'+file_name, mse_output, fmt = '%f', delimiter = ',')
    print(mse_output)
