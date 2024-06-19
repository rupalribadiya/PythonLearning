def diamondPattern(n):
    for i in range(1, (2 * n + 1)):
        if i <= n:
            spaces = ' ' * (n - i) * 2
            numbers = ' '.join(str(j) for j in range(1, 2 * i))
            print(spaces + numbers)
        else:
            spaces = ' ' * (i - n) * 2
            numbers = ' '.join(str(j) for j in range(1, (2 * n -i) * 2))
            print(spaces + numbers)

n = 5
diamondPattern(n)