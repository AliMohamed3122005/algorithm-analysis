import time
import random
import matplotlib.pyplot as plt

def run_insertion_sort(test_arrays):
    def insertionSort(list):
        length = len(list)
        for i in range(1,length):
            key = list[i]
            j = i
            while(j > 0 and list[j-1] > key):
                list[j] = list[j-1]
                j = j - 1
            list[j] = key    


    sizes = []
    time_ = []
    random.seed(42)  # Fixed seed
    for size, original_arr in test_arrays:
        arr = original_arr.copy()
        start = time.time()
        insertionSort(arr)
        end = time.time()
        time_.append((end-start)*1000)
        sizes.append(size)
        print(f"Insertion Sort -> Size : {size} , Execution Time : {(end-start)*1000:.2f} ms")
    return sizes,time_