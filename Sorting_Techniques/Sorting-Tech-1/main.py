
import random
import matplotlib.pyplot as plt

from bubble_sort import run_bubble_sort
from insertion_sort import run_insertion_sort
from selection_sort import run_selection_sort


def main():
    sizes = [1000, 25000, 50000, 100000]

    random.seed(42)
    test_arrays = [
        (size, random.sample(range(500000), size))
        for size in sizes
    ]

    bubble_sizes, bubble_times = run_bubble_sort(test_arrays)
    insertion_sizes, insertion_times = run_insertion_sort(test_arrays)
    selection_sizes, selection_times = run_selection_sort(test_arrays)

    plt.style.use("dark_background")

    plt.plot(
        bubble_sizes, bubble_times,
        marker="o", label="Bubble Sort"
    )

    plt.plot(
        insertion_sizes, insertion_times,
        marker="o", label="Insertion Sort"
    )

    plt.plot(
        selection_sizes, selection_times,
        marker="o", label="Selection Sort"
    )

    plt.title("Sorting Algorithms Comparison")
    plt.xlabel("Input size (N)")
    plt.ylabel("Execution time (ms)")
    plt.grid(True)
    plt.yscale("log")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
