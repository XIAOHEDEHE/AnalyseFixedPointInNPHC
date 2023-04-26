# Import the packages
import math
import os
import numpy as np

# Build two lists to indicate the paramters of the Φ
phi_i = np.array([])
phi_ij = np.array([])
for theta in np.arange(-2.0,2.0,0.2):
    for j in np.arange(-2.0,2.0,0.2):
        phi_ij = np.append(phi_ij,math.exp(j))
        phi_i = np.append(phi_i,math.exp(theta)) 
 

# Then we can do label these points from left to right, from up to down.
#

# Function for u12
polys_u12 = np.array([[]])
param_count = np.size(phi_i)
for i in range(0,phi_i.size):
    f1 = '-u12 + a12*{}*u31*u41 + a12*{}*(1-u41)*(1-u31);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u12-1 + a12*{}*u31*u41 + a12*{}*(1-u41)*(1-u31);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u12 = np.append(polys_u12,f)
polys_u12 = polys_u12.reshape(param_count,2)
# Function for u21
polys_u21 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u21 + a21*{}*u42*u32 + a21*{}*(1-u42)*(1-u32);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u21-1 + a21*{}*u42*u32 + a21*{}*(1-u42)*(1-u32);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u21 = np.append(polys_u21,f)
polys_u21 = polys_u21.reshape(param_count,2)

# Function for u23
polys_u23 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u23 + a23*{}*u12*u42 + a23*{}*(1-u12)*(1-u42);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u23-1 + a23*{}*u12*u42 + a23*{}*(1-u12)*(1-u42);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u23 = np.append(polys_u23,f)
polys_u23 = polys_u23.reshape(param_count,2)
# Function for u32
polys_u32 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u32 + a32*{}*u13*u43 + a32*{}*(1-u13)*(1-u43);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u32-1 + a32*{}*u13*u43 + a32*{}*(1-u13)*(1-u43);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u32 = np.append(polys_u32,f)
polys_u32 = polys_u32.reshape(param_count,2)
 
# Function for u14
polys_u14 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u14 + a14*{}*u21*u31 + a14*{}*(1-u21)*(1-u31);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u14-1 + a14*{}*u21*u31 + a14*{}*(1-u21)*(1-u31);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u14 = np.append(polys_u14,f)
polys_u14 = polys_u14.reshape(param_count,2)
# Function for u41
polys_u41 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u41 + a41*{}*u34*u24 + a41*{}*(1-u34)*(1-u24);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u41-1 + a41*{}*u34*u24 + a41*{}*(1-u34)*(1-u24);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u41 + (1-u41) -1;'
    f = np.array([f1,f2])
    polys_u41 = np.append(polys_u41,f)
polys_u41 = polys_u41.reshape(param_count,2)

# Function for u24
polys_u24 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u24 + a24*{}*u12*u32 + a24*{}*(1-u12)*(1-u32);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u24-1 + a24*{}*u12*u32 + a24*{}*(1-u12)*(1-u32);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u24 = np.append(polys_u24,f)
polys_u24 = polys_u24.reshape(param_count,2)
# Function for u42
polys_u42 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u42 + a42*{}*u14*u34 + a42*{}*(1-u14)*(1-u34);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u42-1 + a42*{}*u14*u34 + a42*{}*(1-u14)*(1-u34);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u42 = np.append(polys_u42,f)
polys_u42 = polys_u42.reshape(param_count,2)

# Function for u13
polys_u13 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u13 + a13*{}*u21*u41 + a13*{}*(1-u21)*(1-u41);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u13-1 + a13*{}*u21*u41 + a13*{}*(1-u21)*(1-u41);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u13 = np.append(polys_u13,f)
polys_u13 = polys_u13.reshape(param_count,2)
# Function for u31
polys_u31 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u31 + a31*{}*u23*u43 + a31*{}*(1-u23)*(1-u43);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u31-1 + a31*{}*u23*u43 + a31*{}*(1-u23)*(1-u43);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u31 = np.append(polys_u31,f)
polys_u31 = polys_u31.reshape(param_count,2)

# Function for u34
polys_u34 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u34 + a34*{}*u13*u23 + a34*{}*(1-u13)*(1-u23);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u34-1 + a34*{}*u13*u23 + a34*{}*(1-u13)*(1-u23);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u34 = np.append(polys_u34,f)
polys_u34 = polys_u34.reshape(param_count,2)
# Function for u43
polys_u43 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u43 + a43*{}*u14*u24 + a43*{}*(1-u14)*(1-u24);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u43-1 + a43*{}*u14*u24 + a43*{}*(1-u14)*(1-u24);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f = np.array([f1,f2])
    polys_u43 = np.append(polys_u43,f)
polys_u43 = polys_u43.reshape(param_count,2)

# For now we have got 12 edges' functions, which indicated by 12 
# lists with param_count*3 dimensions. We hope to conbine them to get a
# param_count*72 dimensions' list.
polys = [polys_u12,polys_u21,polys_u23,polys_u32,
         polys_u14,polys_u41,polys_u24,polys_u42,
         polys_u13,polys_u31,polys_u34,polys_u43]
polys_sum = np.concatenate(polys, axis=1)

for i in range(0,param_count):
    filename = "input{}.txt".format(i)
    sub_folder = "data_fullyconnected"
    
    if not os.path.exists(os.path.join(sub_folder,filename)):
        open(os.path.join(sub_folder,filename),"w").close()
        print("Created successfully")
    else:
        print("File existed")
    np.savetxt(os.path.join(sub_folder,filename),polys_sum[i],fmt="%s")
    with open(os.path.join(sub_folder,filename),"r+") as f:
        content = f.read()
        f.seek(0,0)
        f.write("{\n"+content)
        f.seek(0,2)
        f.write("\n}")
