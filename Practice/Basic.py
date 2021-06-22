import numpy as np
"""
Numpy array vs list :
Numpy arrays are better than normal list as they take up less space are
much faster than list they can also be used higher math functions
which are not possible using list.
"""
# Numpy Array 
vector = np.array([1,2,3], dtype='int16')
metrix = np.array([[1,2.0,3],[4,5,6]])

# gives the structure of the array
print(f"metrix.shape = {metrix.shape} ") # (2, 3)

# gives the number of element in array 
print(f"metrix.size = {metrix.size}") # 6

# gives the type of the value of array
print(f"vector.dtype = {vector.dtype} ") # int16

# gives the amount of bytes taken by each element of the array
print(f"vector.itemsize = {vector.itemsize} ") # 2 bytes

# gives the total amount of bytes taken by array
print(f"vector.nbytes = {vector.nbytes} ") # 6 bytes

# Changing and Accessing elements

array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(f"array = {array}")

# Accessing & changing a specific element
print(f"array[1,1] = {array[1,-1]} ") # 7
array[1,1] = 77

# Getting a specific row 
print(f"array[0, :] = {array[0, :]}") # [1 2 3 4 5]
array[0, :] = [11,22,33, 44, 55]

# Getting a secific column
print(f"array[:, 2] = {array[:, 2]}") # [3, 8]
array[:, 2] = [3, 88]

# Accessing a secific part
print(f"array[0, 1:-1:2] = {array[0, 1:-1:2]}") # [2 4]

# Initializing different types of array

# Creates a array full of zeroes 
zero_array = np.zeros((3,3)) # np.zeros(shape)

# Create a array full of ones
ones_array = np.ones((2,2)) 

# Create a array full of a specific value
value_array = np.full((2,3), 2) # np.full(shape, value)

# Random decimal array
decimal_array = np.random.rand((3))

# Random integer array 
int_array = np.random.randint(4,10, size=(2,2)) # np.random.randint(min,max,size)
print(int_array)

# identity array => create a matrix with same number of columns & rows
identity_array = np.identity(4) # np.identity(row/column)
