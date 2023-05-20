import numpy as np
from matplotlib import pyplot as plt

theta00 = np.arange(200,220)
theta02 = np.arange(220,240)
theta06 = np.arange(260,280)

def show_mse(filename_num):
    full_result = np.array([[]])
    
    # 创建一个新的图表和坐标系
    fig, ax = plt.subplots()

    # 设置横坐标范围
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1,1)
    
    for i in range(len(filename_num)):
        mse_result = np.loadtxt('MSE_FC/output{}.txt'.format(filename_num[i]), delimiter = ',')
        x = np.ones(mse_result.shape)*0.2*i-2
        ax.scatter(x, mse_result, color='blue',s=5)
    plt.grid()
    plt.show()
        
print(show_mse(theta00))
