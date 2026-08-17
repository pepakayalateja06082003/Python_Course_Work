age = 20

if age >= 18:
    print("You are eligible to vote")

eli_acc = eval(input("Enter your account balance: "))
ver_sub = eval(input("Enter your subscription amount: "))

if eli_acc >= ver_sub:
    print("You can subscribe to the service")
else:
    print("You cannot subscribe to the service")

rain = input("Is it raining? (yes/no): ")
if rain.lower() == "yes":
    print("Take an umbrella with you.")
else:
    print("You don't need an umbrella.")