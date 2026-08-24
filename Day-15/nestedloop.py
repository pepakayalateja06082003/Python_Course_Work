
#1)

for row in range(5):
	for column in range(5):
		print("T", end=" ")
	print()

#2)

for i in range(5):
	for j in range(5):
		print(j % 2, end=" ")
	print()

#3)

for i in range(5):
	for j in range(5):
		print(i % 2, end=" ")
	print()

#4)

for i in range(5):
	for j in range(5):
		print( (i + j)%2 , end=" ")
	print()

#5)

for i in range(5):
	for j in range(5):
		print(i + j, end=" ")
	print()

#6)

num = 1
for i in range(5):
	for j in range(5):
		print(num, end=" ")
		num += 1
	print()



#7)

for i in range(5):
	for j in range(i + 1):
		print("x", end="")
	print()

#8)

for i in range(5):
	for j in range(5 - i):
		print("x", end="")
	print()

#9) home work 

for i in range(5):
	if i % 2 == 0:
		for j in range(5):
			print(i * 5 + j + 1, end="")
	else:
		for j in range(4, -1, -1):
			print(i * 5 + j + 1, end="")
	print(",")



#10)

for i in range(5):
	for j in range(4 - i):
		print(" ", end="")
	for j in range(i + 1):
		print("*", end="")
	print()


#11)

for i in range(5):
    for sp in range(i):
        print(" ", end="")
    for j in range(5 - i):
        print("*", end="")
    print()



#12)


n = int(input("size: "))
m = n//2
for i in range(n):
    if i <= m:
        for j in range(i+1):
            print("*",end=' ')
    else:
        for k in range(n-i):
            print("*",end=" ")
    print()