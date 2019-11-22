# Exercise 4: Missing values (using masks)

# Q1. Create a masked array and manipulate

# import numpy and its mask module

import numpy as np
import numpy.ma as MA

# create a masked array

marr = MA.masked_array(range(10), fill_value = -999)

# prints array and fill value

print(marr, marr.fill_value)

# mask 3rd value using MA.masked

marr[2]=MA.masked

print(marr) # will show 3rd value masked






