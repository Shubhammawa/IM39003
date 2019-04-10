
############################################################
############ ANT COLONY OPTIMIZATION #######################
############ SUBMITTED BY: PRERIT JAIN ( 16IM10035) ########
############################################################


import numpy as np
import math

# Defining the Parameters needed in the Algorithm
# Number of nodes in the network
n_nodes = 20
# Weights of pheremone and visibility
alpha = 1
beta = 1
# Initial Pheremone
phe_init = 1
# Number of ants
n_ants = 1000
# Evaporation coffecient
evap = 0.1
# Pheremone spreaded by
pher_iter = 5

coo_matrix = np.array([[0.0333692, 0.9925079],
[0.6020896, 0.0168807],
[0.1532083, 0.7020444],
[0.3181124, 0.1469288],
[0.1878440, 0.8679120],
[0.9786112, 0.4925364],
[0.7918010, 0.7943144],
[0.5145329, 0.0363478],
[0.5500754, 0.8324617],
[0.3893757, 0.6635483],
[0.9641841, 0.6400201],
[0.7718126, 0.5463923],
[0.7549037, 0.4584584],
[0.2837881, 0.7733415],
[0.3308411, 0.1974851],
[0.7977221, 0.1193149],
[0.3221207, 0.7930478],
[0.9201035, 0.1186234],
[0.2397964, 0.1448552],
[0.3967470, 0.6716172]])

# Computing the distances from the coordinates
D_mat = np.zeros((n_nodes, n_nodes))
for i in range(n_nodes):
    for j in range(n_nodes):
        D_mat[i][j] = np.sqrt(((coo_matrix[i][0] - coo_matrix[j][0])**2) + ((coo_matrix[i][1] - coo_matrix[j][1])**2)) 

# Maintaining a TABU list consisting of the index available for travelling 
tabu = np.ones((n_nodes,))
# To store the probability of each node in the tabu list. 
prob_list = {} 
cumm_list = {} 
score = {}
count = np.random.randint(0,1,(n_nodes,n_nodes))
paths = []
distances = []
best_path = []
best_distances = []

# Initializing the Pheremone Matrix
Pher_mat = np.ones((n_nodes,n_nodes))

for i in range(n_ants):
    current_path = []
    
    # Initializing tabu list with all the nodes available.
    tabu = list(np.arange(n_nodes))
    
    # Random Selection of first index. 
    current_path.append(np.random.randint(0,n_nodes))
    tabu.remove(current_path[0])
    path_length = 0
    
    # The path selection for one ant
    while(len(tabu) != 0):
        total_score = 0
        score = {}
        for j in tabu:
            # Computing scores for the next possible node.
            score[j] = (Pher_mat[current_path[path_length]][j]*((i+1)**alpha))*((1/D_mat[current_path[path_length]][j])**beta)
            total_score = total_score + score[j]

        flag = 0
        prob_list = {}
        cumm_list = {}
        
        # Calucating the probabilities and cummulative probabilities of respective possible edges
        for k in (tabu):
            if(flag == 0):
                prob_list[k] = score[k]/total_score
                cumm_list[k] = score[k]/total_score
                prev = k
                flag = flag +1
            else:
                prob_list[k] = score[k]/total_score
                cumm_list[k] = score[k]/total_score + cumm_list[prev]
                prev = k
        
        # Performing Roulette Wheel Selection for the next node.
        r = np.random.uniform(0,1)
        
        if(len(tabu) != 1):
            for k in range(len(tabu)-1):
                if(k==0):
                    if(r < cumm_list[tabu[k]]): 
                        current_path.append(tabu[k])
                        tabu.remove(tabu[k])
                        count[current_path[path_length]][current_path[path_length + 1]] = (count[current_path[path_length]][current_path[path_length + 1]] + 1)
                        path_length = path_length + 1
                        
                else:
                    if(r >= cumm_list[tabu[k]] and r < cumm_list[tabu[k+1]]):
                        current_path.append(tabu[k+1])
                        tabu.remove(tabu[k+1])
                        count[current_path[path_length]][current_path[path_length + 1]] = (count[current_path[path_length]][current_path[path_length + 1]] + 1)
                        path_length = path_length + 1
                        
        else:
            current_path.append(tabu[0])
            tabu.remove(tabu[0])
            count[current_path[path_length]][current_path[path_length + 1]] = (count[current_path[path_length]][current_path[path_length + 1]] + 1)
            path_length = path_length + 1
            
    paths.append(current_path)
    distances.append(dist_cal(current_path,D_mat))
    
    
    #print("This is current_path", current_path, "\n current distance", dist_cal(current_path,D_mat))
    for l in range(len(current_path)-1):
        Pher_mat[current_path[l]][current_path[l+1]] = (1-evap)*Pher_mat[current_path[l]][current_path[l+1]] +  (pher_iter)/dist_cal(current_path, D_mat)
    #print(np.max(Pher_mat))

min_index = distances.index(min(distances))
print("The best path found is",paths[min_index])
print( "\n And the minimum Distance is ", min(distances))



