import random
import time
import matplotlib.pyplot as plt

def run_bubble_sort(test_arrays):
    def Bubble_sort(arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr


    sizes=[]
    time_=[]
    
    for size, original_arr in test_arrays:
        arr = original_arr.copy()
        start = time.perf_counter()
        Bubble_sort(arr)
        end = time.perf_counter()
        time_.append((end-start)*1000)
        sizes.append(size)
        print(f"Bubble Sort -> n: {size} , time of execution {time_[-1]:.2f}  ms")
    return sizes, time_
