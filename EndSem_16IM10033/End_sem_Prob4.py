
# coding: utf-8

# In[48]:


# Shubham Mawa
# 16IM10033


# In[49]:


import numpy as np


# In[50]:


def fitness(x1,x2,n=5):
    f = 28*x1 + 21*x2 + 0.25*x2*x2
    p1 = np.zeros((n))
    p2 = np.zeros((n))
    p3 = np.zeros((n))
    p4 = np.zeros((n))
    for i in range(0,n):
        if((x1[i] + x2[i])>1000):
            p1[i] = 999*(x1[i]+x2[i]-1000)
        else:
            p1[i] = 0

        if((0.5*x1[i] + 0.4*x2[i])>500):
            p2[i] = 999*(0.5*x1[i] + 0.4*x2[i]-500)
        else:
            p2[i] = 0

        if(x1[i]<0):
            p3[i] = 999*(-x1[i])
        else:
            p3[i] = 0

        if(x2[i]<0):
            p4[i] = 999*(-x2[i])
        else:
            p4[i] = 0
    
    obj_func = f - p1 -p2 - p3 - p4
    
    return obj_func
    #return fitness          # 


# In[82]:


# Control parameters
W = 0.7
C1 = 0.8
C2 = 0.8
#n = 10
num_iters = 30
r1 = np.random.uniform(size=(2,5))
r2 = np.random.uniform(size=(2,5))


# In[83]:


# Initialization of Swarm Particles
CP = 700*(r1)
V = r2
LBP = CP
CF = fitness(CP[0],CP[1])
LBF = CF
GBF = np.amax(LBF)
GBP = np.amax(LBP,axis=1)
print(GBP)


# In[84]:


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
    LBF = np.maximum(CF,LBF)
    GBF = np.amax(LBF)
    index = np.argmax(LBF)
    for j in range(0,LBP.shape[0]):
        if(LBF[j]==CF[j]):
            LBP = CP
    GBP = np.amax(LBP,axis=1)
    print("GBP: ",GBP)
    print("Global Best Fitness: ",GBF)
    print("\n")

