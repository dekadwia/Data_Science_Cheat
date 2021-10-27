# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 06:19:32 2021

@author: Deka Dwi Abrianto
"""

#Comaprison Operators
##Numpy recap
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight/np_height**2
bmi
bmi>23
bmi[bmi>23] #Only filter for true

##Numeric comparison
2<3 #numeric comparison
"carl" <"chris" #string comparison
3 < "chris" # Cannot compare string and numeric
3 <4.1 #only numeric and integer can compare

###exercise 1 : equality
#comparison of booleans
print(True == False)
#comparison of integers 
print(-5*15 != 75)
#comparison of strings
print("pyscript" == "PyScript")
#compare booleans with integer
print (True == 1)

###exercise 2 : Greater and less than
#comparison of integers
x = -3*6
print(x >= -10)
#comparison of stings
y = "test"
print("test" <= y)
#comparison of booleans
print(True > False)

### exercise 3: compare arrays
#create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.5])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(my_house >= 8)
print(my_house < your_house)


#Booleans Operators
##and
x = 12
x > 5 and x <15
##or
y = 5
y < 7 or y > 13
##not
not True
#logical with numpy array
np.logical_and(bmi > 21, bmi < 22 )
bmi[np.logical_and(bmi > 21, bmi < 22 )]

### exercise 1 : and or not
#define variables
my_kitchen = 18.0
your_kitchen = 14.0
print(my_kitchen > 10 and my_kitchen < 18)
print(my_kitchen < 14 or my_kitchen > 17)
print(my_kitchen*2 < your_kitchen*3)

###exercise 2: Boolean operator with numpy
my_house = np.array([18.0, 20.0, 10.75, 9.5])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(np.logical_or(my_house>18.5, my_house<10))
print(np.logical_and(my_house<11, your_house<11))


#If, elif, else
##IF
z = 4
if z%2 == 0 :
    print("Z is even")
    
##else
z = 5
if z%2 == 0 :
    print("Z is even")
else :
    print("Z is odd")
    
##elif
z = 3
if z%2 == 0 :
    print("Z is divisible by 2")
elif z%3 == 0 :
    print("Z is divisible by 3")
else :
    print("Z is not divisible by 2 and 3")
    
###Exercise 1 : IF
#Define Variables
room = "kit"
area = 14.0

if room == "kit" :
    print("looking around in the kitchen")
    
if area > 15 :
    print("big place!")

###Exercise 2 : Add Else
#Define Variables
room = "kit"
area = 14.0

if room == "kit" :
    print("looking around kitchen")
else :
    print("looking around somewhere")
    
if area > 15 :
    print("big place!")
else :
    print("pretty small")
    
###Exercise 3: customize further with elif
#define variables 
room = "bed"
area = 14.0

if room == "kit":
    print("looking around in the kitchen")
elif room == "bed":
    print("looking around in the beedroom")
else :
    print("looking around somewhere")

if area>15:
    print("big place!")
elif area>10:
    print("medium size, nice!")
else :
    print("pretty small")
    

#Filtering Pandas DataFrame
##Filtering
import pandas as pd
brics = pd.read_csv("BRICS.csv", index_col=0)
brics[brics['area'] >8]
brics[np.logical_and(brics['area'] > 8, brics['area'] <10)]

###Exercise 1: Driving Right
#Import cars data
import pandas as pd
cars = pd.read_csv('Cars.csv', index_col= 0)
cars
cars[cars['drives_right']]

###Exercise 2: Cars per Capita
cars[cars['cars_per_cap']>500]

###Exercise 3: Cars per Capita(2)
cars[np.logical_and(cars['cars_per_cap']> 100, cars['cars_per_cap']<500)]