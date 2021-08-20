import heapq
import copy


def makeMatrix(y):
    matrix = []
    for I in range(y):
        matrix.append([int(j) for j in input().split()])
    return matrix


N = int(input())


def checkLeft(y, x, ij):
    if ij[1] <= 0:
        return 0
    return 1


def checkRight(y, x, ij):
    if ij[1] >= x-1:
        return 0
    return 1


def checkTop(y, x, ij):
    if ij[0] <= 0:
        return 0
    return 1


def checkBottom(y, x, ij):
    if ij[0] >= y-1:
        return 0
    return 1


def populate(originalCoord, newCoord, matrix, heapStruct, processed):
    (y, x), (i, j) = originalCoord, newCoord
    if processed[i][j]:
        return 0
    originalScore, score = matrix[y][x], matrix[i][j]
    recomputed = originalScore - score - 1

    if recomputed <= 0:
        return 0

    heapq.heappush(heapStruct, (-1 * (originalScore - 1), (i, j)))
    matrix[i][j] = originalScore - 1
    return recomputed


for I in range(N):
    y, x = [int(j) for j in input().split()]

    matrix = makeMatrix(y)
    processed = copy.deepcopy(matrix)
    for i in range(y):
        for j in range(x):
            # To halt BFS
            processed[i][j] = 0

    h = []
    for i in range(y):
        for j in range(x):
            heapq.heappush(h, (-1 * matrix[i][j], (i, j)))

    accumulate = 0
    while len(h) > 0:
        element = heapq.heappop(h)
        height, (i, j) = element

        processed[i][j] = 1
        # Check neighbours
        if checkTop(y, x, (i, j)):
            accumulate += populate((i, j), (i - 1, j), matrix, h, processed)
        if checkBottom(y, x, (i, j)):
            accumulate += populate((i, j), (i + 1, j), matrix, h, processed)

        if checkLeft(y, x, (i, j)):
            accumulate += populate((i, j), (i, j - 1), matrix, h, processed)
        if checkRight(y, x, (i, j)):
            accumulate += populate((i, j), (i, j + 1), matrix, h, processed)

    print(f"Case #{I + 1}: {accumulate}")
