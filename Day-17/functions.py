"""
A function is a reusable block of code that performs a specific task.
Functions help us avoid repeating code and make programs easier to read,
test, and maintain.

"""


# Basic syntax:
# def function_name(parameters):
#     statements
#     return result

''' 

def gst(price):
    print("Original Price: ",price)
    print("Final Price: ", price + price*0.18)
gst(1000)
gst(5000)
gst(800)
gst(10000)

'''
'''

def table(n):
    print(f"{n}-Table")
    print("===========================================")
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

for i in range(1,21):
    table(i)

'''

"""
def isleap(Year):
    if Year % 400 == 0 or (Year % 4 == 0 and Year % 100 != 0):
        return 'Leap Year'
    else:
        return 'Not l.y'


print(isleap(2012))
print(isleap(2013))
print(isleap(2014))
print(isleap(2020))

"""

'''
def isprime(Number):
    if Number < 2:
        return 'Not Prime'
    for i in range(2, Number):
        if Number % i == 0:
            return 'Not Prime'
    return 'Prime'


print(isprime(2))
print(isprime(7))
print(isprime(10))
print(isprime(13))


'''
'''
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
display("PEPAKAYALA TEJA","pepakayalasaitejakumar@gmail.com","P.Teja@123456789")
display("pepakayalasaitejakumar@gmail.com","P.Teja@123456789","P.Teja@123456789")
display("P.Teja@123456789","pepakayalasaitejakumar@gmail.com","PEPAKAYALA TEJA9")

def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display(name="PEPAKAYALA TEJA",email="pepakayalasaitejakumar@gmail.com",pwd="P.Teja@123456789")
display(email="pepakayalasaitejakumar@gmail.com",pwd="P.Teja@123456789",pwd="P.Teja@123456789")
display(pwd="P.Teja@123456789",email="pepakayalasaitejakumar@gmail.com",name="PEPAKAYALA TEJA9")

def display(name,email,pwd=None):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display("PEPAKAYALA TEJA","pepakayalasaitejakumar@gmail.com","P.Teja@123456789")
display("pepakayalasaitejakumar@gmail.com","PEPAKAYALA TEJA")
'''
