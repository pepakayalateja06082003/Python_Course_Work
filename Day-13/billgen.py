data = {
    "suger" : 50,
    "cho" : 220,
    "cooking oil" : 234,
    "rice" : 2323,
    "butter" : 23,
}
for i in data:
    print(i.ljust(20),data[i])
prods = input("Enter the pro : ").split()
#print(prods)
print("========================BILL=================")
bill = 0
for i in prods:
    print(i.ljust(20), data[i])
    bill += data[i]
print("Total Bill " .ljust(20),bill)


s = "PEPAKAYALA TEJA"
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i]=1
        {'P': 2, 'E': 2, 'A': 4, 'K': 1, 'Y': 1, 'L': 1, ' ': 1, 'T': 1, 'J': 1}
print(d)    

a = 'aaaaaaasssssbbbbbbbffffcccttteddccggaaafvvv'
c = 1
res = " "
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c+=1
    else:
        res+=s[i]+a(c)
        c=1
print(res+s[i]+str(c))