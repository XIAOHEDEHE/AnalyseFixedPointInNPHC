# Import the packages
import math
import os
import numpy as np

# Build two lists to indicate the paramters of the Φ
phi_i = np.array([])
phi_ij = np.array([])
for theta in np.arange(-2.0,2.0,0.1):
    for j in np.arange(-2.0,2.0,0.1):
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
for i in range(0,phi_i.size):
    f1 = '-u12 + a12*{}*u41 + a12*{}*u410;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u120 + a12*{}*u41 + a12*{}*u410;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u12 + u120 -1;'
    f = np.array([f1,f2,f3])
    polys_u12 = np.append(polys_u12,f)
polys_u12 = polys_u12.reshape(1600,3)
# Function for u21
polys_u21 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u21 + a21*{}*u52*u32 + a21*{}*u520*u320;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u210 + a21*{}*u52*u32 + a21*{}*u520*u320;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u21 + u210 -1;'
    f = np.array([f1,f2,f3])
    polys_u21 = np.append(polys_u21,f)
polys_u21 = polys_u21.reshape(1600,3)

# Function for u23
polys_u23 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u23 + a23*{}*u12*u52 + a23*{}*u120*u520;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u230 + a23*{}*u12*u52 + a23*{}*u120*u520;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u23 + u230 -1;'
    f = np.array([f1,f2,f3])
    polys_u23 = np.append(polys_u23,f)
polys_u23 = polys_u23.reshape(1600,3)
# Function for u32
polys_u32 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u32 + a32*{}*u63 + a32*{}*u630;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u320 + a32*{}*u63 + a32*{}*u630;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u32 + u320 -1;'
    f = np.array([f1,f2,f3])
    polys_u32 = np.append(polys_u32,f)
polys_u32 = polys_u32.reshape(1600,3)
 
# Function for u14
polys_u14 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u14 + a14*{}*u21 + a14*{}*u210;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u140 + a14*{}*u21 + a14*{}*u210;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u14 + u140 -1;'
    f = np.array([f1,f2,f3])
    polys_u14 = np.append(polys_u14,f)
polys_u14 = polys_u14.reshape(1600,3)
# Function for u41
polys_u41 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u41 + a41*{}*u54*u74 + a41*{}*u540*u740;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u410 + a41*{}*u54*u74 + a41*{}*u540*u740;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u41 + u410 -1;'
    f = np.array([f1,f2,f3])
    polys_u41 = np.append(polys_u41,f)
polys_u41 = polys_u41.reshape(1600,3)

# Function for u25
polys_u25 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u25 + a25*{}*u12*u32 + a25*{}*u120*u320;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u250 + a25*{}*u12*u32 + a25*{}*u120*u320;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u25 + u250 -1;'
    f = np.array([f1,f2,f3])
    polys_u25 = np.append(polys_u25,f)
polys_u25 = polys_u25.reshape(1600,3)
# Function for u52
polys_u52 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u52 + a52*{}*u45*u85*u65 + a52*{}*u450*u850*u650;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u520 + a52*{}*u45*u85*u65 + a52*{}*u450*u850*u650;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u52 + u520 -1;'
    f = np.array([f1,f2,f3])
    polys_u52 = np.append(polys_u52,f)
polys_u52 = polys_u52.reshape(1600,3)

# Function for u36
polys_u36 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u36 + a36*{}*u23 + a36*{}*u230;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u360 + a36*{}*u23 + a36*{}*u230;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u36 + u360 -1;'
    f = np.array([f1,f2,f3])
    polys_u36 = np.append(polys_u36,f)
polys_u36 = polys_u36.reshape(1600,3)
# Function for u63
polys_u63 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u63 + a63*{}*u56*u96 + a63*{}*u560*u960;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u630 + a63*{}*u56*u96 + a63*{}*u560*u960;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u63 + u630 -1;'
    f = np.array([f1,f2,f3])
    polys_u63 = np.append(polys_u63,f)
polys_u63 = polys_u63.reshape(1600,3)

# Function for u45
polys_u45 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u45 + a45*{}*u14*u74 + a45*{}*u140*u740;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u450 + a45*{}*u14*u74 + a45*{}*u140*u740;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u45 + u450 -1;'
    f = np.array([f1,f2,f3])
    polys_u45 = np.append(polys_u45,f)
polys_u45 = polys_u45.reshape(1600,3)
# Function for u54
polys_u54 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u54 + a54*{}*u25*u85*u65 + a54*{}*u250*u850*u650;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u540 + a54*{}*u25*u85*u65 + a54*{}*u250*u850*u650;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u54 + u540 -1;'
    f = np.array([f1,f2,f3])
    polys_u54 = np.append(polys_u54,f)
polys_u54 = polys_u54.reshape(1600,3)

# Function for u56
polys_u56 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u56 + a56*{}*u25*u85*u45 + a56*{}*u250*u850*u450;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u560 + a56*{}*u25*u85*u45 + a56*{}*u250*u850*u450;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u56 + u560 -1;'
    f = np.array([f1,f2,f3])
    polys_u56 = np.append(polys_u56,f)
polys_u56 = polys_u56.reshape(1600,3)
# Function for u65
polys_u65 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u65 + a65*{}*u36*u96 + a65*{}*u360*u960;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u650 + a65*{}*u36*u96 + a65*{}*u360*u960;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u65 + u650 -1;'
    f = np.array([f1,f2,f3])
    polys_u65 = np.append(polys_u65,f)
