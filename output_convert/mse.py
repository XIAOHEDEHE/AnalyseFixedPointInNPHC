import os
import re
import math
import numpy as np

name = os.listdir('output_real')
for file_name in name:
# 打开文件提取内容
    file = open('output_real/'+file_name)
    file_context = file.readlines()
    file.close()

    mse_store = np.array([])
    mse_output = np.array([])
    # 输出结果中各个U的顺序
    neighbor_message = np.array([[2,3],[0,5,6],[7,10],[11,14,15],[16,19,20,21],[24,27,28],[29,32],[33,36,37],[38,41]])
    possibility = np.array([])

    # 将file_context中的字符串类型转化为实数类型，去除它的虚数部分，之后将其存储在mse_store中
    file_context_real = np.array([])
    for line in file_context:
        file_context_real = np.append(file_context_real,complex(line).real)
    file_context_real = file_context_real.reshape((-1,48))

    # for i in range(file_context_real.shape[0]):
    #     for j in outputU:
    #         mse_store = np.append(mse_store,file_context_real[i][j])
    # mse_store = mse_store.reshape([-1,24])
    
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
    possibility = possibility.reshape(-1,9)
        

    # 计算MSE
    for i in range(file_context_real.shape[0]):
        mse_output = np.append(mse_output,np.mean(possibility[i]*2-1))
        
    np.savetxt('MSE/'+file_name, mse_output, fmt = '%f', delimiter = ',')
    print(mse_output)
