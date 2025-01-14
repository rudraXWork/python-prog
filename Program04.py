# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:45:16 2024

@author: srikantap
"""

import pandas as pd

# read titanic data set using pandas
df = pd.read_csv('titanic.csv')


# select Age, Fare and Pclass attributes from the dataset
ageFarePclass = df.loc[:,['Age', 'Fare', 'Pclass']]

# print head information of ageFarePclass
print(ageFarePclass.head())

# Print all information of ageFarePclass
print(ageFarePclass)

# Drop rows with missing values in selected columns
ageFarePclass_cleaned = ageFarePclass.dropna()

# print ageFarePclass_cleaned
print(ageFarePclass_cleaned)

covariance_matrix = ageFarePclass_cleaned.cov()

print("covariance matrix : ", covariance_matrix)

correlation_mtx = ageFarePclass_cleaned.corr()
print(correlation_mtx)
