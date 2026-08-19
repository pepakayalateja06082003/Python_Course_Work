//# String, list, tuple, set, dictionary, Range. ====> for var in seq  ***stmts***

# String
s = 'python class'
for i in s:
    print(i)

# List
l = [10, 20, 30, 40, 50]
for num in l:
    print(num)

# Tuple
prices = (100, 200, 300, 400, 500)
for p in prices:
    print(p)

# Set
name = {'sai', 'kiran', 'suresh', 'ramesh'}
for n in name:
    print(n)

# Dictionary
d = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
for i in d:
    print(i, d[i])

# Range
for i in range(1, 6):
    print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

# Range with index
for i in range(1, 6):
    print(i)

s = 'Java Programming'
for i in range(len(s)):
    print(i, s[i])

# Tuple with index
s = (454, 4567, 14232, 112)
for i in range(len(s)):
    print(i, s[i])

# Dictionary with enumerate
d = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
for i in enumerate(d):
    print(i[0], i[1], d[i[1]])

# Continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Break and else
l = [12, 13, 14, 15, 16, 17]
n = 13

for i in l:
    if i == n:
        print(n, "found")
        break
else:
    print(n, "not found")

pin = 123
for  i in range(5):
    epin = int(input("Enter the pin:"))
    if epin == pin:
        print("unlock phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try after 30 seconds")

#prime number 

n = 14
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime number ")
        break
else:
    print("Prime Number")
    
