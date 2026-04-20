import threading
from typing import Callable
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.lock = threading.lock() # Mutex for thread synchronization
    
    # printFizz() outputs 'fizz'
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.i<=self.n:
            # Acquire lock to ensure thread-safe access to shared index
            with self.lock:
                if self.i%3==0 and self.i%5!=0 and self.i<=self.n:
                    printFizz()
                    self.i+=1
    
    # printBuzz() outputs 'buzz'
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.i<=self.n:
            with self.lock:
                if self.i%5==0 and self.i%3!=0 and self.i<=self.n:
                    printBuzz()
                    self.i+=1
    
    # printFizzBuzz() outputs 'fizzbuzz'
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.i<=self.n:
            with self.lock:
                if self.i%3==0 and self.i%5==0 and self.i<=self.n:
                    printFizzBuzz()
                    self.i+=1
    
    # printNumber(x) outputs 'x' where x is an integer
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i<=self.n:
            with self.lock:
                if self.i%3!=0 and self.i%5!=0 and self.i<=self.n:
                    printNumber(self.i)
                    self.i+=1