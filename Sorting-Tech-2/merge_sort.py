import random
import time
import matplotlib.pyplot as plt



def run_merge_sort(test_arrays):
    def mergeSort(arr):
        if (len(arr)<=1):
            return arr
        mid = len(arr) // 2
        left_half=arr[:mid]
        right_half=arr[mid:]

        sorted_left_half =mergeSort(left_half)
        sorted_right_half =mergeSort(right_half)

        return merge(sorted_left_half,sorted_right_half)

    def merge(left,right):
        result = []
        i =0
        j=0
        while i < len(left) and j<len(right) :
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


    sizes=[]
    time_=[]
    for size, original_arr in test_arrays:
        arr = original_arr.copy()
        start = time.time()
        mergeSort(arr)
        end = time.time()
        time_.append((end-start)*1000)
        sizes.append(size)
        print(f"Merge Sort -> n: {size} , time of execution {time_[-1]:.2f}  ms")
    return sizes, time_
