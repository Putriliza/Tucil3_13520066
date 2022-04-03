n = 4       # Puzzle size is n x n

# Function to print matrix
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

# Recursive function to print the solution from root
def printRute(root):
	
	if root == None:
		return
	printRute(root.parent)
	print(f"LEVEL: {root.level}, PREVIOUS MOVE: {root.prevMove}")
	printmatrix(root.matrix)
	print()


# Return true if this position are in valid in matrix
def isValid(position) -> bool:
    return position[0] >= 0 and position[0] < n and position[1] >= 0 and position[1] < n

# Return tuple (i, j) of position of x in matrix
def getXPos2D(matrix, x):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == x:
                return (i, j)

# Return posion of x in matrix (0-15)
def getXPos(matrix, x) -> int:
	x1, x2 = getXPos2D(matrix, x)
	return x1 * n + x2

# Count tile with number j which i > j but position(j)<position(i)
def kurangI(matrix, i) -> int:
	kurangI = 0
	for j in range (1, i):
		if getXPos(matrix, j) > getXPos(matrix, i):
			kurangI += 1
	return kurangI

# Sum of kurangI(i) + x for i from 1 to n**2
def SumKurangIplusX(matrix) -> int:
    SumKurangI = 0
    for i in range(1, n**2+1):
        SumKurangI += kurangI(matrix, i)
    x1, y1 = getXPos2D(matrix, n**2)    # empty tile position
    X = (x1 + y1) % 2                   # 1 if empty tile are in shadow area, 0 if not
    return SumKurangI + X

# Return true if matrix is solvable
def isReachable(matrix) -> bool:
    return SumKurangIplusX(matrix) % 2 == 0