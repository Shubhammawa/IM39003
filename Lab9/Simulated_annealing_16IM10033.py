
# coding: utf-8

# In[103]:


import numpy as np


# In[104]:


def Obj(x1,x2,n=5):
    sum1 = 0
    sum2 = 0
    for i in range(1,n+1):
        sum1+= i*np.cos((i+1)*x1 + i)
        sum2+= i*np.cos((i+1)*x2 + i)
    obj_func = sum1*sum2
    return obj_func


# In[105]:


# Acceptance probability
def prob(Obj_current, Obj_new, T,k = 1):
    prob_acceptance = np.exp((-(Obj_new-Obj_current))/(k*T))
    return prob_acceptance


# In[106]:


# Cooling Schedule - Determines how rapidly T (temperature decreases)
def T_update(T):
    r = 0.9      # Can be tuned to get different results
    T = r*T
    return T


# In[107]:


def update(x,T):
    u = np.random.uniform(-1,1)
    v = np.random.uniform(-1,1)
    x_new = [0,0]
 
    x_new[0] = x[0] + u*T/50       # At lower temperatures the neighbourhood automatically becomes short          
    x_new[1] = x[1] + v*T/50

    Obj_current = Obj(x[0],x[1])
    Obj_new = Obj(x_new[0],x_new[1])

# Directly accpeting
    if(Obj_new<Obj_current):
        x[0] = x_new[0]
        x[1] = x_new[1]
        Obj_current = Obj_new
        return [x,Obj_current]
    else:
# Accepting with a probability
        p0 = 0.9                # Tuning
        if(prob(Obj_current,Obj_new,T)> p0):
            x[0] = x_new[0]
            x[1] = x_new[1]
            Obj_current = Obj_new
            return [x,Obj_current]
        
        else:
            return [x,Obj_current]


# In[114]:


# Parameters
T = 1000
T_final = 1
x = [4,5]
n = 0
nt = 10
obj = Obj(x[0],x[1])
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
plt.plot(OBJ)

