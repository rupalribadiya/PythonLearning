from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

# Start: It will in turn execute a run method
t1.start()
sleep(0.2)
t2.start()

# Join: Main thread will wait for t1 and t2 threate to complete their execution
t1.join()
t2.join()

print('Bye')
