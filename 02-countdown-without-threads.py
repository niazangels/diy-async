from collections import deque
import time

class Scheduler:
    def __init__(self):
        self.ready = deque() # Fns ready to execute

    def call_soon(self, func):
        self.ready.append(func)
    
    def run(self):
        while self.ready:
            func = self.ready.popleft()
            func()


def countdown(n):
    if n > 0:
        print(f"Down {n}")
        time.sleep(1) # Blocking call - nothing else can happen
        sched.call_soon(lambda: countdown(n-1))


def countup(stop, x=0):
    if x < stop:
        print(f"Up {x}")
        time.sleep(1) # Blocking call - nothing else can happen
        sched.call_soon(lambda: countup(stop, x+1))


sched = Scheduler()
sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(5))
sched.run()


# How can we do this without threads?

# But, first, why even do this?
# 5000 network connections = 5000 threads?
# Threads are a harder to cancel once you start them.


# How can we do this?
# Issue: Figure out how to switch between threads?
