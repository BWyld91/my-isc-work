#Exercise 1: Intro to NumPy arrays

# import numpy as alias np 
import numpy as np

# create list of values from 1 to 10
x = list(range(1,11))

# create np integer array from list 'x'. 1st argument= data, 2nd argument = data type

a1 = np.array(x, dtype=np.int32)

# creay array of floats from list 'x'

a2 = np.array(x, dtype=np.float64)

# print d types using dtype attribute
#print(a1.dtype)
#print(a2.dtype)

# create array of zeros with shape (2,3,4)

z1 = np.zeros((2,3,4))

# create array of 1s with shape (2,3,4)

o1 = np.ones((2,3,4))

# create array with values 0 to 999 

a3 = np.arange(1000)

# create array with values 4 to 10

a4 = np.arange(4,11)


# create araay with values 4 to 20 in steps of 4 

a5 = np.arange(4,21,4)

#Q3. Indexing and slicing arrays

# create 2D array from list and assign to variable a

a = np.array([[2, 2.3, 5.5, -6.4, -2.2, 2.4],[1, 22, 4, 0.1, 5.3, -9],[3, 1, 2.1, 21, 1.1, -2]])

