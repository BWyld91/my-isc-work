#Exercise 2: Interrogating and manipulating arrays
import numpy as np
# create 2D array of shape (2,4) containing 2 lists (made from range)

arr = np.array([range(4), range(10, 14)])

# print shape of array

print(arr.shape)

# print size of array

print(arr.size)

# print min & max of array

print(arr.min(),arr.max())

# print array re-shaped to (2,2,2)

print(arr.reshape(2,2,2))

# alternative

print(np.reshape(arr, (2,2,2)))

# print array transposed

print(arr.transpose())

# alternative

print(np.transpose(arr))

# print array flattened to 1D

print(arr.flatten())

# alternative

print(np.ravel(arr))

# print array converted to floats

print(arr.astype(np.float64))




