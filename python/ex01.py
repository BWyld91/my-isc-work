# Exercise 1- The basics- variables & types

# Set variables (Pythagoras example)

b = 2
c = 3

a=((b**2)+(c**2))**(1/2)

# Type of variables
print(type(a))

# a is a float, to change to an integer

a = int(a)

#Check changed
print(type(a))

# Won't convert integers as strings eg

print(a + ' squared equals '+ b +' squared + '+ c + ' squared.') #Will give error

#Use str() fucntion to print an integer variable as a string
print(str(a) + ' squared equals '+str(b) +' squared + '+ str(c) + ' squared.')
3 squared equals 2 squared + 3 squared.



