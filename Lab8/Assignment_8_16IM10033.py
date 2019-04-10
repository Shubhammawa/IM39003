#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[34]:


# Control Parameters
num_ants = 5000
num_nodes = 20
alpha = 1
beta = 1
init_pheromone = 1
evap = 0.1
pher_iter = 5


# In[35]:


cordinate_matrix = np.array([[0.0333692, 0.9925079],
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


# In[36]:


dist_matrix = np.zeros((num_nodes, num_nodes))
for i in range(num_nodes):
    for j in range(num_nodes):
        dist_matrix[i][j] = np.sqrt((np.power((cordinate_matrix[i][0] - cordinate_matrix[j][0]),2) + 
                                     (np.power((cordinate_matrix[i][1] - cordinate_matrix[j][1]),2))))


# In[37]:


tabu = np.ones((num_nodes,))
# To store the probability of each node in the tabu list. 
prob_list = {} 
cumm_list = {} 
score = {}
count = np.random.randint(0,1,(num_nodes,num_nodes))
paths = []
distances = []
best_path = []
best_distances = []
Pheromone_matrix = np.ones((num_nodes,num_nodes))


# In[38]:


def dist_calc(path,dist_matrix):
    dist = 0
    for i in range(len(path)-1):
        dist = dist + dist_matrix[path[i]][path[i+1]]
    return dist


# In[39]:


for i in range(num_ants):
    current_path = []
    
    # Initializing tabu list
    tabu = list(np.arange(num_nodes))
    
    # Random Selection of first node 
    current_path.append(np.random.randint(0,num_nodes))
    tabu.remove(current_path[0])
    path_length = 0
    
    # Iteration for one ant
    while(len(tabu) != 0):
        total_score = 0
        score = {}
        for j in tabu:
            # Computing scores for the next possible node.
            score[j] = (Pheromone_matrix[current_path[path_length]][j]*((i+1)**alpha))*((1/dist_matrix[current_path[path_length]][j])**beta)
            
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
    distances.append(dist_calc(current_path,dist_matrix))
    
    
    #print("This is current_path", current_path, "\n current distance", dist_cal(current_path,D_mat))
    for l in range(len(current_path)-1):
        Pheromone_matrix[current_path[l]][current_path[l+1]] = (1-evap)*Pheromone_matrix[current_path[l]][current_path[l+1]] +  (pher_iter)/dist_calc(current_path, dist_matrix)
        


# In[40]:


min_index = distances.index(min(distances))
print("The best path obtained is",paths[min_index])
print( "\n The minimum Distance is ", min(distances))


# In[ ]:




