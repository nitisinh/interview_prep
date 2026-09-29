class sorter:
    def __init__(self):
        pass
    """
    Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-1-i): # -1 because we don't need to compare the last element, -i because we don't need to compare the already sorted elements
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    """
    Merge sort is a divide-and-conquer algorithm that divides the input array into two halves,
    calls itself for the two halves, and then merges the two sorted halves.
    """
    def merge_sort(self, arr):
        pass
    def quick_sort(self, arr):
        pass
    def heap_sort(self, arr):
        pass


if __name__ == "__main__":
    s = sorter()
    print(s.bubble_sort([64, 34, 25, 12, 22, 11, 90]))
