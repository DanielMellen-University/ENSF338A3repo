import random
import time
import heapq
import matplotlib.pyplot as plt

def inefficient_insert(queue, element):
    queue.append(element)
    queue.sort(reverse=True)

def inefficient_extract(queue):
    return queue.pop()

def efficient_insert(queue, element):
    heapq.heappush(queue, element)

def efficient_extract(queue):
    return heapq.heappop(queue)

def time_experiment(num_elements, num_trials):
    inefficient_times = []
    efficient_times = []

    for _ in range(num_trials):
        data = [random.randint(0, 1000) for _ in range(num_elements)]

        # Inefficient implementation
        inefficient_queue = []
        start_time = time.time()
        for item in data:
            inefficient_insert(inefficient_queue, item)
        for _ in range(num_elements):
            inefficient_extract(inefficient_queue)
        inefficient_times.append(time.time() - start_time)

        # Efficient implementation
        efficient_queue = []
        start_time = time.time()
        for item in data:
            efficient_insert(efficient_queue, item)
        for _ in range(num_elements):
            efficient_extract(efficient_queue)
        efficient_times.append(time.time() - start_time)

    return inefficient_times, efficient_times

def main():
    num_elements = 1000
    num_trials = 100

    inefficient_times, efficient_times = time_experiment(num_elements, num_trials)

    plt.hist(inefficient_times, bins=20, alpha=0.5, label="Inefficient")
    plt.hist(efficient_times, bins=20, alpha=0.5, label="Efficient")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency")
    plt.legend(loc="upper right")
    plt.title("Priority Queue Insertion and Extraction: Inefficient vs Efficient")
    plt.show()

    print(f"Inefficient avg: {sum(inefficient_times) / num_trials:.6f}s")
    print(f"Efficient avg: {sum(efficient_times) / num_trials:.6f}s")

if __name__ == "__main__":
    main()
