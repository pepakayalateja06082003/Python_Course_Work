# IF-ELSE - Executes one block if True, another if False

marks = 45

if marks >= 50:

    print("Pass")
else:
    print("Fail")

###########################################################

username = input("Enter your username: ")
if username == "admin":
    print("Welcome, admin!")
else:
    print("Access denied. You are not an admin.")

################################################################

products = ["Laptop", "Smartphone", "Tablet"]
product_name = input("Enter the product name: ")
if product_name in products:
    print(f"{product_name} is available.")
else:
    print(f"{product_name} is not available.")
 ###############################################################

bill = eval(input("Enter your bill amount: "))
if bill >= 100:
    print("You are eligible for a discount.", bill - (bill * 20 / 100))
else:
    print("You are not eligible for a discount.")
###################################################################