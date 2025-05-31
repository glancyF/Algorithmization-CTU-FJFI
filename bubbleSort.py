def bubble_sort(arr):
    n = len(arr)
    count = 0
    for run in range(n):
        for i in range(n-1-run):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
                count+=1
    return arr,count

arr = [5, 1, 4, 2, 8]
sorted_arr, swaps = bubble_sort(arr)
print(swaps)
print(sorted_arr)