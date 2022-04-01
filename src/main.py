def getXPos2D(puzzle, x):
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == x:
                return [i, j]

def getXPosition(puzzle, x):
	x1, x2 = getXPos2D(puzzle, x)
	return x1 * n + x2

def SumKurangIplusX(puzzle):
    SumKurangI = 0
    for i in range(1, n**2+1):
        kurangI = 0
        for j in range (1, i):
            if getXPosition(puzzle, j) > getXPosition(puzzle, i):
                kurangI += 1
        SumKurangI += kurangI
    x1, x2 = getXPos2D(puzzle, 16)
    X = (x1 + x2) % 2
    return SumKurangI + X

def isReachable(puzzle):
    return SumKurangIplusX(puzzle) % 2 == 0