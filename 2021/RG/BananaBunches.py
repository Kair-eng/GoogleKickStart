def makeMatrix(bananas):
    size = len(bananas)
    X, Y = size, size
    Matrix = [[bananas[i] for i in range(X)] for _ in range(Y)]
    for i in range(size):
        for j in range(i+1, size):
            Matrix[i][j] += Matrix[i][j - 1]
            Matrix[j][i] = Matrix[i][j]
    return Matrix


T = int(input())
for i in range(T):
    i += 1
    N, SUM = [int(_) for _ in input().rstrip().split()]
    bananas = [int(_) for _ in input().rstrip().split()]
    Matrix = makeMatrix(bananas)
    totalCost = 999999
    choice = [-1, -1]
    for i in range(len(Matrix[0])):
        if totalCost == 1:
            break
        for j in range(i, len(Matrix[0])):
            if i == j and SUM == Matrix[i][j]:
                totalCost = 1
                choice = [i, j]
                break
            if SUM == Matrix[i][j] and totalCost > j - i + 1:
                totalCost = j - i + 1

            for gap in range(j + 2, len(Matrix[0])):
                for k in range(gap, len(Matrix[0])):
                    if SUM == Matrix[i][j]+Matrix[gap][k] and totalCost > j - i + 1 + k - gap + 1:
                        totalCost = j - i + 1 + k - gap + 1
    result = -1 if totalCost == 999999 else totalCost
    print(f"Case #{i}: {result}")
