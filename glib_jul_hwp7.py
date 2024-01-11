# task 3
#def geometric_progression_generator(b, q, num_t):
#    t = (b * q ** n for n in range(num_t))
#    yield from t

#my_generator = geometric_progression_generator(2, 8, 9)
#for t in my_generator:
#    print(t)

# task 4
#def range(start, stop, step=1):
#    while start < stop:
#        yield start
#        start += step
#result = list(range(10, 40, 7.5))
#print(result)

# task 5
#def prime_generator(limit):
#    primes = []
#    number = 2
#    while number <= limit:
#        if all(number % prime != 0 for prime in primes if prime * prime <= number):
#            primes.append(number)
#            yield number
#        number += 1

#for i in prime_generator(31):
#    print(i)

# task 6
#def generate_cubes(limit):
#    num = 2
#    while num <= limit:
#        yield num**3
#        num += 1

#limit = 20
#cubes = list(generate_cubes(limit))
#print(cubes)

# task 7
#def fibonacci_generator():
#    a, b = 1, 1
#    while True:
#        yield a
#        a, b = b, a + b

#f = fibonacci_generator()
#for _ in range(8):
#    print(next(f))

# task 8
from datetime import timedelta, date

def date_range_generator(start, end):
    interval = timedelta(days=1)
    while start <= end:
        yield start
        start += interval

gen = date_range_generator(date(1988, 3, 5), date(1989, 5, 3))
for d in gen:
    print(d)




