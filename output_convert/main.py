import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

positive_real_matrix = np.loadtxt('positive_real.txt', delimiter = ',')
positive_real_matrix_FC = np.loadtxt('positive_real_FC.txt', delimiter = ',')
real_matrix = np.loadtxt('real.txt', delimiter = ',')
real_matrix_FC = np.loadtxt('real_FC.txt', delimiter = ',')

# x = np.linspace(-2,2,20)
# y = np.linspace(-2,2,20)
# X,Y = np.meshgrid(x,y)
# Z = real_matrix
# fig = plt.figure()
# ax = fig.add_subplot(111,projection='3d')
# ax.plot_surface(X,Y,Z)

# plt.imshow(real_matrix, cmap='hot')
# plt.imshow(real_matrix_FC, cmap='hot')
# plt.imshow(positive_real_matrix, cmap='hot')
# plt.imshow(positive_real_matrix_FC, cmap='hot')
# plt.colorbar()


plt.show()