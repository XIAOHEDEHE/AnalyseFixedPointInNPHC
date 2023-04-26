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
 
#
# If we have a 3*3 Grid Graph with Uniform Factors like below:
#      O---O---O           X1--X2--X3   
#      |   |   |           |   |   |
#      O---O---O           X4--X5--X6
#      |   |   |           |   |   |
#      O---O---O           X7--X8--X9
# Then we can do label these points from left to right, from up to down.
#

# Function for u12
polys_u12 = np.array([[]])
param_count = np.size(phi_i)
for i in range(0,phi_i.size):
    f1 = '-u12 + a12*{}*u41 + a12*{}*(1-u41);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u12-1 + a12*{}*u41 + a12*{}*(1-u41);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u12 + (1-u12) -1;'
    f = np.array([f1,f2])
    polys_u12 = np.append(polys_u12,f)
polys_u12 = polys_u12.reshape(param_count,2)
# Function for u21
polys_u21 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u21 + a21*{}*u52*u32 + a21*{}*(1-u52)*(1-u32);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u21-1 + a21*{}*u52*u32 + a21*{}*(1-u52)*(1-u32);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u21 + (1-u21) -1;'
    f = np.array([f1,f2])
    polys_u21 = np.append(polys_u21,f)
polys_u21 = polys_u21.reshape(param_count,2)

# Function for u23
polys_u23 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u23 + a23*{}*u12*u52 + a23*{}*(1-u12)*(1-u52);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u23-1 + a23*{}*u12*u52 + a23*{}*(1-u12)*(1-u52);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u23 + (1-u23) -1;'
    f = np.array([f1,f2])
    polys_u23 = np.append(polys_u23,f)
polys_u23 = polys_u23.reshape(param_count,2)
# Function for u32
polys_u32 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u32 + a32*{}*u63 + a32*{}*(1-u63);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u32-1 + a32*{}*u63 + a32*{}*(1-u63);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u32 + (1-u32) -1;'
    f = np.array([f1,f2])
    polys_u32 = np.append(polys_u32,f)
polys_u32 = polys_u32.reshape(param_count,2)
 
# Function for u14
polys_u14 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u14 + a14*{}*u21 + a14*{}*(1-u21);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u14-1 + a14*{}*u21 + a14*{}*(1-u21);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u14 + (1-u14) -1;'
    f = np.array([f1,f2])
    polys_u14 = np.append(polys_u14,f)
polys_u14 = polys_u14.reshape(param_count,2)
# Function for u41
polys_u41 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u41 + a41*{}*u54*u74 + a41*{}*(1-u54)*(1-u74);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u41-1 + a41*{}*u54*u74 + a41*{}*(1-u54)*(1-u74);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u41 + (1-u41) -1;'
    f = np.array([f1,f2])
    polys_u41 = np.append(polys_u41,f)
polys_u41 = polys_u41.reshape(param_count,2)

# Function for u25
polys_u25 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u25 + a25*{}*u12*u32 + a25*{}*(1-u12)*(1-u32);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u25-1 + a25*{}*u12*u32 + a25*{}*(1-u12)*(1-u32);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u25 + (1-u25) -1;'
    f = np.array([f1,f2])
    polys_u25 = np.append(polys_u25,f)
polys_u25 = polys_u25.reshape(param_count,2)
# Function for u52
polys_u52 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u52 + a52*{}*u45*u85*u65 + a52*{}*(1-u45)*(1-u85)*(1-u65);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u52-1 + a52*{}*u45*u85*u65 + a52*{}*(1-u45)*(1-u85)*(1-u65);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u52 + (1-u52) -1;'
    f = np.array([f1,f2])
    polys_u52 = np.append(polys_u52,f)
polys_u52 = polys_u52.reshape(param_count,2)

# Function for u36
polys_u36 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u36 + a36*{}*u23 + a36*{}*(1-u23);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u36-1 + a36*{}*u23 + a36*{}*(1-u23);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u36 + (1-u36) -1;'
    f = np.array([f1,f2])
    polys_u36 = np.append(polys_u36,f)
polys_u36 = polys_u36.reshape(param_count,2)
# Function for u63
polys_u63 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u63 + a63*{}*u56*u96 + a63*{}*(1-u56)*(1-u96);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u63-1 + a63*{}*u56*u96 + a63*{}*(1-u56)*(1-u96);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u63 + (1-u63) -1;'
    f = np.array([f1,f2])
    polys_u63 = np.append(polys_u63,f)
polys_u63 = polys_u63.reshape(param_count,2)

# Function for u45
polys_u45 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u45 + a45*{}*u14*u74 + a45*{}*(1-u14)*(1-u74);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u45-1 + a45*{}*u14*u74 + a45*{}*(1-u14)*(1-u74);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u45 + (1-u45) -1;'
    f = np.array([f1,f2])
    polys_u45 = np.append(polys_u45,f)
polys_u45 = polys_u45.reshape(param_count,2)
# Function for u54
polys_u54 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u54 + a54*{}*u25*u85*u65 + a54*{}*(1-u25)*(1-u85)*(1-u65);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u54-1 + a54*{}*u25*u85*u65 + a54*{}*(1-u25)*(1-u85)*(1-u65);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u54 + (1-u54) -1;'
    f = np.array([f1,f2])
    polys_u54 = np.append(polys_u54,f)
polys_u54 = polys_u54.reshape(param_count,2)

# Function for u56
polys_u56 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u56 + a56*{}*u25*u85*u45 + a56*{}*(1-u25)*(1-u85)*(1-u45);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u56-1 + a56*{}*u25*u85*u45 + a56*{}*(1-u25)*(1-u85)*(1-u45);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u56 + (1-u56) -1;'
    f = np.array([f1,f2])
    polys_u56 = np.append(polys_u56,f)
