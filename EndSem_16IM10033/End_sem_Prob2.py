
# coding: utf-8

# In[57]:


import numpy as np
import matplotlib.pyplot as plt


# In[58]:


def Obj(x1,x2,x3,x4,n=5):
    f = (1/6.931)-((int(x1)*int(x2))/(int(x3)*int(x4)))
    obj_func = np.power(f,2)
    return obj_func


# In[59]:


# Acceptance probability
def prob(Obj_current, Obj_new, T,k = 1):
    prob_acceptance = np.exp((-(Obj_new-Obj_current))/(k*T))
    return prob_acceptance


# In[64]:


# Cooling Schedule - Determines how rapidly T (temperature decreases)
def T_update(T):
    r = 0.9      # Can be tuned to get different results
    T = r*T
    return T


# In[65]:


def update(x,T):
    u = np.random.uniform(-1,1)
    v = np.random.uniform(-1,1)
    x_new = [0,0,0,0]
 
    x_new[0] = x[0] + u*T/50       # At lower temperatures the neighbourhood automatically becomes short          
    if(x_new[0]<=12):
        x_new[0] = 12
    elif(x_new[0]>=60):
        x_new[0] = 60
    x_new[1] = x[1] + v*T/50
    if(x_new[1]<=12):
        x_new[1] = 12
    elif(x_new[1]>=60):
        x_new[1] = 60
    x_new[2] = x[2] + v*T/50
    if(x_new[2]<=12):
        x_new[2] = 12
    elif(x_new[2]>=60):
        x_new[2] = 60
    x_new[3] = x[3] + v*T/50
    if(x_new[3]<=12):
        x_new[3] = 12
    elif(x_new[3]>=60):
        x_new[3] = 60
    Obj_current = Obj(x[0],x[1],x[2],x[3])
    Obj_new = Obj(x_new[0],x_new[1],x_new[2],x_new[3])

# Directly accpeting
    if(Obj_new<Obj_current):
        x[0] = x_new[0]
        x[1] = x_new[1]
        x[2] = x_new[2]
        x[3] = x_new[3]
        Obj_current = Obj_new
        return [x,Obj_current]
    else:
# Accepting with a probability
        p0 = 0.99                # Tuning
        if(prob(Obj_current,Obj_new,T)> p0):
            x[0] = x_new[0]
            x[1] = x_new[1]
            x[2] = x_new[2]
            x[3] = x_new[3]
            Obj_current = Obj_new
            return [x,Obj_current]
        
        else:
            return [x,Obj_current]


# In[66]:


# Parameters
T = 1000
T_final = 1
x = [10,30,10,30]
n = 0
nt = 30
obj = Obj(x[0],x[1],x[2],x[3])
i = 0
OBJ = []
while(T>T_final):
    while(n<nt):
        result = update(x,T)
        x,obj = result
        n = n + 1
    T = T_update(T)
    n = 0
    i+=1
    OBJ.append(obj)
    if(i%5==0):
        print("Objective value after iteration " + str(i) + " = " + str(obj))
        print("x = ",x)
        print("\n")
#plt.plot(OBJ)

