
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

sizes=[10000,25000,50000,100000]
time_=[]

for size in sizes:
    arr=random.sample(range(500000),size)
    start = time.time()
    selection_sort(arr)
    time.sleep(1)
    end = time.time()
    time_.append((end-start)*1000)
    print(f"n: {size} , time of execution {time_[-1]:.2f}  milliseconds")

plt.plot(sizes,time_,marker='o')
plt.xlabel("n")
plt.ylabel("execution time")
plt.grid()
plt.show()
