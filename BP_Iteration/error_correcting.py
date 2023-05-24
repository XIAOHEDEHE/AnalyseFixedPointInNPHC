import numpy as np

# # Initial message
# ra1=0.428571429
# ra2=0.428571429
# ra3=0.428571429
# ra5=0.428571429
# rb2=0.428571429
# rb3=0.428571429
# rb4=0.428571429
# rb6=0.428571429
# rc1=0.428571429
# rc3=0.428571429
# rc4=0.428571429
# rc7=0.428571429
# q2a=0.428571429
# q3a=0.36
# q5a=0.5
# q1a=0.428571429
# q3b=0.36
# q4b=0.428571429
# q6b=0.5
# q2b=0.428571429
# q3c=0.36
# q4c=0.428571429
# q7c=0.5
# q1c=0.428571429

# # another
# ra1=0.5
# q2a=0.5
# q3a=0.5
# q5a=0.5
# ra2=0.5
# q1a=0.5
# ra3=0.5
# ra5=0.5
# rb2=0.5
# q3b=0.5
# q4b=0.5
# q6b=0.5
# rb3=0.5
# q2b=0.5
# rb4=0.5
# rb6=0.5
# rc1=0.5
# q3c=0.5
# q4c=0.5
# q7c=0.5
# rc3=0.5
# q1c=0.5
# rc4=0.5
# rc7=0.5

# Initial message
ra1=0.1
ra2=0.2
ra3=0.3
ra5=0.22
rb2=0.37
rb3=0.65
rb4=0.24
rb6=0.33
rc1=0.87
rc3=0.21
rc4=0.32
rc7=0.42
q2a=0.44
q3a=0.47
q5a=0.5
q1a=0.87
q3b=0.88
q4b=0.76
q6b=0.5
q2b=0.52
q3c=0.15
q4c=0.11
q7c=0.5
q1c=0.24


