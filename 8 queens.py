def isSafe(mat, row, col):
    n = len(mat)
    for i in range(row):
        if mat[i][col]:
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if mat[i][j]:
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if mat[i][j]:
            return False
        i -= 1
        j -= 1
    return True


def PlaceQueen(row, mat):
    n = len(mat)
    if row == n:
        return True
    for i in range(n):
        if isSafe(mat, row, i):
            mat[row][i] = 1
            if PlaceQueen(row + 1, mat):
                return True
            mat[row][i] = 0
    return False


def queens():
    n = int(input())

    mat = [[0] * n for _ in range(n)]

    PlaceQueen(0, mat)

    return mat


if __name__ == "__main__":
    res = queens()
    for v in res:
        print(" ".join(map(str, v)))
