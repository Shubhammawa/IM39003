
# coding: utf-8

# In[112]:


# Shubham Mawa
# 16IM10033


# In[113]:


import numpy as np


# In[114]:


def fitness(x):
    return (np.ones(5)-x*x+2*x)


# In[115]:


# Control parameters
W = 0.7
C1 = 0.2
C2 = 0.6
n = 10
num_iters = 10
r1 = np.random.uniform(size=5)
r2 = np.random.uniform(size=5)


# In[116]:


# Initialization of Swarm Particles
CP = 3*(r1)
V = r2-0.5
LBP = CP
CF = fitness(CP)
LBF = CF
GBF = np.amax(LBF)
GBP = np.amax(LBP)


# In[117]:


#PSO
for i in range(0,num_iters):
    V = W*V + C1*((np.random.uniform(size=5))*(LBP-CP)) + C2*((np.random.uniform(size=5))*(GBP-CP))
    CP = CP + V
    CF = fitness(CP)
    LBF = np.maximum(CF,LBF)
    GBF = np.amax(LBF)
    index = np.argmax(LBF)
    for j in range(0,LBP.shape[0]):
        if(LBF[j]==CF[j]):
            LBP = CP
    GBP = np.amax(LBP)
    print("GBP: ",GBP)
    print("GBF: ",GBF)
    print("\n")

