# Exercise 2: Writing & Plotting NetDCF files

# Write a function to convert time from datafile to Python datetime object

# Imports
import time
from netCDF4 import Dataset
from datetime import datetime, timedelta
import numpy as np
from csv import reader

# Function to convert time to number format

def time_convert(tm):
    tm = datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
    return tm
  
# function to convert temps to Kelvin

def temp_convert(temp):
    temp = temp.strip("+").strip("C").lstrip("0")
    return float(temp)+273.15

# define variable for in and out files

infile = 'output.csv'
outfile = 'sensor-data.nc'


#Parse data in python lists

times = []
temps = []

# open infile and read data into lists
with open(infile, 'rt') as tsvfile:    # 'rt' read as text file
    tsvreader = reader(tsvfile, delimiter='\t')
    for row in tsvreader:
        times.append(time_convert(row[0]))
        temps.append(temp_convert(row[1]))
        
# Set reference time and convert datetime values to offset values from reference time
#reference time is the first time in the input data
base_time = times[0]
time_values = []

for t in times:
    value = t - base_time
    ts = value.total_seconds()
    time_values.append(ts)
    
    time_units = "seconds since " + base_time.strftime('%Y-%m-%d %H:%M:%S')

# define dataset to go into outfile
dataset = Dataset(outfile, "w", format='NETCDF4_CLASSIC')

# create time dimension - with unlimited length
time_dim = dataset.createDimension("time", None)

# create time varaible
time_var = dataset.createVariable("time", np.float64, ("time"))
time_var[:] = time_values
time.var.units = time_units
time.var.standard_name = "time"
time_var.calendar = "standard"

# create temp variable
temp_var = dataset.createVariable("temp", np,float64, ("temp"))
temp[:] = temps

#  Set   the   variable attributes
temp.var_id =  "temp"   
temp.long_name =  "Temperature   of sensor   (K)"  
temp.units  =  "K"   
temp.standard_name   =  "air_temperature" 
#  Set   the   global   attributes
dataset.Conventions  =  "CF-1.6" 
dataset.institution  =  "NCAS"   
dataset.title  =  "My   first CF-netCDF   file" 
dataset.history   =  "%s:  Written  with  script:  write_sensor_data_to_netcdf.py"  %  (datetime.now().strftime("%x  %X"))

# Write the file
dataset.close()

print("Wrote: %s" % output_file)
print("Try: ncdump %s" % output_file)