#Exercise 7: Aliasing 

#Q1. Create an alias & try changing original variable & alias

a = [0, 1, 2]

b = a 

print(a,b)

# modify b so first member of list is string 'hello'
b[0] = 'hello'

print(a,b)  # see as changed b also changed a

# append value 3 to list a 

a.append(3)
print(a,b)   #again has changed both as a & b are aliases for same list


#Q2. Try with a string

a = 'can I change'
b = a
print(a,b)

b = 'different' 
print(a,b)  # see with string only b changes- as strings are immutable. Lists are mutable so can be changed via aliasing changes

#Q3. Force 'deep copy' to avoid aliasing

a = [0,1,2]
import copy  #import copy module
b = copy.deepcopy(a)    #copy.deepcopy function 
print(a,b)
b[0] = 'hello'       # only changes b as deep copy of a made to avoid aliasing
print(a,b)
