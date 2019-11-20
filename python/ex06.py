#Exercise 6: Strings

#Q1 Loop through a string as a sequence

# create string variable 's'

s = 'I love to write python'

# loop through and display each element

for i in s:
  print(i)
  
# print 5th element/ last element/ length of 's'

print(s[4])
print(s[-1])
print(len(s))

#Q2 Split a string and loop through words rather than characters

s = 'I love to write python'

# split into words. ie by spaces

split_s = s.split(' ')
print(split_s)

# loop through words and look for 'i'
for word in split_s:
    if word.find('i') >-1:  #tells has to find find i at index of 0 or above in word to print 
        print(f'I found "i" in {word} ')

# does same thing     
for word2 in split_s:
    if 'i' in word2:
        print(f'i in {word2}')
        
#Q3 

something = 'Completely Different'

number_t = something.count('t') # counts 't' in string
print(number_t)

plete = something.rindex('plete') #index where sub-string 'plete' starts
plete

# or alternatively
something.find('plete')

# replace Different with Silly
thing2 = something.replace('Different', 'Silly') 

# note doing this WONT do a replace C with B as strings are immutable
something[0] = 'B'




