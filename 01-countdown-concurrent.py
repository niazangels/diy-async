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
# countdown(5)
# countup(5)

# Concurrent execution
# Classic solution: use threads

import threading

threading.Thread(target=countdown, args=(5,)).start()
threading.Thread(target=countup, args=(5,)).start()

# threads in python == threads in C == fully threaded at OS level
# One real issue is GIL => prevents threads from running in true parallel


