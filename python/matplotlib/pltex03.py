# Exercise 3 Basemap

from example_code.map_data import *
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# top import will ensure following variables exist in local scope
# tas (temp), lons, lats


# create figure

fig = plt.figure()

# set up Basemap instance with regular lat/lon coord ref system
m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90,
	    llcrnrlon=-180, urcrnrlon=180, resolution='c')

# add coastlines
m.drawcoastlines()

# create 'Jet' colourmap 

