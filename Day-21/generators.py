def reels():
    data = ['1..100', '101..200', '201..300', '301..400', '401..500']
    for i in data:
        yield i
res = reels()
print(next(res))
print(next(res))
print(next(res))
print(next(res))


def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

res = countdown()
for i in res:
    print(i)


def factors(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


res = factors(16)
for i in res:
    print(i)



for i in res:
    print(i)


def prime(number):
    for i in range(2, number):
        if number % i == 0:
            return
    yield number


res = prime(17)