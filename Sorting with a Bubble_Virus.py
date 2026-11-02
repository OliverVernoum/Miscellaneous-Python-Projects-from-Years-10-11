def bubble_sort(arr):

    for n in range(len(arr)-1, 0, -1):
        swapped = False       
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
            
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                
                swapped = True

                print(arr)

        if not swapped:
            bubble_sort(arr)
arr = [1,2,3,4,5,4,3,2,1,6,7,4,7,8,9,3,4,5,6,7,8,5,3,6,8,9,8,7,6,3,5,67,3,5,8,4,7,9,4,2,3,5,6,12,3,6,3,6,9,6,4,6,9,5,4,54,566,787,85,3,4,668,6,75,6,53,54,668,67,8,75,6354,567,436,547,567,546,547,657,453,5,7567,56,54,567,563734,54,567,68,84,15,2436,26,1,1124,356,243,53154,54,615,4,632,5,64,6]
print(f"Unsorted algorithm is: {arr}")
bubble_sort(arr)

