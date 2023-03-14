import threading
import time
import random

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = -1
        self.buffer = [None] * capacity
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def enqueue(self, data):
        with self.not_full:
            while self.size == self.capacity:
                self.not_full.wait(1)
            if self.size < self.capacity:
                self.rear = (self.rear + 1) % self.capacity
                self.buffer[self.rear] = data
                self.size += 1
                self.not_empty.notify()

    def dequeue(self):
        with self.not_empty:
            while self.size == 0:
                self.not_empty.wait(1)
            if self.size > 0:
                data = self.buffer[self.front]
                self.front = (self.front + 1) % self.capacity
                self.size -= 1
                self.not_full.notify()
                return data

def producer(q):
    while True:
        data = random.randint(1, 10)
        time.sleep(data)
        q.enqueue(data)

def consumer(q):
    while True:
        data = random.randint(1, 10)
        time.sleep(data)
        print(q.dequeue())

if __name__ == "__main__":
    q = Queue(10)
    threads = [threading.Thread(target=producer, args=(q,)),
               threading.Thread(target=consumer, args=(q,))]
    for t in threads:
        t.start()
