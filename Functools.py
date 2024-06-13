from functools import reduce;
from Factorial import *;

num = [2,5,3,4,7,6,8,9,1,6]

n = 9
print(num.index(n))

evens = list(filter(lambda x: x % 2 == 0, num))
print(evens)

doubles = list(map(lambda x: x * 2, evens))
print(doubles)

sumAll = reduce(lambda x, y: x + y, doubles)
print(sumAll)

print(__name__)

fact = factorial(num[0]); # Use Module from another file
print(fact)
