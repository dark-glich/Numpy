import numpy as np

# Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.
list = [12.23, 13.32, 100, 36.32]
array = np.array(list)
print(array)

# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10. 
array = np.arange(2,11).reshape((3,3))
print(array)

# Write a NumPy program to create a null vector of size 10 and update sixth value to 11.
array = np.zeros((10))
array[5] = 11
print(array)

# Write a NumPy program to create an array with values ranging from 12 to 38.
array = np.arange(12,39)
print(array)

# Write a NumPy program to reverse an array 
array = np.array([1,2,4,5,6,7,8,9])
array = array[::-1]
print(array)

# Write a NumPy program to convert an array to a float type.
array = np.array([10, 20, 30])
array.dtype = 'float64'
print(array.dtype)

# 