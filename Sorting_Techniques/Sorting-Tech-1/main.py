from bubble_sort import run_bubble_sort
from insertion_sort import run_insertion_sort
from selection_sort import run_selection_sort
import matplotlib.pyplot as plt


def main():
    run_bubble_sort()
    run_insertion_sort()
    run_selection_sort()
    plt.title("Sorting Algorithms Comparison")
    plt.show()
    


if __name__ == "__main__":
    main()