polys_u65 = polys_u65.reshape(1600,3)

# Function for u47
polys_u47 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u47 + a47*{}*u14*u54 + a47*{}*u140*u540;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u470 + a47*{}*u14*u54 + a47*{}*u140*u540;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u47 + u470 -1;'
    f = np.array([f1,f2,f3])
    polys_u47 = np.append(polys_u47,f)
polys_u47 = polys_u47.reshape(1600,3)
# Function for u74
polys_u74 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u74 + a74*{}*u87 + a74*{}*u870;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u740 + a74*{}*u87 + a74*{}*u870;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u74 + u740 -1;'
    f = np.array([f1,f2,f3])
    polys_u74 = np.append(polys_u74,f)
polys_u74 = polys_u74.reshape(1600,3)

# Function for u58
polys_u58 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u58 + a58*{}*u25*u56*u45 + a58*{}*u250*u560*u450;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u580 + a58*{}*u25*u56*u45 + a58*{}*u250*u560*u450;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u58 + u580 -1;'
    f = np.array([f1,f2,f3])
    polys_u58 = np.append(polys_u58,f)
polys_u58 = polys_u58.reshape(1600,3)
# Function for u85
polys_u85 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u85 + a85*{}*u78*u98 + a85*{}*u780*u980;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u850 + a85*{}*u78*u98 + a85*{}*u780*u980;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u85 + u850 -1;'
    f = np.array([f1,f2,f3])
    polys_u85 = np.append(polys_u85,f)
polys_u85 = polys_u85.reshape(1600,3)

# Function for u69
polys_u69 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u69 + a69*{}*u56*u36 + a69*{}*u560*u360;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u690 + a69*{}*u56*u36 + a69*{}*u560*u360;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u69 + u690 -1;'
    f = np.array([f1,f2,f3])
    polys_u69 = np.append(polys_u69,f)
polys_u69 = polys_u69.reshape(1600,3)
# Function for u96
polys_u96 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u96 + a96*{}*u89 + a96*{}*u890;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u960 + a96*{}*u89 + a96*{}*u890;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u96 + u960 -1;'
    f = np.array([f1,f2,f3])
    polys_u96 = np.append(polys_u96,f)
polys_u96 = polys_u96.reshape(1600,3)

# Function for u78
polys_u78 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u78 + a78*{}*u47 + a78*{}*u470;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u780 + a78*{}*u47 + a78*{}*u470;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u78 + u780 -1;'
    f = np.array([f1,f2,f3])
    polys_u78 = np.append(polys_u78,f)
polys_u78 = polys_u78.reshape(1600,3)
# Function for u87
polys_u87 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u87 + a87*{}*u58*u98 + a87*{}*u580*u980;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u870 + a87*{}*u58*u98 + a87*{}*u580*u980;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u87 + u870 -1;'
    f = np.array([f1,f2,f3])
    polys_u87 = np.append(polys_u87,f)
polys_u87 = polys_u87.reshape(1600,3)

# Function for u89
polys_u89 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u89 + a89*{}*u58*u78 + a89*{}*u580*u780;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u890 + a89*{}*u58*u78 + a89*{}*u580*u780;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u89 + u890 -1;'
    f = np.array([f1,f2,f3])
    polys_u89 = np.append(polys_u89,f)
polys_u89 = polys_u89.reshape(1600,3)
# Function for u98
polys_u98 = np.array([[]])
for i in range(0,phi_i.size):
    f1 = '-u98 + a98*{}*u69 + a98*{}*u690;'.format(phi_i[i]*phi_ij[i],(1/phi_i[i])*(1/phi_ij[i]))
    f2 = '-u980 + a98*{}*u69 + a98*{}*u690;'.format((1/phi_ij[i])*(phi_i[i]),phi_ij[i]*(1/phi_i[i]))
    f3 = 'u98 + u980 -1;'
    f = np.array([f1,f2,f3])
    polys_u98 = np.append(polys_u98,f)
polys_u98 = polys_u98.reshape(1600,3)

# For now we have got 12 edges' functions, which indicated by 12 
# lists with 1600*3 dimensions. We hope to conbine them to get a
# 1600*72 dimensions' list.
polys = [polys_u12,polys_u21,polys_u23,polys_u32,
         polys_u14,polys_u41,polys_u25,polys_u52,
         polys_u45,polys_u54,polys_u56,polys_u65,
         polys_u47,polys_u74,polys_u58,polys_u85,
         polys_u69,polys_u96,polys_u78,polys_u87,
         polys_u89,polys_u98,polys_u36,polys_u63]
polys_sum = np.concatenate(polys, axis=1)

for i in range(0,1600):
    filename = "input{}.txt".format(i)
    sub_folder = "data_full"
    
    if not os.path.exists(os.path.join(sub_folder,filename)):
        open(os.path.join(sub_folder,filename),"w").close()
        print("Created successfully")
    else:
        print("File is exist")
    np.savetxt(os.path.join(sub_folder,filename),polys_sum[i],fmt="%s")
    with open(os.path.join(sub_folder,filename),"r+") as f:
        content = f.read()
        f.seek(0,0)
        f.write("{\n"+content)
        f.seek(0,2)
        f.write("\n}")