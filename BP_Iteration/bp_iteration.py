# Import the packages
import numpy as np
import math

#
# If we have a 3*3 Grid Graph with Uniform Factors like below:
#      O---O---O           X1--X2--X3   
#      |   |   |           |   |   |
#      O---O---O           X4--X5--X6
#      |   |   |           |   |   |
#      O---O---O           X7--X8--X9
# Then we can do label these points from left to right, from up to down.
#
phi_ij = np.array([])
phi_i = np.array([])
for theta in np.array([0,0.2,0.6]):
    for j in np.arange(-2.0,2.0,0.2):
        phi_ij = np.append(phi_ij,math.exp(j))
        phi_i = np.append(phi_i,math.exp(theta)) 
phi_ij = phi_ij.reshape(3,-1)
phi_i = phi_i.reshape(3,-1)

# Initalization the message and define the structure of the graph
num_nodes = 9
num_edges = 12
num_states = 2
messages_positive = np.ones(2 * num_edges) * (0.3)
messages_passive = 1-messages_positive
'''
messages table
0 -> 12 | 6 -> 25 | 12 -> 56 | 18 -> 69
1 -> 21 | 7 -> 52 | 13 -> 65 | 19 -> 96
2 -> 23 | 8 -> 36 | 14 -> 47 | 20 -> 78
3 -> 32 | 9 -> 63 | 15 -> 74 | 21 -> 87
4 -> 14 | 10 ->45 | 16 -> 58 | 22 -> 89
5 -> 41 | 11 ->54 | 17 -> 85 | 23 -> 98
'''

# Define adjancy table
def adjancy(messages):
    adjancy_message = np.array([
                            messages[5],
                            messages[3]*messages[7],
                            messages[0]*messages[7],
                            messages[9],
                            messages[1],
                            messages[11]*messages[15],
                            messages[0]*messages[3],
                            messages[10]*messages[13]*messages[17],
                            messages[2],
                            messages[12]*messages[19],
                            messages[4]*messages[15],
                            messages[6]*messages[13],messages[17],
                            messages[6]*messages[10]*messages[17],
                            messages[19]*messages[8],
                            messages[4]*messages[15],
                            messages[21],
                            messages[6]*messages[10]*messages[13],
                            messages[20]*messages[23],
                            messages[12]*messages[8],
                            messages[22],
                            messages[14],
                            messages[16]*messages[23],
                            messages[18]
                            ])
    return adjancy_message

# Belief Propagation algorithm
def belief_propagation(iteration):
    for iter in range(iteration):
        adjancy_p_message = adjancy(messages_positive)
        adjancy_passive_message = adjancy(messages_passive)
        for edge in range(num_edges*2):
            messages_positive[edge] = (1/phi_i[0][0])*(1/phi_ij[0][0])*adjancy_passive_message[edge] + phi_i[0][0]*phi_ij[0][0]*adjancy_p_message[edge]
            messages_passive[edge] = phi_ij[0][0]*(1/phi_i[0][0])*adjancy_passive_message[edge] + (1/phi_ij[0][0])*(phi_i[0][0])*adjancy_p_message[edge]
            # To normalized the messages
            messages_positive[edge] = messages_positive[edge]/(messages_positive[edge] + messages_passive[edge])
            messages_passive[edge] = 1 - messages_positive[edge]
    print(messages_positive)
    return messages_positive

belief_propagation(10)