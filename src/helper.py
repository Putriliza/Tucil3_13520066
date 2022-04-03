n = 4

def printmatrix(matrix):
    for i in range(n):
        print("-----" * n)
        for j in range(n):
            print("|", end=" ")
            if matrix[i][j] == n**2:
                print("  ", end=" ")
            else:
                print(str(matrix[i][j]).ljust(2), end = " ")
        print("|")
    print("-----" * n)

def printRute(root):
	
	if root == None:
		return
	printRute(root.parent)
	print(f"LEVEL: {root.level}, PREVIOUS MOVE: {root.prevMove}")
	printmatrix(root.matrix)
	print()

def isValid(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def getXPos2D(matrix, x):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == x:
                return [i, j]

def getXPos(matrix, x):
	x1, x2 = getXPos2D(matrix, x)
	return x1 * n + x2

def kurangI(matrix, i):
	kurangI = 0
	for j in range (1, i):
		if getXPos(matrix, j) > getXPos(matrix, i):
			kurangI += 1
	return kurangI

def SumKurangIplusX(matrix):
    SumKurangI = 0
    for i in range(1, n**2+1):
        SumKurangI += kurangI(matrix, i)
    x1, x2 = getXPos2D(matrix, n**2)
    X = (x1 + x2) % 2
    return SumKurangI + X

def isReachable(matrix):
    return SumKurangIplusX(matrix) % 2 == 0