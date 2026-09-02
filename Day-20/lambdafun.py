#var= lambda arguments: expression
'''
wish = lambda name: f"Welcome to the course {name}"
print(wish("Dinesh"))
print(wish("Abhi"))

gst = lambda price: price+price*0.18
print(gst(1000))
print(gst(2000))

avg = lambda a,b,c: (a+b+c)/3
print(avg(3,4,5))
print(avg(8,10,15))

iseven = lambda a: "Even" if a%2==0 else "Odd"
print(iseven(10))
print(iseven(11))

largest = lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(largest(23,34,12))
print(largest(30,54,22))

isvowels = lambda a: "Vowels" if a in "aeiouAEIOU" else "Consonants"
print(isvowels("u"))
print(isvowels("k"))
'''
'''
l = [1,2,3,4,5,6,7]
update = list(map(lambda i: i+10, l))
print(update)


t = (789,421,3453,24235,35430)
discount = list(map(lambda i: i-i*0.3,t))
print(discount)
'''
'''

l = [1,2,3,4,5,6,7]
update = list(filter(lambda i: i+10, l))
print(update)


t = (789,421,3453,24235,35430)
discount = list(filter(lambda i: i-i*0.3,t))
print(discount)
'''
'''
l=['dinesh@gmail.com','dineshperukuri@gmail.com','dinesh21@gmail.com','Abhi1526@gmail.com']
domain = list(map(lambda i: i.split('@')[-1],l))
print(domain)
'''
'''
from functools import reduce

l = [4,5,6,7,89,24,66,88]
res = reduce(lambda sum,i: sum+i,l)
print(res)

res1 = reduce(lambda pro,i: pro*i,l)
print(res1)
'''
'''
products={'Eggs':80,
          'suger':50,
          'salt':89,
          'butter':100,
          'milk':20
}
'''
'''
res = list(filter(lambda i: products[i]>50,products))
print(res)

products={'Eggs':80,
          'suger':50,
          'salt':89,
          'butter':100,
          'milk':20
}
'''
'''
print(dict(sorted(products.items(),key= lambda i:i[1])))
print(dict(sorted(products.items(),key= lambda i:i[1],reverse=True)))
'''