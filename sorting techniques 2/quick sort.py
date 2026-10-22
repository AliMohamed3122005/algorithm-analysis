import random


    
def random_quick_sort(arr,low, high):
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




unsorted_list = [random.randint(1, 100) for _ in range(10)]
print("Unsorted List:", unsorted_list)
random_quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
print("Sorted List:", unsorted_list)