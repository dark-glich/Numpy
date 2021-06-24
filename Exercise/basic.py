import numpy as np

array = np.array([0,1,2,3,4])
print(f"array = {array}")
# get the numpy version and show numpy build configuration.
print(f"version = {np.version}")
print(np.show_config())

# test whether none of the elements of a given array is zero.
print(array.all())

# test whether none of the elements of a given array is non-zero.
print(array.any())

# create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.
x = np.array([1,7,13,105])
print(x.nbytes)

# Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.
x = np.zeros((5))
y = np.ones((5))
z = np.full(5,(5))
print(np.concatenate((x,y,z)))

# Write a NumPy program to create an array of the integers from 30 to70.
v = np.arange(30, 71)
print(v)

# Write a NumPy program to create an array of the integers from 30 to70.
v = np.arange(30, 71)
v = v[v % 2 == 0]
print(v)

# Write a NumPy program to create a 3x3 identity matrix.
i = np.identity(3)
print(i)

# Write a NumPy program to generate a random number between 0 and 1.
r = np.random.rand((1))
print(r)

# Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
v = np.linspace(5,50,10)
print(v)

# Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
r = np.random.randint(0, 10, size=(5))
print(r)

# Write a NumPy program to multiply the values of two given vectors.
vect1 = np.array([2,4,6,8,10])
vect2 = np.array([1,3,5,7,9])
print(vect1 * vect2)

# Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
p = np.arange(10, 22)
p = p.reshape((3,4))
print(p)

# Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 0, and inside 1.
z = np.zeros((10,10))
o = np.ones((8,8))
z[1:-1, 1:-1] = o
print(z)

# Write a NumPy program to create a 5x5 matrix with 6 & elements on the main diagonal equal to 1, 2, 3, 4, 5.
s= np.full((5,5), 6)
d = np.diag([1-6,2-6,3-6,4-6,5-6])
print(s+d)

# Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
r = np.random.random((3,3,3))
print(r)

# Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array.
array = np.array([[10,20],[30,40]])
print(array.sum())
print(array.sum(axis=0))
print(array.sum(axis=1))

# Write a NumPy program to compute the inner product of two given vectors.
x = np.array([2, 4])
y = np.array([1, 3])
print(np.dot(x,y))

# Multiply two given arrays of same size element-by-element
x = np.array([1,5,7,8,2])
y = np.array([4,7,3,6,4])
print(x*y)

# Write a NumPy program to create an array of equal shape and data type of a given array.
ex = np.array([[1,5],[8,2]])
a = np.zeros_like(ex)
print(a.dtype, a.shape)
