# Exercise 3: Lists and slicing

# Q1: selecting from and slicing simple list

x = [1, 2, 3, 4, 5]
print(x[1])
print(x[-2])
print(x[:]) #whole list by slice
print(x[1:4]) #2nd to 4th item by slice

# Q2: create list from range

y = list(range(1,11))
print(y)

y[0] = 10 #Replaces first value (index 0) to 10
print(y)


y.append(11) #Append value in brackets to list y
print(y)


y.extend([12, 13, 14]) #Extends list y by adding another list 
print(y)

#Q3: lists & loops

forward = []
backward = []

values = ['a', 'b', 'c']

for i in values:
    forward.append(i)
    backward.insert(0, i) #inserts each i at front of list (ie index 0)
    
print(forward)
print(backward)

forward.reverse()
print(forward)
print(backward)

#Q4

countries = ['uk', 'usa', 'uk', 'uae']
dir(countries) #displays properties and methods of the list
help(countries.count) # prints documentation about count method to screen
countries.count('uk') #counts how many times 'uk' appears in list countries









