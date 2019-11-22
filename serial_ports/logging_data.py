# Logging data from serial ports

# import serial & datetime & io modules

import serial

import io
from datetime import datetime


# open serial port with appropriate parameters

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)

# prints to screen instant temperature reading with datetime stamp

#print(datetime.utcnow().isoformat(), ser.read(size=8))
#ser.close()  #closes serial connection after that one reading


# create while loop to print data to screen until 5 measurements are taken


#count = 0

#while count < 5:
#    datastring = ser.read(size=8) # sets reading to a variable
#    print(datetime.utcnow().isoformat(), datastring)
#    count +=1 

#ser.close()

# Rewrite above code to use readline() to output file

# set output file

output = '/home/user01/my-isc-work/serial_ports/output.tsv'

sio = io.TextIOWrapper(
    io.BufferedRWPair(ser, ser, 1),
    encoding='ascii', newline='\r'
)

with open(output, 'a') as f: #appends to existing file
      while ser.isOpen():    #logs while serial port open
          datastring = sio.readline()
          # \t adds tab between date and datastring \n adds new line after each reading
          f.write(datetime.utcnow().isoformat() +'\t' + datastring + '\n')
          f.flush() #forces to write to file after each reading rather than when got a few
          
ser.close()

