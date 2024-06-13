#Abstract Class and Abstract method

from abc import ABC, abstractmethod
class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):

    def process(self):
        print("Laptop is running")

class Tablet(Computer):

    def process(self):
        print("Tablet is running")

l1 = Laptop()
l1.process()

t1 = Tablet()
t1.process()