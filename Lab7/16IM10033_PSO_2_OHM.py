
# coding: utf-8

# In[71]:


# Shubham Mawa
# 16IM10033


# In[72]:


import numpy as np


# In[73]:


def fitness(x1,x2,n=5):
    sum1 = 0
    sum2 = 0
    for i in range(1,n+1):
        sum1+= i*np.cos((i+1)*x1 + i)
        sum2+= i*np.cos((i+1)*x2 + i)
    obj_func = sum1*sum2
    fitness = 1/(1 + obj_func)
    return obj_func
    #return fitness          # 


# In[74]:


# Control parameters
W = 0.7
C1 = 0.3
C2 = 0.6
n = 10
num_iters = 10
r1 = np.random.uniform(size=(2,5))
r2 = np.random.uniform(size=(2,5))


# In[75]:


# Initialization of Swarm Particles
CP = 255*(r1)
V = r2
LBP = CP
CF = fitness(CP[0],CP[1])
LBF = CF
GBF = np.amax(LBF)
GBP = np.amax(LBP,axis=1)
print(GBP)


# In[76]:


#PSO

# Block 1 - To be used if using fitness function (objective function can't be directly used as it is a minimization problem.)
# for i in range(0,num_iters):
#     V = W*V + C1*((np.random.uniform(size=(2,5)))*(LBP-CP)) + C2*((np.random.uniform(size=(2,5)))*((np.resize(GBP,(2,5)))-CP))
#     CP = CP + V
#     CF = fitness(CP[0],CP[1])
#     LBF = np.maximum(CF,LBF)
#     GBF = np.amax(LBF)
#     index = np.argmax(LBF)
#     for j in range(0,LBP.shape[0]):
#         if(LBF[j]==CF[j]):
#             LBP = CP
#     GBP = np.amax(LBP,axis=1)
#     print("GBP: ",GBP)
#     print("Global Best Fitness: ",GBF)
#     print("\n")

# Block 2 - To be used if using objective function minimization directly
for i in range(0,num_iters):
    V = W*V + C1*((np.random.uniform(size=(2,5)))*(LBP-CP)) + C2*((np.random.uniform(size=(2,5)))*((np.resize(GBP,(2,5)))-CP))
    CP = CP + V
    CF = fitness(CP[0],CP[1])
    LBF = np.minimum(CF,LBF)
    GBF = np.amin(LBF)
    index = np.argmin(LBF)
    for j in range(0,LBP.shape[0]):
        if(LBF[j]==CF[j]):
            LBP = CP
    GBP = np.amin(LBP,axis=1)
    print("GBP: ",GBP)
    print("Global Best Fitness: ",GBF)
    print("\n")

