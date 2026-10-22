import sys
from pathlib import Path

part1_path = Path(__file__).resolve().parent.parent / "Sorting-Tech-1"
sys.path.insert(0, str(part1_path))

from merge_sort import run_merge_sort
from quick_sort import run_quick_sort
from hybrid_merge_sort import run_hybrid_merge_sort

from selection_sort import run_selection_sort
from insertion_sort import run_insertion_sort
from bubble_sort import run_bubble_sort
from heap_sort import run_heap_sort

import matplotlib.pyplot as plt
import random


def main():
        sizes = [100, 2500, 5000, 10000]
        random.seed(42)
        test_arrays = [
                (size, random.sample(range(500000), size))
                for size in sizes
        ]

        merge_sizes, merge_times = run_merge_sort(test_arrays)
        quick_sizes, quick_times = run_quick_sort(test_arrays)
        hybrid_sizes, hybrid_times = run_hybrid_merge_sort(test_arrays, threshold=6)
        bubble_sizes, bubble_times = run_bubble_sort(test_arrays)
        insertion_sizes, insertion_times = run_insertion_sort(test_arrays)
        selection_sizes, selection_times = run_selection_sort(test_arrays)
        heap_sizes, heap_times = run_heap_sort(test_arrays)
        plt.style.use("dark_background")

        plt.plot(merge_sizes, merge_times, marker="o",
                color="#00FFFF", label="Merge Sort")

        plt.plot(quick_sizes, quick_times, marker="o",
                color="#FB00FF", label="Quick Sort")

        plt.plot(hybrid_sizes, hybrid_times, marker="o",
                color="#FFFF00", label="Hybrid Merge Sort")

        plt.plot(bubble_sizes, bubble_times, marker="o",
                color="#00FF48", label="Bubble Sort")

        plt.plot(insertion_sizes, insertion_times, marker="o",
                color="#0400FF", label="Insertion Sort")

        plt.plot(selection_sizes, selection_times, marker="o",
                color="#FF5500", label="Selection  Sort")

        plt.plot(heap_sizes, heap_times, marker="o",
                color="#F6FAF9", label="Heap Sort")


        
        plt.title("Sorting Algorithms Comparison")
        plt.xlabel("Input size (N)")
        plt.ylabel("Execution time (ms)")
        plt.grid(True)
        plt.yscale("log")
        plt.legend()
        plt.show()
        


if __name__ == "__main__":
        main()