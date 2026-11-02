#Merge sort


i = 0

def merge_sort(arr1, arr2):
    arr3 = []
    i = j = 0
    for i in range (len(arr1)):
        if arr1[i] > arr2[i]:
            arr3.append(arr1[i])
            arr3.append(arr2[i])
        else:
            arr3.append(arr2[i])
            arr3.append(arr1[i])
    print(arr3)


        arr3=arr3(arr2(i), arr1(i))
        i +=1
    print(arr3)


arr1 = [1,3,2,8,99,44,77,2]
arr2 = [7,33,8,22,9,44,7,11,88]
arr3=[]

merge_sort(arr1,arr2)
print(arr3)
