def merge_sort(A):
    B = [0] * len(A)

    def merge(A, B, start, mid, end):
        i = start
        j = mid
        for k in range(start, end):
            if i < mid and (j >= end or A[i] <= A[j]):
                B[k] = A[i]
                i += 1
            else:
                B[k] = A[j]
                j += 1

    def sort(A, B, start, end):
        if end - start <= 1:
            return
        mid = (start + end) // 2
        sort(A, B, start, mid)
        sort(A, B, mid, end)
        merge(A, B, start, mid, end)
        for k in range(start, end):
            A[k] = B[k]

    sort(A, B, 0, len(A))

