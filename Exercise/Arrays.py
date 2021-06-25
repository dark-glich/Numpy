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

# Write a NumPy program to create a 2d array with 1 on the border and 0 inside.
array = np.ones((5,5))
z = np.zeros((3,3))
array[1:-1, 1:-1] = z
print(array)

# Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.
array = np.zeros((8,8))
array[1::2, ::2] = 1
array[::2,1::2] = 1
print(array)

# Write a NumPy program to convert a tuple into arrays.
tuple = (1,2,3,4,5)
array = np.array(tuple)
print(array)

# Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees.
c = np.array([0, 12, 45.21 ,34, 99.91])
c = ((c * 9/5) + 32)
print(c)

# Write a NumPy program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements.
array = np.arange(1,10)
print(array.size, array.itemsize, array.nbytes)

# Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
array1 = np.array([1,4,10,14])
array2 = np.array([1,10])
print(np.in1d(array1, array2))

# Write a NumPy program to find common values between two arrays.
array1 = np.array([1,4,5,8])
array2 = np.array([1,5])
print(np.intersect1d(array1, array2))

# Write a NumPy program to get the unique elements of an array.
array = np.array([1,21,2,1,34,1,3,21])
print(np.unique(array))

# Write a NumPy program to construct an array by repeating.
array = np.array([1,2,3])
print(np.hstack((array, array)))

# Write a NumPy program to repeat elements of an array. 
array = np.repeat([1,2,3], 2)
print(array)

# Write a NumPy program to find the indices of the maximum and minimum values of an array. 
array = np.array([[1,2,3],[2,4,5]])
print(array.max())
print(array.min())

# Write a NumPy program compare two given arrays.
n = np.array([2,4])
m = np.array([3,1])
print(np.greater(n,m))
print(np.less(n,m))

# Write a NumPy program to get the values of the elements that are bigger than 10 in a given array.
array = np.arange(1,20)
array = array[array > 10]
print(array)

# Write a NumPy program to create a new array of 3*5, filled with 2. 
array = np.full((3,5), 2)
print(array)

#Write a NumPy program to create an array of 10's with the same shape and type of a given array.
x = np.array([10.2,15,20,25])
y = np.full_like(x, 10)
print(y)