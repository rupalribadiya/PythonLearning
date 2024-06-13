# Fibonacci Series

lst = [0, 1]
i = 0
j = 1

for num in range(1,11):
    fib = i + j
    lst.append(fib)
    i = j
    j = fib
    print(i,j)

print(lst)