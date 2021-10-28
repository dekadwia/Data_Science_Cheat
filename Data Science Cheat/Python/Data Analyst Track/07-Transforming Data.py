# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 06:21:46 2021

@author: Deka Dwi Abrianto
"""

#INTRODUCING TO DATAFRMAES

##Exploring a DataFrame
dogs.head() #To see first 5 rows
dogs.info() #To see dataframe column and missing value
dogs.shape #To see the dimension of dataframe, how much row and column
dogs.describe() #Compute some summary statistics like mean, median
dogs.values #to see values of the data in 2D numpy array
dogs.columns #to see name of column
dogs.index #to see index number of column

###Inspecting a DataFrame
import pandas as pd
homeless = pd.read_csv('homelessness.csv', index_col = 0)
#Print head of data
print(homeless.head())
#Print information about data
print(homeless.info())
#Print the shape of data
print(homeless.shape)
#Print the description of data
print(homeless.describe())

###Exercise 2: Parts of the DataFrame
#print the values of data
print(homeless.values)
#print the nama column of data
print(homeless.columns)
#print row index of data
print(homeless.index)


#SORTING AND SUBSETTING

##Create Data
dict = {'name': ['Stella', 'Cooper', 'Bella', 'Charlie', 'Lucy', 'Max', 'Bernie'],
        'breed': ['Chihuahua', 'Schnauzer', 'Labrador', 'Poodle', 'Chow Chow', 'Labrador', 'St. Bernard'],
        'color': ['Tan', 'Grey', 'Brown', 'Black', 'Brown', 'Black', 'White'],
        'height_cm': [18, 49, 56, 43, 46, 59, 77],
        'weight_kg': [2, 17, 24, 24, 24, 29, 74],
        'date_of_birth': ['2015-04-20', '2011-12-11', '2013-07-01', '2016-09-16', '2014-08-25', '2017-01-20', '2018-02-27']
        }
import pandas as pd
dogs = pd.DataFrame(dict)
##Sorting
dogs.sort_values('weight_kg')

##Sorting in descending order
dogs.sort_values('weight_kg', ascending = False)

##Sorting by multiple variables
dogs.sort_values(['height_cm', 'weight_kg'])

##Sorting by multiple variables and sort by mix descending and ascending order
dogs.sort_values(['weight_kg', 'height_cm'], ascending=[True, False])

##Subsetting Columns
dogs.name
dogs['name']

##Subsetting multiple columns
dogs[['breed', 'height_cm']]

##Subsetting rows
dogs[dogs['height_cm']> 50]

##Subsetting based on text data
dogs[dogs['breed']== 'Labrador']

##Subsetting based on dates
dogs[dogs['date_of_birth']> '2015-01-01']

##Subsetting based on multiple conditions
is_lab = dogs['breed'] == 'Labrador'
is_brown = dogs['color'] == 'Brown'
dogs[is_lab & is_brown]

##Subsetting based on multiple column in 1 row
dogs[(dogs['breed']=='Labrador') & (dogs['color'] == 'Brown')]

##Subsetting using .isin()
dogs[dogs['color'].isin(['Black', 'Brown'])]

###Exercise 1: Sorting Rows
homeless_ind = homeless.sort_values('individuals')
print(homeless_ind.head())
#sort by descending family members
homeless.sort_values('family_members', ascending = False)
#Sort by region, then descending family members
homeless.sort_values(['region', 'family_members'], ascending = [False, True])

###Exercise 2: Subsetting Columns
#Select individuals column
homeless['individuals']
#Select the state and family members
homeless[['state', 'family_members']]
#Select only individuals and state columnn only
homeless[['individuals', 'state']]

###Exercise 3: Subesetting Rows
#Filter for rows where individuals is greater than 10000
homeless[homeless['individuals']>10000]
#Filter for rows where region is mountain
homeless[homeless['region']=='Mountain']
#Filter for rows where family members is less than 1000 and region is pacific
homeless[(homeless['family_members']< 1000) & (homeless['region']=='Pacific')]

###Exercise 4: Subsetting rows by categorical variables
#Subset for rows in south atlantic or mid atlantic regions
homeless[homeless['region'].isin(['South Atlantic', 'Mid-Atlantic'])]
#Atau bisa juga dengan
homeless[(homeless['region'] == 'South Atlantic') | (homeless['region'] == 'Mid-Atlantic')]
#Filter for rows in Mojave Desert States
homeless[homeless['state'].isin(['California', 'Arizona', 'Nevada', 'Utah'])]


#NEW COLUMNS

##Adding a New Column
dogs['height_m'] = dogs['height_cm']/100
dogs['bmi'] = dogs['weight_kg'] / dogs['height_m']**2
##Multiple Manipulation
bmi_under_100 = dogs[dogs['bmi']<100]
bmi_sort = bmi_under_100.sort_values('height_cm', ascending = False)
bmi_sort[['name', 'height_cm', 'bmi']]

###Exercise 1: Adding new column
#Add total column of individulas and family members
homeless['total'] = homeless['individuals'] + homeless['family_members']
#Add p_individuals col as proportion of individuals
homeless['p_individuals'] = homeless['individuals']/homeless['total']
print(homeless)

###Exercise 2: Combo Attack
#create indiv_per_10k col as homeless individuals per 10k state pop
homeless['indiv_per_10k'] = 10000 * homeless['individuals'] / homeless['state_pop']
#Subset rows for indiv_per_10k greater than 20
high_homeless = homeless[homeless['indiv_per_10k']>20]
#sort high homeless by descending indiv_per_10k
high_homeless_sort = high_homeless.sort_values('indiv_per_10k', ascending = False)
#Select only state and indiv_per_10k
high_homeless_sort[['state', 'indiv_per_10k']]