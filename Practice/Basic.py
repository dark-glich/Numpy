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

