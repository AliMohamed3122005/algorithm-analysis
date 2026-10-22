import sys
from pathlib import Path

part1_path = Path(__file__).resolve().parent.parent / "Sorting-Tech-1"
sys.path.insert(0, str(part1_path))

import time
from selection_sort import selection_sort


def run_hybrid_merge_sort(test_arrays,threshold):
    def mergeSort(arr):
        if threshold < 1:
            raise ValueError("Threshold must be at least 1")
        if (len(arr)<=threshold):
            selection_sort(arr)
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
        print(f"Hybrid Merge Sort -> n: {size} , time of execution {time_[-1]:.2f}  ms")
    return sizes, time_
