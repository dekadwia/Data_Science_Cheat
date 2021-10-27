# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:12:17 2021

@author: Deka Dwi Abrianto
"""

#RANDOM NUMBERS 

##Random Generators
import numpy as np
np.random.seed(123)
np.random.rand()

np.random.rand()

#Coin Toss
np.random.seed(123)
coin = np.random.randint(0,2) #Randomly generate 0 or 1, 2 not included
print(coin)
if coin == 0:
    print('Heads')
else:
    print('Tails')

###Exercise 1: Random Float
#import numpy
import numpy as np
#Set the sees
np.random.seed(123)
#Generate and Print out random float
print(np.random.rand())

###Exercise 2: Roll the Dice
#Import numpy and set seed
import numpy as np
np.random.seed(123)
#Use randint to simulate the dice
print(np.random.randint(1,7))
#Use Randint again
print(np.random.randint(1,7)) #Will make a different result

###Exercise 2: Determine your next move
#Starting step
step = 50
#roll the dice
dice = np.random.randint(1,7)
#Finish the control construct
if dice <=2:
    step = step -1
elif dice <=5:
    step = step + 1
else:
    step = step + np.random.randint(1,7)
print(dice)
print(step)


#RANDOM WALK

##Heads or Tails 10 times flip
import numpy as np
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")
print(outcomes)

##Head or tails random walk
import numpy as np
np.random.seed(123)
tails = [0]
for x in range(10):
    coin = np.random.randint(0,2)
    tails.append(tails[x] + coin)
print(tails)

###Exercise 1: The next step
#Initialize random walk
random_walk = [0]
for x in range(10):
    #Set step: last element in random_walk
    step = random_walk[-1]
    #Roll the dice
    dice = np.random.randint(1,7)
    #Determine next step
    if dice  <=2:
        step = step-1
    elif dice <=5:
        step = step+1
    else:
        step = step + np.random.randint(1,7)
    #Append next step to random walk
    random_walk.append(step)
#print random walk
print(random_walk)

###Exercise 2: How Long you can go? (set the minimum value to 0)
#Initialize random walk
random_walk = [0]
for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    
    if dice <=2:
        #use max to make sure step can't go below 0
        step = max(0, step-1)
    elif dice<=5:
        step = step+1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
print(random_walk)

###Exercise 3: Visualize the walk
random_walk = [0]
for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    
    if dice <=2:
        #use max to make sure step can't go below 0
        step = max(0, step-1)
    elif dice<=5:
        step = step+1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
#Visualize random walk
import matplotlib.pyplot as plt
plt.plot(random_walk)
plt.show()


#DISTRIBUTION

##100 Runs
import numpy as np
np.random.seed(123)
final_tails = []
for x in range(100):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
print(final_tails)

#Histogram 100 runs
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails = []
for x in range(100):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
plt.hist(final_tails, bins = 10)
plt.show()

###Exercise 1: Simulate Multiple Walks
#Initialize all walks
all_walks = []
for i in range(10):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <=5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
        
    #Append random walk to all walks
    all_walks.append(random_walk)

#Print all_walks
print(all_walks)

###Exercise 2: Visualize all_walks
all_walks = []
for i in range(10):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <=5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
        
    #Append random walk to all walks
    all_walks.append(random_walk)
#Convert all walks to numpy array :np_aw
np_aw = np.array(all_walks)
#plot np_aw and show
plt.plot(np_aw)
plt.show()
#clear the figure
plt.clf()
#transpose np_aw to np_aw_t
np_aw_t = np.transpose(np_aw)
#plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

###Exercise 3: Implement Clumsiness
all_walks = []
for i in range(10):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <=5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
            
        #Implement Clumsiness
        if np.random.rand() <= 0.001:
            step = 0
            
        random_walk.append(step)
    all_walks.append(random_walk)
#Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

###Exercise 4: Plot the Distribution
all_walks = []
for i in range(10):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <=5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
            
        #Implement Clumsiness
        if np.random.rand() <= 0.001:
            step = 0
            
        random_walk.append(step)
    all_walks.append(random_walk)
#Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
#Select Last Row from np_aw_t
ends = np_aw_t[-1,:]
#plot histogram of ends
plt.hist(ends)
plt.show()