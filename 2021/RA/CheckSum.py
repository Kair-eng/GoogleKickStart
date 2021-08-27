import heapq
import copy

def makeMatrix(y):
    matrix = []
    for I in range(y):
        matrix.append([int(j) for j in input().split()])
    return matrix

def propagate(ij,  processed, columns, rows):
    i, j = ij
    if processed[i][j] == 1:
        return

    processed[i][j] = 1
    if(ij in columns[j]):
        columns[j].remove(ij)
    if(ij in rows[i]):
        rows[i].remove(ij)
    
    
    if len(columns[j]) == 1:
        i1, j1 = columns[j].pop()
        propagate((i1,j1),  processed, columns, rows)
    
    if len(rows[i]) == 1:
        i2, j2 = rows[i].pop()
        propagate((i2,j2),  processed, columns, rows)

def clear1Cells(processed, columns, rows):
    keepRunning = 1
    while keepRunning:
        keepRunning = 0
        for i in range(len(columns)):
            if(len(columns[i])==1):
                keepRunning = 1
                propagate(list(columns[i])[0],processed,columns,rows)
        for i in range(len(rows)):
            if(len(rows[i])==1):
                keepRunning = 1
                propagate(list(rows[i])[0],processed,columns,rows)

N = int(input())

for I in range(N):
    NxN =  int(input())

    matrix = makeMatrix(NxN)
    costMatrix = makeMatrix(NxN)
    input()
    input()
    processed = copy.deepcopy(matrix)
    columns = [set() for i in range(NxN)]
    rows = [set() for i in range(NxN)]
    h = []

    #Create priority to process
    for i in range(NxN):
        for j in range(NxN):
            if matrix[i][j] == -1:
                columns[j].add((i,j))
                rows[i].add((i,j))
                heapq.heappush(h, (costMatrix[i][j], (i, j)))
            processed[i][j] = 0

    accumulate = 0
    
    #Clear all 1 cell Rows or 1 cell Columns
    clear1Cells(processed,columns,rows)
    while len(h) > 0:


        #Count the current lowest cell
        element = heapq.heappop(h)
        timeCost, (i, j) = element
        if(processed[i][j]):
            continue
        


        # Propagate
        accumulate += timeCost
        propagate((i,j),processed,columns,rows)
        clear1Cells(processed,columns,rows)
    print(f"Case #{I + 1}: {accumulate}")