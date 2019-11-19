# Exercise 2 Control Flow

# Q1: While loops. NOTE: colon after while statement

var = 3

while var >= 5:
    print('never ending')






# Q2: Create variable assigned to list

gases = ['He', 'Ne', 'Ar', 'Kr']

count = 0 

while count < 4:
    item = gases[count]
    print(item,count)
    count += 1


# Q3: if/elif/else

name = 'Bart' 

if name == 'Lisa':
    print(name +' plays saxophone')

elif name == 'Bart':
    print(name +' rides skateboard')

else:
    print(name +' lives in Springfield')

# Q4: truth testing

x = 1

if x:
    print(x, ' is True')

a = 22.1 
b = 'hello' 
c = [1,2]
d = 0
e = 0.0
f = None
g = False
h = ''
i = ()
j = {}
k = []

if a:
    print(a, ' is True')

if b:
    print(b, ' is True')

if c:
    print(c, ' is True')

if d:
    print(d, ' is True')
else:
    print(d, ' is not True')

if e:
    print(e, ' is True')

if f:
    print(f, ' is True')
else:
    print(f, ' is not True')

if g:
    print(g, ' is True')

if h:
    print(h, ' is True')
else:
    print(h, ' is not True')

if i:
    print(i, ' is True')
else:
    print(i, ' is not True')

if j:
    print(j, ' is True')
else:
    print(j, ' is not True')

if k:
    print(k, ' is True')
else:
    print(k, ' is not True')








