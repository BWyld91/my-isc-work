# Exercise 2: Multiple axes & multiple graphs


# Q1

import numpy as np
import matplotlib.pyplot as plt

# define data

time = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

## Plot CO2 and Temp against time on same plot ## 

# allows subplotting by axis  

fig, ax1 = plt.subplots()

# create first plot usinf ax1 instead of plt

ax1.plot(time, co2, 'r--')
ax1.set_ylabel('CO2 concentration (ppm)', color='r')
ax2 = ax1.twinx()     # get 2nd axis with twin x axis
ax2.plot(time, temp, 'g-')
ax2.set_ylabel('Temperature (oC)', color='g')
plt.xlabel('Time (decades)')
plt.title('Temperature and CO2 concentration versus time')
plt.show()

## Plot as 3 graphs side by side on single page ##
## ie sub plotting ##

# select first plot in a 3,1 layout

plt.subplot(1, 3, 1)
plt.plot(range(0, 10, 1), 'y-')
plt.title('Plot 1')
plt.ylabel('Y- axis')

# select second plot

plt.subplot(1, 3, 2)
plt.plot(range(10, 0, -1), 'ko-', markeredgecolor='r')
plt.title('Plot 2')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

# select 3rd plot

plt.subplot(1, 3, 3)
y = [4]*10
plt.plot(y, 'g--')

plt.show()


