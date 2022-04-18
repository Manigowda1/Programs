from threading import *
from time import sleep

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


m1 = Hello()
m2 = Hi()

m1.start()
sleep(0.2) # avoids collision
m2.start()

m1.join() # main thread will wait for t1 to execute
m2.join()# main thread will wait for t2 to execute
print("Bye")

