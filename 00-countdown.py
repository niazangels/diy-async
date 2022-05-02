import py_compile
import time

def countdown(n):
    while n > 0:
        print(f"Down {n}")
        time.sleep(1)
        n -= 1

def countup(stop):
    x = 0
    while x < stop:
        print(f"Up {x}")
        time.sleep(1)
        x += 1

# Sequential execution
countdown(5)
countup(5)