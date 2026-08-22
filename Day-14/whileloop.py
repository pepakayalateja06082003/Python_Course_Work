"""While-loop examples.

A while loop repeats its body while its condition remains True.  The loop
variable must be updated so that the condition eventually becomes False.
"""
'''
# 1. Increase i from 1 to 10.
i = 1
while i < 10:
	i += 1
print("Value after increasing:", i)

# 2. Print numbers from 10 down to 1.
i = 10
while i > 0:
	print(i)
	i -= 1

# 3. Print multiples of 5 from 5 through 50.
i = 5
while i <= 50:
	print(i)
	i += 5

# 4. Print each character in a string using its index.
text = "while loop"
i = 0
while i < len(text):
	print(text[i])
	i += 1

# 5. Print each item in a list using its index.
numbers = [5467, 54678, 6789, 987]
i = 0
while i < len(numbers):
	print(numbers[i])
	i += 1

# 6. Reverse a number without converting it to a string.
# The last digit is obtained with %, then removed with //.
number = 8765
reversed_number = 0
while number > 0:
	digit = number % 10
	reversed_number = reversed_number * 10 + digit
	number //= 10
print("Reversed number:", reversed_number)

# 7. Add all even digits in a number.
number = 5456774648
even_digit_sum = 0
while number > 0:
	digit = number % 10
	if digit % 2 == 0:
		even_digit_sum += digit
	number //= 10
print("Sum of even digits:", even_digit_sum)


# 8. Remove every zero from a list.
# The condition is True while at least one zero is present. Each call to
# remove(0) deletes the first zero, so the loop ends when no zeros remain.

l = [6, 9, 23, 0, 0, 0, 12, 0, 13, 0, 1, 0, 4, 0, 1, 0, 0, 1, 4, 5, 6, 6, 13, 0]
while 0 in l:
	l.remove(0)
print(l)
print(1)

# 9. Add the first and last list items, then move both indexes toward the center.
# If both indexes meet, print the middle item once.
l = [2, 3, 6, 76, 12, 4, 5, 62, 4, 5, 3, 32, 23]
i, j = 0, len(l) - 1
while i <= j:
	if i == j:
		print(l[i])
	else:
		print(l[i] + l[j])
	i += 1
	j -= 1

'''

