
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def Obj_func(x1,x2,n=5):
    sum1 = 0
    sum2 = 0
    for i in range(1,n+1):
        sum1+= i*np.cos((i+1)*x1 + i)
        sum2+= i*np.cos((i+1)*x2 + i)
    obj_func = sum1*sum2
    return obj_func


# In[3]:


def fitness(obj_func):
    '''Fitness function in a minimization problem'''
    fitness = 1/(1+obj_func)
    return fitness


# In[4]:


def init_population(pop_size=50, encoding_size=16):
    '''Generates initial population of population size pop_size
    where each chromosome is a binary string of size encoding_size'''
    
    # First 8 bits represent X1, next 8 bits represent X2
    x = []
    for i in range(0,pop_size):
        x.append(np.random.randint(2, size=encoding_size))
    x = np.array(x)
    return x


# In[5]:


# Sample population of size 3
x = init_population(pop_size=50)
print(x[0])
print(x.shape[0])


# In[6]:


def decoding(x):
    '''Binary to decimal conversion'''
#     x1 = []
#     x2 = []
#     for i in range(0,x.shape[0]):
#         temp1 = 0
#         for j in range(0,int((x.shape[1])/2)):
#             temp1+= np.power(2,(((x.shape[1])/2) -j-1))*x[i][j]
#         x1.append(temp1)
        
#         temp2 = 0
#         for k in range(int((x.shape[1])/2),int(x.shape[1])):
#             #print(k)
#             #print(x[i][k])
#             temp2+= np.power(2,(((x.shape[1])) -k-1))*x[i][k]
#         #print("")
#         x2.append(temp2)
#     x_dec = [x1,x2]
#     x_dec = np.array(x_dec)
#     return x_dec
    x1 = 0
    x2 = 0
    temp1 = 0
    for j in range(0,int((x.shape[0])/2)):
        temp1+= np.power(2,(((x.shape[0])/2) -j-1))*x[j]
    x1 = temp1
        
    temp2 = 0
    for k in range(int((x.shape[0])/2),int(x.shape[0])):
        temp2+= np.power(2,(((x.shape[0])) -k-1))*x[k]
    x2 = temp2
    x_dec = [x1,x2]
    x_dec = np.array(x_dec)
    return x_dec


# In[7]:


#print(x)
print(x[-1])
print(x.shape)


# In[8]:


x_dec = decoding(x[-1])
print(x_dec)
#print(x_dec[:,0])


# In[9]:


def tournament_selection(x):
    '''Selection operator'''
    mating_pool = []
    for i in range(0,x.shape[0]):
        player1 = x[int(np.random.rand(1)*x.shape[0]),:]
        player2 = x[int(np.random.rand(1)*x.shape[0]),:]
        
        p1_x1, p1_x2 = decoding(player1)
        p2_x1, p2_x2 = decoding(player2)
        if(Obj_func(p1_x1,p1_x2,5)<Obj_func(p2_x1,p2_x2,5)):
            mating_pool.append(player1)
        else:
            mating_pool.append(player2)
    return np.array(mating_pool)


# In[10]:


mating_pool = tournament_selection(x)
print(mating_pool.shape)
print(mating_pool[0])


# In[11]:


def crossover(chromosome_1, chromosome_2):
    '''Two point crossover operator'''
    p1 = int(np.random.rand(1)*chromosome_1.shape[0])
    p2 = int(np.random.rand(1)*chromosome_2.shape[0])
    
    for i in range(p1,p2):
        temp = chromosome_1[i]
        chromosome_1[i] = chromosome_2[i]
        chromosome_2[i] = temp
    return [chromosome_1,chromosome_2]


# In[12]:


def mutation(x, P_m = 0.2):
    '''Bit flip mutation operator'''
    for i in range(0,x.shape[0]):
        for j in range(0,x.shape[1]):
            rand_num = np.random.uniform()
            if(rand_num<P_m):
                if(x[i][j]==0):
                    x[i][j]==1
                elif(x[i][j]==1):
                    x[i][j]==0
    return x


# In[13]:


print(int((np.random.rand(1))*x.shape[0]))


# In[14]:


def GA(P_c=0.8):
    x = init_population()
    x_dec = decoding(x)
    mating_pool = tournament_selection(x)
    new_mating_pool = []
    #Crossover
    # To be carried out on 80% of the chromosomes
    num_crossovers = int(x.shape[0]*P_c)
    for i in range(0,num_crossovers,2):
        #print(i)
        new_C1, new_C2 = crossover(mating_pool[i],mating_pool[i+1])
        new_mating_pool.append(new_C1)
        new_mating_pool.append(new_C2)
    for i in range(0,x.shape[0]-num_crossovers):
        new_mating_pool.append(mating_pool[i])
    
    new_x = mutation(np.array(new_mating_pool))
    
    obj_func = []
    for i in range(0,new_x.shape[0]):
        x1, x2 = decoding(new_x)
        obj_func.append(Obj_func(x1,x2,5))
        #obj_func.append(Obj_func(x2))
    print("Min function value: ",np.min(obj_func))
    


# In[17]:


num_iter = 50
for i in range(0,num_iter):
    GA()

