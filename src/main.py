import time
import numpy as np

import copy
from inputPuzzle import *
from queue import PriorityQueue


class node:	
	def __init__(self, matrix, emptyTilePos, cost, level, parent):
		self.matrix = matrix
		self.emptyTilePos = emptyTilePos
		self.cost = cost
		self.level = level
		self.parent = parent

	def __lt__(self, nxt):
		return self.cost < nxt.cost

def calculateCost(matrix) -> int:
	cost = 0
	for i in range(n):
		for j in range(n):
			if (matrix[i][j] != final[i][j]):
				if matrix[i][j] == 16:
					continue
				cost += 1
				
	return cost

def newNode(newTilePos, liveNode) -> node:

	newMatrix = copy.deepcopy(liveNode.matrix)

	x1, y1 = liveNode.emptyTilePos
	x2, y2 = newTilePos
	newMatrix[x1][y1], newMatrix[x2][y2] = newMatrix[x2][y2], newMatrix[x1][y1]

	cost = calculateCost(newMatrix)

	level = liveNode.level + 1
	cost = cost + level		# g + f

	if (newMatrix.tobytes() in visitedMatrix):
		return None
	else:
		visitedMatrix[newMatrix.tobytes()] = True
		new_node = node(newMatrix, newTilePos, cost, level, liveNode)
		return new_node

def printmatrix(matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 16:
                print("-", end=" ")
            else:
                print("%d " % (matrix[i][j]), end = " ")
			
        print()

def isValid(x, y):
	return x >= 0 and x < n and y >= 0 and y < n

def printRute(root):
	
	if root == None:
		return
	printRute(root.parent)
	print(f"Cost: {root.cost}, Level: {root.level}")
	printmatrix(root.matrix)
	print()

def solve(initial, emptyTilePos):
	pq = PriorityQueue()

	cost = calculateCost(initial)
	
	root = node(initial,
				emptyTilePos, cost, 0, None)
	pq.put(root)

	while not pq.empty():
		liveNode = pq.get()

		if liveNode.cost == liveNode.level: # g = 0, ditemukan
			printRute(liveNode)
			return

		for i in range(n):
			newTilePos = [
				liveNode.emptyTilePos[0] + row[i],
				liveNode.emptyTilePos[1] + col[i], ]
				
			if isValid(newTilePos[0], newTilePos[1]):
				child = newNode(newTilePos, liveNode)
				if child != None:
					pq.put(child)

					global totalNodes
					totalNodes += 1

def getXPos2D(matrix, x):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == x:
                return [i, j]

def getXPosition(matrix, x):
	x1, x2 = getXPos2D(matrix, x)
	return x1 * n + x2

def SumKurangIplusX(matrix):
    SumKurangI = 0
    for i in range(1, n**2+1):
        kurangI = 0
        for j in range (1, i):
            if getXPosition(matrix, j) > getXPosition(matrix, i):
                kurangI += 1
        SumKurangI += kurangI
    x1, x2 = getXPos2D(matrix, 16)
    X = (x1 + x2) % 2
    return SumKurangI + X

def isReachable(matrix):
    return SumKurangIplusX(matrix) % 2 == 0


n = 4

row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

totalNodes = 0

visitedMatrix = {}

initial = inputFromFile("t4.txt")

final = np.array([[ 1, 2, 3, 4],
		 [5, 6, 7, 8],
		 [9, 10, 11 , 12],
		 [13, 14, 15, 16]])

emptyTilePos = getXPos2D(initial, 16)

if (isReachable(initial)):
	start = time.time()
	solve(initial, emptyTilePos)
	end = time.time()
	print(f"SumKurangI+X = {SumKurangIplusX(initial)}")
	print(f"Time elapsed = {end - start} seconds")
	print(f"Total nodes = {totalNodes}")
else:
	print(f"SumKurangI+X = {SumKurangIplusX(initial)}")
	print("GABISA SAYY")