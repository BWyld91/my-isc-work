#Exercise 8: Functions

#Q1. Create a simple function

# define function 'double_it'

def double_it(number):
    return number * 2 

# if pass string will give string twice

#Q2. Pythagoras function

# define function called 'calc_hypo' which requires 2 arguments (a & b)

def calc_hypo(a,b):
    hypo = ((a**2)+(b**2))**1/2
    return hypo
  
print(calc_hypo(3, 4))

#Q3. Improve above function by putting checks in code


def calc_hypo(a,b):
    
    # ensure all inputs are 'float' & 'int' 
    if type(a) not in (int, float) or type(b) not in (int, float):
        print('a and b cannot be string')
        return False
    # ensure only none zero values entered
    elif a <= 0 or b <= 0:
        print('a and b must be greater than zero')
        return False
    else:
        hypo = ((a**2)+(b**2))**1/2
        return hypo
        

      
print(calc_hypo(1,2))

print(calc_hypo(9.9, 'length'))

print(calc_hypo(2,0))