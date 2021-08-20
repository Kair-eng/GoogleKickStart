import copy
def makeMatrix(y):
    matrix = []
    for I in range(y):
        matrix.append([int(j) for j in input().split()])
    return matrix

def sizeIt(matrix):
    mX = sizeMatrixX(matrix)
    mY = sizeMatrixY(matrix)
    return (mX, mY)

#Horizontal
def sizeMatrixX(m):
    matrix = copy.deepcopy(m)
    x, y = len(m[0]), len(m)
    i, j = 0, 0
    while i < y:
        j = 0
        while j < x:
            if m[i][j] == 0:
                matrix[i][j] = (0,0)
                j += 1
                continue
            length = findEndX(m, i, j)
            for I in range(j, j + length):
                #Left/Right Ends
                matrix[i][I]=(I - j + 1, length - (I - j))
            j += length
        i += 1
    return matrix
    
def findEndX(m, i, j):
    length = 1
    for k in range(j + 1, len(m[0])):
        if m[i][k] == 1:
            length += 1
        else:
            break
    return length

#Vertical    
def sizeMatrixY(m):
    matrix = copy.deepcopy(m)
    x, y = len(m[0]), len(m)
    i, j = 0, 0
    while j < x:
        i = 0
        while i < y:
            if m[i][j] == 0:
                matrix[i][j] = (0, 0)
                i += 1
                continue
            length = findEndY(m, i, j)
            for I in range(i, i + length):
                #Top/Bottom Ends
                matrix[I][j] = (I - i + 1, length - (I - i))
            i += length
        j += 1
    return matrix


def findEndY(m, i, j):
    length = 1
    for k in range(i + 1, len(m)):
        if m[k][j] == 1 :
            length += 1
        else:
            break
    return length


##############
#Counter
def sumIt(n):
    return n - 1

def compute(i,j):
    cumulative = 0
    if i <= 1 or j <= 1:
        return 0
    d1, d2 = max(i,j), min(i,j)
    if d2 * 2 <= d1:
        cumulative += sumIt(d2)
    else:
        cumulative += sumIt(int(d1/2))
        
    d1, d2 = d2, d1
    
    if d2 * 2 <= d1:
        cumulative += sumIt(d2)
    else:
        cumulative += sumIt(int(d1/2))
        
    return cumulative

def check(mX, mY):
    cumulative = 0
    cumulative += compute(mX[0],mY[0])
    cumulative += compute(mX[1],mY[0])
    cumulative += compute(mX[0],mY[1])
    cumulative += compute(mX[1],mY[1])
    return cumulative

N = int(input())


for I in range(N):
    y,x = [int(j) for j in input().split()]
    matrix = makeMatrix(y)
    mX, mY = sizeIt(matrix)
    counter = 0
    for i in range(y):
        for j in range(x):
            counter += check(mX[i][j], mY[i][j])
    print(f"Case #{I + 1}: {counter}")
