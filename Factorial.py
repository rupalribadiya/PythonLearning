# Factorial Of A Number
def factorial(n):
    print(__name__)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
fact = factorial(num)
print(fact)