# Exercise 1: Getting started with Matplotlib


# Q1

# import packages

import matplotlib.pyplot as plt
import numpy as np

#  plot line defined by range(10) and display

#plt.plot(range(10))
#plt.show()

# note you can zoom in on data on plot and pan around
# saves each window view as a plot to click through

# Q2

# define variables for input
time = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]

plt.plot(time, co2, 'b--')
plt.title('Concentration of CO2 versus time')
plt.ylabel('CO2 concentration (ppm)')
plt.xlabel('Time (decade)')
plt.show()

# add additional line to plot but same experiement variables

# define additional data
co22 = [260, 275, 290, 255, 295, 310, 375]


plt.plot(time, co2, 'b--')
plt.plot(time, co22, 'g-') # just define another plot line
plt.title('Concentration of CO2 versus time')
plt.ylabel('CO2 concentration (ppm)')
plt.xlabel('Time (decade)')
plt.show()



