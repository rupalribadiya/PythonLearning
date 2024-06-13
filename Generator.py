#It create an iterator

def topTen():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1

num = topTen()

print(num.__next__())
for sq in num:
    print(sq)