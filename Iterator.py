class TopTen:
    def __init__(self):
        self.num = 0;

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 10:
            self.num += 1;
            return self.num
        else:
            raise StopIteration


n = TopTen()
print(n.__next__())
print(n.__next__())

for i in n:
    print(i)
