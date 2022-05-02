from collections import deque
import time
import heapq

class Scheduler:
    def __init__(self):
        self.ready = deque() # Fns ready to execute
        self.sleeping = []
        self.sequence = 0

    def call_soon(self, func):
        self.ready.append(func)
    
    def call_later(self, func, delay):
        """
        Interesting corner case:
        >>> sleeping = [(2, f), (2, g)]
        >>> sleeping.sort()
        Traceback (most recent call last):
        TypeError: '<' not supported between instances of 'function' and 'function'
        """
        deadline = time.time() + delay # Expiration time
        heapq.heappush(self.sleeping, (deadline, self.sequence,  func)) # Priority queue
        self.sequence += 1

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                # Find nearest deadline
                deadline, _, func = heapq.heappop(self.sleeping)
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
