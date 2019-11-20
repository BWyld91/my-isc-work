#Exercise 5: Input & output

#Q1. Read entire contents of csv file and print each line to screen

with open('weather.csv', 'r') as reader:
    data = reader.read()
    print(data)
  

#Q2. Read line by line

with open('weather.csv', 'r') as reader:
    data = reader.readline()
    while data != '':
        print(data)
        data = reader.readline()
    print("It's over") 
  
#Q3. Use a for loop. Get just rainfall values.

with open('weather.csv', 'r') as reader:
    data = reader.readlines()
    linecount = 0 
    rain = []
    
 
    
    for line in data:
        linecount +=1
        
        if linecount != 1:
            raincol = line.strip().split(",")[-1] # split at commas(",") [-1] take last section. line.strip() removes \n white space
            raincol = float(raincol) #turns into float value 
            rain.append(raincol) #adds rain col value to list 'rain'
        
    print(rain)
    
    with open('raindata.csv', 'w') as writer:
        for raincol in rain:
            writer.write(str(raincol) + "\n")
            
#Q4. Writing & reading binary data

import struct #import 'struct' module

bin_data = struct.pack("bbbb", 123, 12, 45, 34) #struct.pack to pack the list into 4 bytes

with open('mybinary.dat', 'wb') as bwriter: #open and write new file as binary writer (bw)
    bwriter.write(bin_data) #write variable bin_data to file
    
with open('mybinary.dat', 'rb') as breader: #'rb' indicates read in binary mode
     bin_data2 = breader.read() #reads file above in variable 'bin_data2'
     print(bin_data2)
     
#Unpack binary data in bin_data2 unsing struct.unpack

data = struct.unpack("bbbb", bin_data2)
print(data)
    


    
        
        
      
	

