# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 04:30:10 2021

@author: Deka Dwi Abrianto
"""

#CARA MEMBACA DATA MENGGUNAKAN PANDAS
##Membaca file menggunakan pandas
import pandas as pd
csv_data = pd.read_csv("shopping_data.csv")
print(csv_data)

##Membaca file dengan menggunakan head(): Melihat 5 Data pertama
import pandas as pd
csv_data = pd.read_csv("shopping_data.csv")
print(csv_data.head())

##Melakukan akses data kolom
import pandas as pd
csv_data=pd.read_csv("shopping_data.csv")
print(csv_data['Age']) #Mengakses kolom age

##Melakukan akses data melalui baris
import pandas as pd
csv_data = pd.read_csv("shopping_data.csv")
print(csv_data.iloc[5]) #mengakses baris ke 5

##Meenampilkan suatu data dari baris dan kolom tertentu
import pandas as pd 
csv_data = pd.read_csv("shopping_data.csv")
print(csv_data['Age'].iloc[1])
print("Cuplikan Dataset:")
print(csv_data.head())

##Menampilkan data dalam range tertentu
import pandas as pd
csv_data = pd.read_csv("shopping_data.csv")
print("Menampilkan data ke 5 sampai kurang dari 10 dalam satu baris:")
print(csv_data.iloc[5:10])

##Menampilkan informasi statistik dengan numpy
import pandas as pd
csv_data = pd.read_csv("shopping_data.csv")
print(csv_data.describe(exclude=['O'])) #akan mengabaikan data non numeical


#DATA MISSING HINGGA NORMALISASI DATA
##Melakukan pengecekan terhadapa nilai NULL yang ada
import pandas as pd
csv_data = pd.read_csv("shopping_data_missingvalue.csv")
print(csv_data.isnull().values.any())

##Mengisi missing value dengan mean()
import pandas as pd

csv_data = pd.read_csv("shopping_data_missingvalue.csv")
print(csv_data.mean())
print("Dataset yang masih terdapat nilai kosong ! :")
print(csv_data.head(10))

csv_data=csv_data.fillna(csv_data.mean())
print("Dataset yang sudah diproses Handling Missing Values dengan Mean :")
print(csv_data.head(10))

##Mengisi missing value dengan median()
import pandas as pd
csv_data = pd.read_csv("shopping_data_missingvalue.csv")
print("Dataset yang masih terdapat nilai kosong ! :")
print(csv_data.head(10))

csv_data=csv_data.fillna(csv_data.median())
print("Dataset yang sudah diproses Handling Missing Values dengan Median :")
print(csv_data.head(10))

##Praktek normalisasi data dengan menggunakan scikit learn pada python
import pandas as pd
import numpy as np
from sklearn import preprocessing

csv_data = pd.read_csv("shopping_data.csv")
array = csv_data.values
X = array[:,2:5] #memisahkan fitur dari dataset
Y = array[:,0:1] #memisahkan class dari dataset
dataset=pd.DataFrame({'Customer ID':array[:,0],'Gender':array[:,1],'Age':array[:,2],'Income':array[:,3],'Spending Score':array[:,4]})
print("dataset sebelum dinormalisasi :")
print(dataset.head(10))
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0,1)) #inisialisasi normalisasi MinMax
data = min_max_scaler.fit_transform(X) #transformasi MinMax untuk fitur
dataset = pd.DataFrame({'Age':data[:,0],'Income':data[:,1],'Spending Score':data[:,2],'Customer ID':array[:,0],'Gender':array[:,1]})
print("dataset setelah dinormalisasi :")
print(dataset.head(10))