# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:33:05 2024

@author: srikantap
"""

# Find mean median and mode of an array
import numpy as np

arr = np.array([34, 76, 12, 58, 93])

# calculate mean of array
mean = np.mean(arr)
print("Mean : ", mean)          # Output: 

# Calculate median 
median = np.median(arr)
print("Median : ", median)


values, counts = np.unique(arr, return_counts=True)
mode_index = np.argmax(counts)
mode_value = values[mode_index]

# Print the result
print(f"Mode: {mode_value}")


# Or using scipy library 
from scipy import stats

# Calculate mode
mode_value = stats.mode(arr)

print("Mode : ",mode_value)