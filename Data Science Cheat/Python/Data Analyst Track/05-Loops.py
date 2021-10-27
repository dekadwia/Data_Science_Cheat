# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:29:07 2021

@author: Deka Dwi Abrianto
"""

#WHILE LOOP

error = 50
while error > 1:
    print(error)
    error = error/4
    
###Exercise 1: Basic While Loop
#Initialize Offset
offset = 8
#Code the while loop
while offset != 0 :
    print("Correcting...")
    print(offset)
    offset = offset -1
###Exercise 2: Add Conditionals
offset = -6 
while offset != 0:
    print("correcting...")
    if offset >0 :
        offset = offset - 1
    else :
        offset = offset + 1
    print(offset)


#FOR LOOP

fam = [1.73, 1.68, 1.71, 1.89]
for a in fam :
    print(a)
#Update for loop with index
for index, height in enumerate(fam) :
    print("index " + str(index) + ": " + str(height))
    
##Loop over string
for c in "family" :
    print(c.capitalize())

###Exercise 1: Loop over the list
areas = [11.25, 18, 20,10.75, 9.5]
for wide in areas :
    print(wide)
    
###Exercise 2: Indexes and Values
for index, wide in enumerate(areas) :
    print("room" + str(index) + ":" + str(wide))

###Exercise 3: Indexes and Values(2)
for index, wide in enumerate(areas) :
    print("room" + str(index+1) + ":" + str(wide))
    
###Exercise 4: Loop over list 
#House list of list
house = [["hallway", 11.25],
         ["kitchen", 18],
         ["living room", 20],
         ["bedroom", 10.75],
         ["bathroom", 9.5]]
for x in house: 
    print("the " + x[0] + " is " + str(x[1]) + " sqm")
    
    
# LOOP DATA STRUCTERS PART 1

##Loop over dictionaries
world = {"afghanistan" : 30.55,
         "albania" : 2.77,
         "algeria" : 39.21}
for key, value in world.items() :
    print(key + " -- " + str(value))
    
##Loop in Numpy Array
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight/np_height **2
for val in bmi :
    print(val)

##Loop in 2D Numpy Array
meas = np.array([np_height, np_weight])
for val in meas:
    print(val)

##Loop in 2D Numpy Array in 1 row
for val in np.nditer(meas) :
    print(val)
    
###Exercise 1: Loop over dictionaries
europe = {'spain' : 'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo',
          'italy':'rome', 'poland':'warsaw', 'austria':'vienna'}
for key, value in europe.items():
    print('the capital of ' + key + ' is ' +value)
    

#LOOP DATA STRUCTURES PART 2

##looping using pandas with iterrows
import pandas as pd
brics = pd.read_csv('BRICS.csv', index_col = 0)
for lab, row in brics.iterrows():
    print(lab)
    print(row)
    
##Selective Print
for lab, row in brics.iterrows():
    print(lab + ": " + row['capital'] )
    
##Add column using for loop 
for lab, row in brics.iterrows():
    brics.loc[lab, "name_length"] = len(row['country'])
print(brics)

##To add new column, using apply is more efficient than using loop
brics['name_length'] = brics['country'].apply(len)
print(brics)

###Exercise 1: Loop over DataFrame(1)
#Import cars data
import pandas as pd
cars = pd.read_csv('Cars.csv', index_col =0)
#Iterate over rows of cars
for a, row in cars.iterrows():
    print(a)
    print(row)
    
###Exercise 2: Add Column using for loop
for lab, row in cars.iterrows():
    cars.loc[lab, 'Country'] = row['country'].upper()
print(cars)

###Exercise 3: Add column using apply
for lab, row in cars.iterrows():
    cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)