# Inheritance

class A:

    def __init__(self):
        print('in A init..')

    def feature1(self):
        print("feature1")

class B:

    def __init__(self):
        print('in B init..')

    def feature2(self):
        print("feature2")



class C(A, B): #Method Resolution Order (MRO) = (A,B) Or (B,A)

    def __init__(self):
        super().__init__() # It will call A class init method as while inheriting MRO of A is top
        print('in C init..')



c1 = C();
