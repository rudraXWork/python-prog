# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:44:09 2024

@author: srikantap
"""

import numpy as np

# Example 3x3 matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calculate covariance matrix
cov_matrix = np.cov(matrix, rowvar=False)

# Print the covariance matrix
print("Covariance Matrix:")
print(cov_matrix)

# Calculate correlation matrix
corr_matrix = np.corrcoef(matrix, rowvar=False)

# Print the correlation matrix
print("\nCorrelation Matrix:")
print(corr_matrix)

# Generate a random 3x3 matrix with integer values between 10 and 99
random_matrix_int = np.random.randint(10, 99, size=(3, 3))

# Print the random integer matrix
print("Random 3x3 Matrix with Integers:")
print(random_matrix_int)

# Calculate covariance of random matrix
cov_r_mtx = np.cov(random_matrix_int, rowvar=False)

#Print the covariance of random matrix
print("\n  covariance of random matrix : ")
print(cov_r_mtx)

# Calculate correlation of random matrix
corr_r_mtx = np.corrcoef(cov_r_mtx, rowvar = False)
print("\n Correlation of random matrix :")
print(corr_r_mtx)


