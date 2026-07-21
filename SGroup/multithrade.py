from threading import *
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello\n")
            sleep(1)
            
            
class hi(Thread):
    def run(self):
        for i in range(500):
            print("hi\n")
            sleep(1)
            
            
t1 = hello()
t2 = hi()

t1.start()
t2.start()