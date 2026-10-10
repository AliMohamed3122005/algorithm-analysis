import time
import random
import matplotlib.pyplot as plt

def run_insertion_sort():
    def insertionSort(list):
        length = len(list)
        for i in range(1,length):
            key = list[i]
            j = i
            while(j > 0 and list[j-1] > key):
                list[j] = list[j-1]
                j = j - 1
            list[j] = key    


    sizes = [10000,25000,50000,100000]
    time_ = []
    for size in sizes:
        arr = random.sample(range(20000),size)
        start = time.time()
        insertionSort(arr)
        end = time.time()
        time_.append((end-start)*1000)
        print(f"Insertion Sort -> Size : {size} , Execution Time : {(end-start)*1000:.2f} ms")

    plt.style.use("dark_background")
    plt.plot(sizes, time_, marker="o", color="#00FF00", label="Insertion Sort")
    plt.title("Insertion Sort - Execution Time")
    plt.xlabel("Input size (N)")
    plt.ylabel("Execution time (Ms)")
    plt.grid(True)
    plt.legend()
    plt.ticklabel_format(style="plain", axis="y")
