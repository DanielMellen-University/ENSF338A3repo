import sys

def main():
    test_list = []
    prev_capacity = 0

    for i in range(64):
        test_list.append(i)
        current_capacity = sys.getsizeof(test_list) - sys.getsizeof([])
        if current_capacity != prev_capacity:
            print(f"Capacity changed at {i + 1} elements. New capacity: {current_capacity} bytes.")
            prev_capacity = current_capacity

if __name__ == "__main__":
    main()