polys_u56 = polys_u56.reshape(param_count,2)
# Function for u65
polys_u65 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u65 + a65*{}*u36*u96 + a65*{}*(1-u36)*(1-u96);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u65-1 + a65*{}*u36*u96 + a65*{}*(1-u36)*(1-u96);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u65 + (1-u65) -1;'
    f = np.array([f1,f2])
    polys_u65 = np.append(polys_u65,f)
polys_u65 = polys_u65.reshape(param_count,2)

# Function for u47
polys_u47 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u47 + a47*{}*u14*u54 + a47*{}*(1-u14)*(1-u54);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u47-1 + a47*{}*u14*u54 + a47*{}*(1-u14)*(1-u54);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u47 + (1-u47) -1;'
    f = np.array([f1,f2])
    polys_u47 = np.append(polys_u47,f)
polys_u47 = polys_u47.reshape(param_count,2)
# Function for u74
polys_u74 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u74 + a74*{}*u87 + a74*{}*(1-u87);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u74-1 + a74*{}*u87 + a74*{}*(1-u87);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u74 + (1-u74) -1;'
    f = np.array([f1,f2])
    polys_u74 = np.append(polys_u74,f)
polys_u74 = polys_u74.reshape(param_count,2)

# Function for u58
polys_u58 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u58 + a58*{}*u25*u56*u45 + a58*{}*(1-u25)*(1-u56)*(1-u45);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u58-1 + a58*{}*u25*u56*u45 + a58*{}*(1-u25)*(1-u56)*(1-u45);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u58 + (1-u58) -1;'
    f = np.array([f1,f2])
    polys_u58 = np.append(polys_u58,f)
polys_u58 = polys_u58.reshape(param_count,2)
# Function for u85
polys_u85 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u85 + a85*{}*u78*u98 + a85*{}*(1-u78)*(1-u98);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u85-1 + a85*{}*u78*u98 + a85*{}*(1-u78)*(1-u98);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u85 + (1-u85) -1;'
    f = np.array([f1,f2])
    polys_u85 = np.append(polys_u85,f)
polys_u85 = polys_u85.reshape(param_count,2)

# Function for u69
polys_u69 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u69 + a69*{}*u56*u36 + a69*{}*(1-u56)*(1-u36);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u69-1 + a69*{}*u56*u36 + a69*{}*(1-u56)*(1-u36);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u69 + (1-u69) -1;'
    f = np.array([f1,f2])
    polys_u69 = np.append(polys_u69,f)
polys_u69 = polys_u69.reshape(param_count,2)
# Function for u96
polys_u96 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u96 + a96*{}*u89 + a96*{}*(1-u89);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u96-1 + a96*{}*u89 + a96*{}*(1-u89);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u96 + (1-u96) -1;'
    f = np.array([f1,f2])
    polys_u96 = np.append(polys_u96,f)
polys_u96 = polys_u96.reshape(param_count,2)

# Function for u78
polys_u78 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u78 + a78*{}*u47 + a78*{}*(1-u47);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u78-1 + a78*{}*u47 + a78*{}*(1-u47);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u78 + (1-u78) -1;'
    f = np.array([f1,f2])
    polys_u78 = np.append(polys_u78,f)
polys_u78 = polys_u78.reshape(param_count,2)
# Function for u87
polys_u87 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u87 + a87*{}*u58*u98 + a87*{}*(1-u58)*(1-u98);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u87-1 + a87*{}*u58*u98 + a87*{}*(1-u58)*(1-u98);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u87 + (1-u87) -1;'
    f = np.array([f1,f2])
    polys_u87 = np.append(polys_u87,f)
polys_u87 = polys_u87.reshape(param_count,2)

# Function for u89
polys_u89 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u89 + a89*{}*u58*u78 + a89*{}*(1-u58)*(1-u78);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u89-1 + a89*{}*u58*u78 + a89*{}*(1-u58)*(1-u78);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u89 + (1-u89) -1;'
    f = np.array([f1,f2])
    polys_u89 = np.append(polys_u89,f)
polys_u89 = polys_u89.reshape(param_count,2)
# Function for u98
polys_u98 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u98 + a98*{}*u69 + a98*{}*(1-u69);'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = 'u98-1 + a98*{}*u69 + a98*{}*(1-u69);'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    # f3 = 'u98 + (1-u98) -1;'
    f = np.array([f1,f2])
    polys_u98 = np.append(polys_u98,f)
polys_u98 = polys_u98.reshape(param_count,2)

# For now we have got 12 edges' functions, which indicated by 12 
# lists with param_count*3 dimensions. We hope to conbine them to get a
# param_count*72 dimensions' list.
polys = [polys_u12,polys_u21,polys_u23,polys_u32,
         polys_u14,polys_u41,polys_u25,polys_u52,
         polys_u45,polys_u54,polys_u56,polys_u65,
         polys_u47,polys_u74,polys_u58,polys_u85,
         polys_u69,polys_u96,polys_u78,polys_u87,
         polys_u89,polys_u98,polys_u36,polys_u63]
polys_sum = np.concatenate(polys, axis=1)

for i in range(0,param_count):
    filename = "input{}.txt".format(i)
    sub_folder = "data"
    
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


'''np.savetxt("input0.txt",polys_sum[0],fmt="%s")
with open("input0.txt","r+") as f:
    content = f.read()
    f.seek(0,0)
    f.write("{\n"+content)
    f.seek(0,2)
    f.write("\n}")'''