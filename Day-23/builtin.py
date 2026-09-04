import sys
print(sys.argv)
print(sys.version)
print(sys.path)
print("Start")
sys.exit()
print("end")

import platform
print(platform.system())
print(platform.release())
print(platform.processor())

print(math.pi)
print(math.e)
print(mayh.log(2,2))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.radians(30))
print(math.gcd(8,12))
print(math.sqrt(36))
print(math.pow(2,3))



print(round(12.666))
print(round(12.9999999999))

print(math.cell(12.0000001))
print(math.cell(12.3))
print(math.cell(12.6666))
print(math.cell(12.999999))

print(math.floor(12.0000001))
print(math.floorl(12.3))
print(math.floor(12.6666))
print(math.floor(12.999999))

import random
random.seed(9)
print(random.random())
print(random.randint(100000,999999))
print(random.uniform(1,6))

l = ['r' , 'p' , 's']
print(random.choice(l))
lang = ['py','ja','css']
print(random.choice(lang,k=2))

random.shuffle(lang)
print(land)


from collections import Counter , defaultdict


s = "hi"
d = defaultdict(int)
for char in s:
    res[char] += 1
    print(res)

l = deque([])

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.appendleft(70)
l.pop()