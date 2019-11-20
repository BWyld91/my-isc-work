# Exercise 4: Tuples

#Q1

t = (1,) #comma at end for tuple of single value

print(t[0])

tu = range(100,201) #Creates variable 'tu' range 100-200

tup = tuple(tu) #converts variable 'tu' to a tuple

#print first and last values of tuple
print(tup[0])
print(tup[-1])

#Q2 step through items in a list and print count (index) for each one.

mylist = [23, 'hi', 2.4e-10]

for (i, item) in enumerate(mylist):
    print(i, item)
    
#Q3 Unpack mulitple values from tuple

first, middle, last = mylist #assigns each value of tuple mylist to variable on left
print(first, middle, last) # prints values
middle, last, first = first, middle, last # reassigns values to those on left
print(first, middle, last)
