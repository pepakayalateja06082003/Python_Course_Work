'''
def fun(arg):
    if base condition:
        return
    function (modified args)
    '''
'''
def display(n):
    if n==1:
        return
    print(n)
    display(n+1)
display(1)
'''
'''
def display(n):
    if n==0:
        return
    print(n)
    display(n-1)

display(10).
'''

def display(s,n):
    if n==len(s):
        return
    print(s[n])
    display(s,n+1)
display("Dinesh",0)