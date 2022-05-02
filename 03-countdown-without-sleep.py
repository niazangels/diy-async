from collections import deque
import time

class Scheduler:
    def __init__(self):
        self.ready = deque() # Fns ready to execute
        self.sleeping = []

    def call_soon(self, func):
        self.ready.append(func)
    
    def call_later(self, func, delay):
        deadline = time.time() + delay # Expiration time
        self.sleeping.append((deadline, func))
        self.sleeping.sort()
    
    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                # Find nearest deadline
                deadline, func = self.sleeping.pop(0)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(func)
            
            while self.ready:
                func = self.ready.popleft()
                func()

def countdown(n):
    if n > 0:
        print(f"Down {n}")
        sched.call_later(lambda: countdown(n-1), delay=4)


def countup(stop, x=0):
    if x < stop:
        print(f"Up {x}")
        sched.call_later(lambda: countup(stop, x+1), delay=1)


sched = Scheduler()
sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(20))
sched.run()

# How can we do this?
# Issue: Figure out how to switch between threads?
