"""Demonstration of local and global variable scope."""


# A function can read a global variable if it does not define a local
# variable with the same name.
def display():
	print("Inside function:", n)


n = 10
display()
print("Outside function:", n)


# The global keyword is used when a function needs to assign to the global
# variable.  It is written as: global n (the variable name is required).
def update_number():
	global n
	n = 20
	print("Inside function after update:", n)


update_number()
print("Outside function after update:", n)


# Without global, an assignment creates a local variable instead:
def local_number():
	n = 30
	print("Inside local function:", n)


local_number()
print("Outside local function:", n)

# Concept:
# - Global scope: n can be accessed throughout this file.
# - Local scope: a variable assigned inside a function belongs to that
#   function only.
# - Use "global n" only when you intentionally want to modify the global n.

#============================================================================
# A nested function can modify a variable from its enclosing function with
# the nonlocal keyword.
def course_display():
	course = "PFS"

	def update():
		nonlocal course
		course = "JFS"
		print("In.fu:", course)

	update()
	print("OU.f:", course)


course_display()


numbers = [1, 2, 3, 4, 5, 6, 7]
print(max(numbers))
print(20)
print(max)

def display(n):
	n[5] = 6
	print("Inside the function:", n)
n = {1:2,3:4}
display(n)
print("outside the function:",n)



def display(n):
	if n==11:
		return
	print(n)
	display(n+1)
display(1)
