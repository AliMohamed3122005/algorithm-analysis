import random
import time
import matplotlib.pyplot as plt

def run_bubble_sort():
    def Bubble_sort(arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr


    sizes=[10000,25000,50000,100000]
    time_=[]
    for size in sizes:
        arr=random.sample(range(500000),size)
        start = time.time()
        Bubble_sort(arr)
        end = time.time()
        time_.append((end-start)*1000)
        print(f"Bubble Sort -> n: {size} , time of execution {time_[-1]:.2f}  ms")

    plt.style.use("dark_background")
    plt.plot(sizes, time_, marker="o", color="#00FFFF", label="Bubble Sort")
    plt.title("Bubble Sort - Execution Time")
    plt.xlabel("Input size (N)")
    plt.ylabel("Execution time (Ms)")
    plt.grid(True)
    plt.legend()
    plt.ticklabel_format(style="plain", axis="y")
