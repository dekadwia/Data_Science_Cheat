# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 06:50:43 2021

@author: Deka Dwi Abrianto
"""
#MATPLOTLIB
##BASIC PLOT WITH MATPLOTLIB
##LINE PLOT
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2519, 3692, 5263, 6972]
plt.plot(year, pop)
plt.show()

##SCATTER PLOT
year = [1950, 1970, 1990, 2010]
pop = [2519, 3692, 5263, 6972]
plt.scatter(year, pop)
plt.show()

###EXERCISE 1 
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Population.csv")
plt.plot(data['year'], data['population'])
plt.show()

###EXERCISE 2 LINE PLOT
plt.plot(data['gdp_cap'], data['life_exp'])
plt.show()

###EXERCISE 3 SCATTER PLOT
plt.scatter(data['gdp_cap'], data['life_exp'])
plt.xscale('log') #Put the x axis on logaritmic scale
plt.show()

###EXERCISE 4 SCATTER PLOT (2)
plt.scatter(data['population'], data['life_exp'])
plt.show()



##HISTOGRAM
##HISTOGRAM EXAMPLE
values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins =3)
plt.show()

###EXERCISE 1 BUILD A HISTOGRAM
plt.hist(data['life_exp'])
plt.show()

###EXERCISE 2 BUILD A HISTOGRAM(2) SETTING BINS
plt.hist(data['life_exp'], bins = 5) # for bins 5
plt.show()
plt.clf() # to clean up plot

plt.hist(data['life_exp'], bins = 20) #for bins 20
plt.show()
plt.clf()



##CUSTOMIZATION
##ADD AXIS LABEL
year = [1950, 1970, 1990, 2010]
pop = [2519, 3692, 5263, 6972]

#To Add More Data
year = [1800, 1850, 1900] + year
pop = [1000, 1262, 1650] + pop

plt.plot(year, pop)
plt.xlabel('year')
plt.ylabel('Population')
plt.title('World Population Projection')
plt.yticks([0, 1000, 2000, 3000, 4000, 5000, 6000, 7000],
           ['0','1000M','2000M','3000M','4000M','5000M','6000M','7000M'])
plt.show()

###EXERCISE 1: LABELS
plt.scatter(data['gdp_cap'], data['life_exp'])
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in Years]')
plt.title('World Development in 2007')
plt.show()

###EXERCISE 2: TICKS
plt.scatter(data['gdp_cap'], data['life_exp'])
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in Years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],
           ['1k', '10k', '100k'])
plt.show()

###EXERCISE 3: SIZES (bug)
import numpy as np
np_pop = np.array(data['population'])
np_pop = np_pop*2 #bug
plt.scatter(data['gdp_cap'], data['life_exp'], s = np_pop)
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in Years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],
           ['1k', '10k', '100k'])
plt.show()

###EXERCISE 4: COLORS (bug)
col = {
       'Asia' : 'red',
       'Europe' : 'green',
       'Africa' : 'blue',
       'Americas' : 'yellow',
       'Oceania' : 'red'} #bug
plt.scatter(x = data['gdp_cap'], y = data['life_exp'], 
            s = np.array(data['population'])*2, c = col, alpha = 0.8)
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in Years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],
           ['1k', '10k', '100k'])
plt.show()

###EXERCISE 5: ADDITIONAL CUSTOMIZATIONS (bug)
plt.scatter(x = data['gdp_cap'], y = data['life_exp'], 
            s = np.array(data['population'])*2, c = col, alpha = 0.8) #bug in col
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in Years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],
           ['1k', '10k', '100k'])
#Additional Customization text
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
#Add Gridline
plt.grid(True)
plt.show()


#Dictionaries and Pandas
##Dictionaries
world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
world["albania"]

###Using index not Dictionaries
countries = ["spain", "france", "germany", "norway"]
capital = ["madrid", "paris", "berlin", "oslo"]
index_germany = countries.index("germany")
print(capital[index_germany])

###Create Dictionaries and Access Dictionaries
europe = {"spain":"madrid", "france":"paris", "germany":"berlin", "norway":"oslo"}
print(europe)
print(europe.keys())
print(europe["spain"])

##Dictionaries part 2
'''Dictionaries are imutable and must unique. if there are 2 values, they will be match with the last one'''

#Add data to the dictionaries
world['sealand'] = 0.000027
world
'sealand' in world # To check is sealand is on dictionaris or not
world['sealand'] = 0.000028 #To update data
world
del(world['sealand']) #to delete the data
world

###Dictionaries Manipulation (1)
europe['italy'] ='rome'
europe['poland'] ='warsawa'
europe
#to assert italy and poland is in database
print('italy' in europe)
print('poland' in europe)

### Dictionaries in dictionaries
euro = {"spain": {'capital':'madrid', 'population':46.77},
        'france': {'capital':'paris', 'population':66.03},
        'germany': {'capital':'berlin', 'population':80.62},
        'norway' : {'capital':'oslo', 'population':5.084}}
print(euro['france']['population'])
print(euro['france'])
print(euro['france']['capital'])
#Create sub dictionaries data
euro['italy'] = {'capital':'rome', 'population':59.83}
euro

##Pandas Part 1
dict = {'country': ["Brazil", 'Russia', 'India', 'China', 'South Africa'],
        'capital': ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
        'area' : [8.516, 17.10, 3.286, 9.597, 1.221],
        'population': [200.4, 143.5, 1252, 1357, 52.98]}
#change to DataFrame using pandas
import pandas as pd
brics = pd.DataFrame(dict)
brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]
brics

#read data from CSV
brics = pd.read_csv('brics.csv', index_col = 0)
brics

###Dictionaries to DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
import pandas as pd
my_dict = {'country' : names, 'drives_right': dr, 'cars_per_cap':cpc}
cars = pd.DataFrame(my_dict)
print(cars)
cars
#Define the row label
cars.index = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars

##Pandas Part 2
#Column Access
import pandas as pd
brics = pd.read_csv('brics.csv', index_col= 0)
brics
brics['country']
#Check type of the data
type(brics['country'])
#Make type data to be dataframe
brics[['country']]
type(brics[['country']])
#Select 2 Column
brics[['country', 'capital']]
#Row Access
brics[1:4]
#Row Access with loc
brics.loc['RU']
#Row access with loc transform it to DataFrame
brics.loc[['RU']]
#Aceess more than 1
brics.loc[['RU', 'CH', 'IN']]
#Row and Column slicing with loc
brics.loc[['RU', 'IN', 'CH'], ['country', 'capital']]
#select all rows but only select 2 column
brics.loc[:, ['country', 'capital']]
#Row access using iloc
brics.iloc[[1]]
brics.iloc[[1,2,3]]
brics.iloc[[1,2,3], [0,1]]
brics.iloc[:, [0,1]]

###Exercise : Square Brackets
#read the data
cars = pd.read_csv('Cars.csv')
cars['country']
cars[['country']]
cars
cars[['country', 'drives_right']]

###exercise : square brackets (2)
cars = pd.read_csv('Cars.csv', index_col=0)
cars[0:4]
cars[3:6]

###exercise 3 : loc and iloc
print(cars.loc['JAP'])
print(cars.iloc[2])
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1,6]])

###Exercise 4 : loc and iloc (2)
cars.loc['MOR','drives_right']
cars.loc[['RU', 'MOR'], ['country', 'drives_right']]

####Exercise 5 : loc and iloc (3)
cars.loc[:, 'drives_right'] #As Series
cars.loc[:, ['drives_right']] #As DataFrame
cars.loc[:, ['drives_right', 'cars_per_cap']]
