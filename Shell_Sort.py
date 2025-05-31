def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            current = arr[i]
            position = i
            while position >= gap and arr[position - gap] > current:
                arr[position] = arr[position - gap]
                position -= gap
            arr[position] = current
        gap //= 2
    return arr

arr = [8, 5, 3, 7, 2, 6, 4, 1]
print(shellSort(arr))