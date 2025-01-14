# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:54:03 2024

@author: srikantap
"""


import pandas as pd


# Reading data from a CSV file into a DataFrame
df = pd.read_csv('titanic.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Show all attributes 
all_attr = dir(df)
# print(all_attr)


# print all the columns header name
col_header = df.columns
print(col_header)

# print column attribute name as list
col_header_list = df.columns.tolist()
print("col_header_list  : ",col_header_list)

# print age header
print("age hader : \n", df['Age'].head())

# Average of age
mean_age = df['Age'].mean()
print("Mean age : ", mean_age)

# Mode of age
mode_age = df['Age'].mode()
print("Mode of age :", mode_age)        # if the data has multiple modes than it will show them all 
                                        # Here only one mode present

# Median of age
median_age = df['Age'].median()
print("Median of age : ", median_age)


# Covariance between Age and Survived
covariance_Age_Survived = df['Age'].cov(df['Survived'])
print("Covariance : ", covariance_Age_Survived)         # Output: Covariance :  -0.5512
# The -ve covariance suggests that variable increases, the other variable tends to decrease

# Covariance between Pclass and Fare
covariance_Pclass_Fare = df['Pclass'].cov(df['Fare'])
print("Covariance between Pclass and Fare : ", covariance_Pclass_Fare)  
# Output: Covariance between Pclass and Fare :  -22.830196170065197
# As the class increases the fare decreases


# Correlation between Age and Survived
correlation_Age_Survived = df['Age'].corr(df['Survived'])
print("Correlation : ", correlation_Age_Survived)         # Output: Correlation :  -0.07722109457217763
# The -ve Correlation suggests that variable increases, the other variable tends to decrease

# Correlation between Pclass and Fare
correlation_Pclass_Fare = df['Pclass'].corr(df['Fare'])
print("Correlationbetween Pclass and Fare : ", correlation_Pclass_Fare)  
# Output: Correlationbetween Pclass and Fare :  -0.5494996199439072
# As the class increases the fare decreases
