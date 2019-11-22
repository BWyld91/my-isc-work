# Exercise 3: Array calculations and operations

#Q1 Array calculations

import numpy as np 

# create 2D array of shape (2, 4) containing 2 lists:
# (range(4), range(10, 14)) and assign to variable a

a = np.array([range(4), range(10, 14)])

# create array from list

b = np.array([2, -1, 1, 0])

# multiply a * b


#print(a*b) #multiplies each row of a by b as arrays different shapes

# multiply b by 100

b1 = b*100

# multiply b by 100.0

b2 = b*100.0

# are these the same? True

#print(b1 == b2)

# why do they look different. Interrogate typecodes to find out why.

#print(b1.dtype, b2.dtype)



#Q2 array comparisons

# create array 0 to 9

arr = np.arange(10)

# print 2 ways to show where in array elements are less than 3

#print(arr < 3)

#print(np.less(arr, 3))

# create numpy condition where 'arr' < 3 OR > 8

condition = np.logical_or(arr < 3, arr > 8)

# create new array where arr value * 5 is condition is true and arr * -5 if false

arr2 = np.where(condition, arr * 5, arr * -5)
#print(arr2)


#Q3. Implement mathematical function that works on arrays

# define a function to take 2D array of horizontal zonal wind components (u)
# and 2D horizontal meridional wind components (v) and returns an array
# of magnitudes of total wind (w).
# include a test for overall magnitude.
# if < 0.1 set to 0.1 
# return array must be same size and shape as input arrays

def calc_w(v, u, min = 0.1): #required arguments
    w = ((v ** 2) + (u ** 2)) ** 0.5
    output = np.where(w > min, w, min)
    return output 
  
u = np.array([[4, 5, 6], [2, 3, 4]]) 
v = np.array([[2, 2, 2,], [1, 1, 1]]) 

print(calc_w(v, u, 0.1)