for i in range(50):
    ra11_new = (1-q2a)*(1-q3a)*q5a + q2a*(1-q3a)*(1-q5a) + (1-q2a)*q3a*(1-q5a) + q2a*q3a*q5a
    ra10_new = (1-q2a)*(1-q3a)*(1-q5a) + q2a*q3a*(1-q5a) + (1-q2a)*q3a*q5a + q2a*(1-q3a)*q5a
    ra21_new = (1-q1a)*(1-q3a)*q5a + q1a*(1-q3a)*(1-q5a) + (1-q1a)*q3a*(1-q5a) + q1a*q3a*q5a
    ra20_new = (1-q1a)*(1-q3a)*(1-q5a) + q1a*q3a*(1-q5a) + (1-q1a)*q3a*q5a + q1a*(1-q3a)*q5a
    ra31_new = (1-q1a)*(1-q2a)*q5a + q1a*(1-q2a)*(1-q5a) + (1-q1a)*q2a*(1-q5a) + q1a*q2a*q5a
    ra30_new = (1-q1a)*(1-q2a)*(1-q5a) + q1a*q2a*(1-q5a) + (1-q1a)*q2a*q5a + q1a*(1-q2a)*q5a
    ra51_new = (1-q1a)*(1-q2a)*q3a + q1a*(1-q2a)*(1-q3a) + (1-q1a)*q2a*(1-q3a) + q1a*q2a*q3a
    ra50_new = (1-q1a)*(1-q2a)*(1-q3a) + q1a*q2a*(1-q3a) + (1-q1a)*q2a*q3a + q1a*(1-q2a)*q3a

    rb21_new = (1-q3b)*(1-q4b)*q6b + q3b*(1-q4b)*(1-q6b) + (1-q3b)*q4b*(1-q6b) + q3b*q4b*q6b
    rb20_new = (1-q3b)*(1-q4b)*(1-q6b) + q3b*q4b*(1-q6b) + (1-q3b)*q4b*q6b + q3b*(1-q4b)*q6b
    rb31_new = (1-q2b)*(1-q4b)*q6b + q2b*(1-q4b)*(1-q6b) + (1-q2b)*q4b*(1-q6b) + q2b*q4b*q6b
    rb30_new = (1-q2b)*(1-q4b)*(1-q6b) + q2b*q4b*(1-q6b) + (1-q2b)*q4b*q6b + q2b*(1-q4b)*q6b
    rb41_new = (1-q3b)*(1-q6b)*q2b + q3b*(1-q6b)*(1-q2b) + (1-q3b)*q6b*(1-q2b) + q3b*q6b*q2b
    rb40_new = (1-q3b)*(1-q6b)*(1-q2b) + q3b*q6b*(1-q2b) + (1-q3b)*q6b*q2b + q3b*(1-q6b)*q2b
    rb61_new = (1-q3b)*(1-q4b)*q2b + q3b*(1-q4b)*(1-q2b) + (1-q3b)*q4b*(1-q2b) + q3b*q4b*q2b
    rb60_new = (1-q3b)*(1-q4b)*(1-q2b) + q3b*q4b*(1-q2b) + (1-q3b)*q4b*q2b + q3b*(1-q4b)*q2b

    rc11_new = (1-q3c)*(1-q4c)*q7c + q3c*(1-q4c)*(1-q7c) + (1-q3c)*q4c*(1-q7c) + q3c*q4c*q7c
    rc10_new = (1-q3c)*(1-q4c)*(1-q7c) + q3c*q4c*(1-q7c) + (1-q3c)*q4c*q7c + q3c*(1-q4c)*q7c
    rc31_new = (1-q1c)*(1-q4c)*q7c + q1c*(1-q4c)*(1-q7c) + (1-q1c)*q4c*(1-q7c) + q1c*q4c*q7c
    rc30_new = (1-q1c)*(1-q4c)*(1-q7c) + q1c*q4c*(1-q7c) + (1-q1c)*q4c*q7c + q1c*(1-q4c)*q7c
    rc41_new = (1-q3c)*(1-q1c)*q7c + q3c*(1-q1c)*(1-q7c) + (1-q3c)*q1c*(1-q7c) + q3c*q1c*q7c
    rc40_new = (1-q3c)*(1-q1c)*(1-q7c) + q3c*q1c*(1-q7c) + (1-q3c)*q1c*q7c + q3c*(1-q1c)*q7c
    rc71_new = (1-q3c)*(1-q4c)*q1c + q3c*(1-q4c)*(1-q1c) + (1-q3c)*q4c*(1-q1c) + q3c*q4c*q1c
    rc70_new = (1-q3c)*(1-q4c)*(1-q1c) + q3c*q4c*(1-q1c) + (1-q3c)*q4c*q1c + q3c*(1-q4c)*q1c

    q1a_new = rc1
    q1a0 = (1-rc1)
    q1c_new = ra1
    q1c0 = (1-ra1)
    q2a_new = rb2
    q2a0 = (1-rb2)
    q2b_new = ra2
    q2b0 = (1-ra2)
    q3a_new = rb3*rc3
    q3a0 = (1-rb3)*(1-rc3)
    q3b_new = ra3*rc3
    q3b0 = (1-ra3)*(1-rc3)
    q3c_new = ra3*rb3
    q3c0 = (1-ra3)*(1-rb3)
    q4b_new = rc4
    q4b0 = (1-rc4)
    q4c_new = rb4
    q4c0 = (1-q4c)

    q1a_new = q1a_new/(q1a0+q1a_new)
    q1c_new = q1c_new/(q1c0+q1c_new)
    q2a_new = q2a_new/(q2a0+q2a_new)
    q2b_new = q2b_new/(q2b0+q2b_new)
    q3a_new = q3a_new/(q3a0+q3a_new)
    q3c_new = q3c_new/(q3c0+q3c_new)
    q3b_new = q3b_new/(q3b0+q3b_new)
    q4b_new = q4b_new/(q4b0+q4b_new)
    q4c_new = q4c_new/(q4c0+q4c_new)

    ra1=ra11_new
    ra2=ra21_new
    ra3=ra31_new
    ra5=ra51_new
    rb2=rb21_new
    rb3=rb31_new
    rb4=rb41_new
    rb6=rb61_new
    rc1=rc11_new
    rc3=rc31_new
    rc4=rc41_new
    rc7=rc71_new
    q2a=q2a_new
    q3a=q3a_new
    q1a=q1a_new
    q3b=q3b_new
    q4b=q4b_new
    q2b=q2b_new
    q3c=q3c_new
    q4c=q4c_new
    q1c=q1c_new

    output = np.array([ra1,ra2,ra3,ra5,rb2,rb3,rb4,rb6,rc1,rc3,rc4,rc7,q2a,q3a,q1a,q3b,q4b,q2b,q3c,q4c,q1c,q5a,q6b,q7c])
    print(i)
    print(output)

