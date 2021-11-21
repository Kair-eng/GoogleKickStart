T = int(input())
for CASE in range(T):

    # L B R T
    dims = []
    X, Y = -1, -1

    K = int(input())
    X_coordinate = []
    Y_coordinate = []
    for i in range(K):
        L, B, R, T = [int(_) for _ in input().split()]
        X_coordinate.append((L, 0, i))
        X_coordinate.append((R, 1, i))
        Y_coordinate.append((B, 0, i))
        Y_coordinate.append((T, 1, i))
    X_coordinate = sorted(X_coordinate, key=lambda coord: coord[0])
    Y_coordinate = sorted(Y_coordinate, key=lambda coord: coord[0])

    Behind, Ahead = 0, K

    for x in range(len(X_coordinate)):
        if Ahead - Behind <= 0:
            break
        X, Side, Box = X_coordinate[x]
        if Side == 0:
            Ahead -= 1
        else:
            Behind += 1

    Behind, Ahead = 0, K
    for y in range(len(Y_coordinate)):
        if Ahead - Behind <= 0:
            break
        Y, Side, Box = Y_coordinate[y]
        if Side == 0:
            Ahead -= 1
        else:
            Behind += 1

    print(f"Case #{CASE+1}: {X} {Y}")
