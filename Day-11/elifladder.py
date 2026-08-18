

budget = int(input("Enter your restaurant budget (in rupees): "))
if budget > 10000:
    print("Trip")
elif budget > 5000:
    print("Resort stay")
elif budget > 3000:
    print("Fine dining")
elif budget > 1000:
    print("Casual dining")
elif budget > 500:
    print("Fast food")



#=================================================


hr = int(input("Enter the time : "))
if 5 <= hr <= 11:
    print("Good Morning")
elif 12 <= hr <= 15:
    print("Good Afternoon")
if 16 <= hr <= 20:
    print("Good Evening")
if 21 <= hr <= 23 or 0 <= hr <= 4:
    print("Good Night")

#========================================================= 


cus_budget = int(input("Enter your restaurant budget (in rupees): "))
if cus_budget > 10000: 
    print("Trip")
elif cus_budget > 5000:
    print("Resort stay")
elif cus_budget > 3000:
    print("Fine dining")
elif cus_budget > 1000:
    print("Casual dining")
else:
    print("Budget too low for any specific option")
    