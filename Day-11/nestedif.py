fa = eval(input("Follows Account: "))
if fa == 1:
    cf = eval(input("close Friend: "))
    if cf:
        print("You are a close friend")
    else:
        print("You are not a close friend")
else:
    print("You do not follow the account plz follow the account ")


#==============================================================

reg = eval(input("Registered: "))
if reg:
    fee = eval (input("Paid fee: "))
    if fee:
        print("paid fee entry allowed")
    else:
        print("Not paid fee entry not allowed")
else:
    print("Not registered entry not allowed")

#==============================================================

file = eval(input("link active: "))
if file:
    access = eval(input("access granted: "))
    if access:
        print("You can access the file")
    else:
        print("You cannot access the file")
else:
    print("Link is not active you cannot access the file")

#============================================================


data = {
    'Teja':{'status': True, "python":90, "mysql": 80, "flask": 70},
    'dipak':{'status': False, "python":80, "mysql": 70, "flask": 60},
    'dinesh':{'status': True, "python":70, "mysql": 60, "flask": 50},
    'sai':{'status': False, "python":60, "mysql": 50, "flask": 40},
    'sai teja':{'status': True, "python":None, "mysql": None, "flask": None},
}

name = input("Enter your name: ")
if name in data:
    if data[name]['status']:
        sum =  data[name]['python'] + data[name]['mysql'] + data[name]['flask']
        avg = sum / 3
        print(f"Hello {name},!!!")
        print(f"Your average score is: {avg}")
        if avg >= 95:
            print("You are an excellent student")
        elif avg >= 85:
            print("You are a good student")
        elif avg >= 75:
            print("You are an average student")
        elif avg >= 65:
            print("You are a below average student")
        elif avg >= 50:
            print("You are a poor student")
        elif avg < 50:
            print("You are a failed student")
    else:
        print(f'{name} exam is faaa try next time bye ')
            