import numpy as np
import matplotlib.pyplot as plt
import random
import time


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [i for i in range(1000)]
x = random.randint(0, 999)

linear_times = []
binary_times = []

for i in range(100):
    start_time = time.time()
    linear_search(arr, x)
    end_time = time.time()
    linear_times.append(end_time - start_time)

    start_time = time.time()
    binary_search(arr, x)
    end_time = time.time()
    binary_times.append(end_time - start_time)

print("Linear search times:")
print(f"min={min(linear_times):.6f} avg={sum(linear_times)/len(linear_times):.6f}")

print("Binary search times:")
print(f"min={min(binary_times):.6f} avg={sum(binary_times)/len(binary_times):.6f}")
