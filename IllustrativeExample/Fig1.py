import numpy as np
from matplotlib import pyplot as plt

# # Fig.1(a): Polytope S1
# x = np.array([0,2,1])
# y = np.array([0,1,0])
# plt.xlim(0,4)
# plt.ylim(0,4)
# plt.grid()
# plt.plot(x,y,color='k')
# plt.show()

# # Fig.1(b): Polytope S2
# x = np.array([0,1,1])
# y = np.array([1,1,0])
# plt.xlim(0,4)
# plt.ylim(0,4)
# plt.grid()
# plt.plot(x,y,color='k')
# plt.show()

# Fig.1(c): Minkowski sum
x = np.array([0,2,3,3,2])
y = np.array([1,2,2,1,0])
x1 = np.array([0,2,1])
y1 = np.array([0,1,0])
x2 = np.array([2,3,2,2])
y2 = np.array([1,1,1,2])
plt.xlim(0,4)
plt.ylim(0,5)
plt.grid()
plt.plot(x,y,color='k')
plt.plot(x1,y1,color='k')
plt.plot(x2,y2,color='k')
plt.show()