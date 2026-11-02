import time

def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                print(arr)
                time.sleep(0.002)
        if not swapped:
            break


arr = [5,7,2,34,7,9,5,2,56,7,4,4,7,8,5,6,8,4,7,8,3,7,9,4,3,2,5,3,8,7,1,39,7,1,3,8,43,8,4,36,4,7,65,4,8,6,4,7,6,4,8,4,5,4,5,4,6,2,8,9,3,7,90,4,3,8,0,6,2,8,3,7,90,3,8,9,]

print(f"Unsorted list: {arr}")
bubble_sort(arr)
print(f"Sorted list: {arr}")

