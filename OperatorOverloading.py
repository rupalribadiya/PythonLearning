# Duck Typing: If Object has a method is behave like that.

# Operator Overloading

class Students:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        return Students(s1, s2)

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        #return f'{self.m1}, {self.m2}'
        return '{} {}'.format(self.m1, self.m2)

s1 = Students(90, 85)
s2 = Students(68, 90)

s3 = s1 + s2 #Student.__add__(s1, s2)
print(s3) #Student.__str__(s1)

if s1 > s2: #Student.__gt__(s1, s2)
    print('s1 win')
else:
    print('s2 win')

