import time


def maxHeapify(arr,i,length): ## O(log n)
    left = (i*2)+1
    right = (i*2)+2
    largest = i
    if(left <= length and arr[left] > arr[largest]):
        largest = left
    if(right <= length and arr[right] > arr[largest]):
        largest = right
    if(largest != i):
        arr[largest],arr[i]=arr[i],arr[largest]
        maxHeapify(arr,largest,length)

def buildMaxHeap(arr): ## O(n)
    length = len(arr)
    for i in range((length//2)-1,-1,-1):
        maxHeapify(arr,i,length-1)

def heapSort(arr):  
    buildMaxHeap(arr)
    length = len(arr)
    heapSize = length
    for i in range(length-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapSize -= 1
        maxHeapify(arr,0,heapSize-1)
    return arr    


def run_heap_sort(test_arrays):
    sizes = []
    times = []

    for size, arr in test_arrays:
        arr_copy = arr.copy()

        start = time.perf_counter()
        heapSort(arr_copy)
        end = time.perf_counter()

        sizes.append(size)
        times.append((end - start) * 1000)

    return sizes, times