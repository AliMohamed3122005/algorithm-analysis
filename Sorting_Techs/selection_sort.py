import random
import time
import matplotlib.pyplot as plt

def run_selection_sort():
    def selection_sort(lst):
        n = len(lst)
        for i in range(n):
            min_index = i
            for j in range(i+1,n):
                if lst[min_index] > lst[j]:
                    min_index = j
            lst[min_index], lst[i] = lst[i], lst[min_index]

    sizes=[10000,25000,50000,100000]
    time_=[]

    for size in sizes:
        arr=random.sample(range(500000),size)
        start = time.time()
        selection_sort(arr)
        end = time.time()
        time_.append((end-start)*1000)
        print(f"Selection Sort -> n: {size} , time of execution {time_[-1]:.2f}  ms")


    plt.style.use("dark_background")
    plt.plot(sizes, time_, marker="o", color="#FF00FF", label="Selection Sort")
    plt.xlabel("Input size (N)")
    plt.ylabel("Execution time (Ms)")
    plt.title("Selection Sort - Execution Time")
    plt.grid(True)
    plt.legend()
    plt.ticklabel_format(style="plain", axis="y")


