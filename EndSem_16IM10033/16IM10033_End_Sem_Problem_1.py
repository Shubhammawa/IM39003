
# coding: utf-8

# In[113]:


# Shubham Mawa
# 16IM10033
import numpy as np


# In[114]:


def fitness(x1,x2,x3,x4,x5,n=5):
    f = 5.3578547*np.multiply(x3,x3) + 0.8356891*np.multiply(x1,x5) + 37.293239*(x1) - 40792.141
    g1 = 85.334407 + 0.0056858*np.multiply(x2,x5) + 0.00026*np.multiply(x1,x4) - 0.0022053*np.multiply(x3,x5)
    g2 = 80.51249 + 0.0071317*np.multiply(x2,x5) + 0.0029955*np.multiply(x1,x2) + 0.00218138*np.multiply(x3,x3)
    g3 = 9.300961 + 0.0047026*np.multiply(x3,x5) + 0.0012547*np.multiply(x1,x3) + 0.0019085*np.multiply(x3,x4)
    
    p1 = np.zeros((n))
    p2 = np.zeros((n))
    p3 = np.zeros((n))
    p4 = np.zeros((n))
    p5 = np.zeros((n))
    p6 = np.zeros((n))
    p7 = np.zeros((n))
    p8 = np.zeros((n))
    
    for i in range(0,n):
        if(g1[i]<0):
            p1[i] = 999*(-g1[i])
        elif(g1[i]>92):
            p1[i] = 999*(g1[i]-92)
        else:
            p1[i] = 0

        if(g2[i]<90):
            p2[i] = 999*(90-g2[i])
        elif(g2[i]>110):
            p2[i] = 999*(g2[i]-110)
        else:
            p2[i] = 0

        if(g3[i]<20):
            p3[i] = 999*(20-g3[i])
        elif(g3[i]>25):
            p3[i] = 999*(g3[i]-25)
        else:
            p3[i] = 0

        if(x1[i]<78):
            p4[i] = 999*(78-x1[i])
        elif(x1[i]>102):
            p4[i] = 999*(x1[i]-102)
        else:
            p4[i] = 0

        if(x2[i]<33):
            p5[i] = 999*(33-x1[i])
        elif(x2[i]>45):
            p5[i] = 999*(x1[i]-45)
        else:
            p5[i] = 0

        if(x3[i]<27):
            p6[i] = 999*(27-x3[i])
        elif(x3[i]>45):
            p6[i] = 999*(x3[i]-45)
        else:
            p6[i] = 0

        if(x4[i]<27):
            p7[i] = 999*(27-x4[i])
        elif(x4[i]>45):
            p7[i] = 999*(x4[i]-45)
        else:
            p7[i] = 0

        if(x5[i]<27):
            p8[i] = 999*(27-x5[i])
        elif(x5[i]>45):
            p8[i] = 999*(x5[i]-45)
        else:
            p8[i] = 0
    
    
    L = f + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
    
    return L


# In[115]:


# Control parameters
W = 0.7
C1 = 0.3
C2 = 0.6
n = 10
num_iters = 10
r1 = np.random.uniform(size=(5,5))
r2 = np.random.uniform(size=(5,5))


# In[118]:


# Initialization of Swarm Particles
CP = 50*(r1)
print(CP)
V = r2
LBP = CP
CF = fitness(CP[0],CP[1],CP[2],CP[3],CP[4])
LBF = CF
GBF = np.amin(LBF)
GBP = np.amax(LBP,axis=1)
print(GBP)
#print(LBF)


# In[117]:


for i in range(0,num_iters):
    V = W*V + C1*((np.random.uniform(size=(5,5)))*(LBP-CP)) + C2*((np.random.uniform(size=(5,5)))*((np.resize(GBP,(5,5)))-CP))
    CP = CP + V
    CF = fitness(CP[0],CP[1],CP[2],CP[3],CP[4])
    LBF = np.minimum(CF,LBF)
    GBF = np.amin(LBF)
    index = np.argmin(LBF)
    for j in range(0,LBP.shape[0]):
        if(LBF[j]==CF[j]):
            LBP = CP
    GBP = np.amin(LBP,axis=1)
    print("GBP: ",GBP)
    GB_obj = fitness(GBP[0],GBP[1],GBP[2],GBP[3],GBP[4])
    print("Global Best Fitness: ",GBF)
    print("Objective value: ",GB_obj)
    print("\n")

