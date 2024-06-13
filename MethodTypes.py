#Class method vs Instance method vs Static menthod
#Inner Class

class Student:

    school = 'St Xvious' #Class Variable

    def __init__(self, name, rollNo, m1, m2, m3):
        #Instance Variable
        self.name = name
        self.rollNo = rollNo
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lp = self.Laptop()

    #Instance Method: Which uses instance Variables
    def agvScore(self):
        return (self.m1 + self.m2 + self.m3)/3

    #Class Method: which uses class variables
    @classmethod
    def getSchool(cls):
        return cls.school

    #Static Method: Which don't use class variable or instance variable
    @staticmethod
    def info():
        print('This is a student module..')

    def show(self):
        print(self.name, self.rollNo)
        self.lp.show()

    #Inner Class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Rupal',1, 40,45,38);
s2 = Student('Nishant', 2, 32,48,35);

print(s1.agvScore());
print(s2.agvScore());

print(Student.getSchool());
Student.info();

s1.show();
s2.show();
