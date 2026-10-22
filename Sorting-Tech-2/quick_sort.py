
import random
import time
import matplotlib.pyplot as plt


def run_quick_sort(test_arrays):
    def random_quick_sort(arr, low, high):
        if low < high:
            pivot_index = random_partition(arr, low, high)
            random_quick_sort(arr, low, pivot_index - 1)
            random_quick_sort(arr, pivot_index + 1, high)

    def random_partition(arr, low, high):
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        return partition(arr, low, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    sizes = []
    time_ = []

    for size, original_arr in test_arrays:
        arr = original_arr.copy()

        start = time.time()
        random_quick_sort(arr, 0, len(arr) - 1)
        end = time.time()

        time_.append((end - start) * 1000)
        sizes.append(size)
        print(
            f"Quick Sort -> n: {size}, "
            f"time of execution: {time_[-1]:.2f} ms"
        )
    return sizes, time_
