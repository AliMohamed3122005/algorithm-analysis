import time
import random
import matplotlib.pyplot as plt

def insertionSort(list):
    length = len(list)
    for i in range(1,length):
        key = list[i]
        j = i
        while(j > 0 and list[j-1] > key):
            list[j] = list[j-1]
            j = j - 1
        list[j] = key    


sizes = [1000,2000,3000,5000,10000]
times = []
for size in sizes:
    arr = random.sample(range(20000),size)
    start = time.time()
    insertionSort(arr)
    end = time.time()
    times.append((end-start)*1000000)
    print(f"Size : {size} , Execution Time : {(end-start)*1000000}")

plt.plot(sizes,times,marker="o",color="blue",label="Insertion Sort")
plt.title("Insertion Sort Execution Time")
plt.xlabel("Input size (N)")
plt.ylabel("Execution time (Ms)")
plt.grid(True)
plt.legend()
plt.ticklabel_format(style="plain", axis="y")
plt.show()