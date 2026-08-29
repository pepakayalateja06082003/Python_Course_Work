'''
def display():
    print("Inside function:",n)
n=10
display()
print("Outside function",n)
'''

'''
def display():
    global n 
    n = 10
    print("Inside function:",n)
display()
print("Outside function:",n)
'''
#Parameters
'''
def display():
    global n
    n+=10
    print("Inside function:",n)
n=10
display()
print("Outside function:",n)
'''

'''
def display():
    course = "PFS"
    def update():
        nonlocal course
        course = "JFS"
        print("Inner function:",course)
    update()
    print("Outer function:",course)
display()
'''
l = [1,2,3,4,5]
print(max(1))
print = 20
print(max)

