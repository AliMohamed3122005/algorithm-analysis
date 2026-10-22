import random
import time
import matplotlib.pyplot as plt



def selection_sort(lst):
        n = len(lst)
        for i in range(n):
            min_index = i
            for j in range(i+1,n):
                if lst[min_index] > lst[j]:
                    min_index = j
            lst[min_index], lst[i] = lst[i], lst[min_index]

def run_selection_sort(test_arrays):
    sizes=[]
    time_=[]
    
    
    for size, original_arr in test_arrays:
        arr = original_arr.copy()
        start = time.perf_counter()
        selection_sort(arr)
        end = time.perf_counter()
        time_.append((end-start)*1000)
        sizes.append(size)
        print(f"Selection Sort -> n: {size} , time of execution {time_[-1]:.2f}  ms")
    return sizes,time_


