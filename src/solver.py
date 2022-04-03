import numpy as np

import copy

from inputPuzzle import *
from queue import PriorityQueue
from node import *
from helper import *

final = np.array([[ 1, 2, 3, 4],
		 [5, 6, 7, 8],
		 [9, 10, 11 , 12],
		 [13, 14, 15, 16]])

direction = ['UP', 'RIGHT', 'DOWN', 'LEFT']

visitedMatrix = {}

def newNode(newEmptyTilePos, liveNode, prevMove) -> node:
	newMatrix = copy.deepcopy(liveNode.matrix)

	x1, y1 = liveNode.emptyTilePos
	x2, y2 = newEmptyTilePos
	newMatrix[x1][y1], newMatrix[x2][y2] = newMatrix[x2][y2], newMatrix[x1][y1]

	level = liveNode.level + 1						# f(i)
	missplaced = calculateMissplaced(newMatrix)		# g(i)
	cost = level + missplaced						# c(i) = f(i) + g(i)

	if (newMatrix.tobytes() in visitedMatrix):
		return None
	else:
		visitedMatrix[newMatrix.tobytes()] = True
		newnode = node(newMatrix, newEmptyTilePos, cost, level, liveNode, prevMove)
		return newnode

def calculateMissplaced(matrix) -> int:
	cost = 0
	for i in range(n):
		for j in range(n):
			if (matrix[i][j] != final[i][j]):
				if matrix[i][j] == n**2:
					continue
				cost += 1
				
	return cost

def move(currentPos, i):
	# i = 0: move up
	# i = 1: move right
	# i = 2: move down
	# i = 3: move left
	moverow = [-1, 0, 1, 0]
	movecol = [0, 1, 0, -1]

	x1, y1 = currentPos
	return [x1 + moverow[i], y1 + movecol[i]]

def solve(initial):
	pq = PriorityQueue()
	totalNodes = 0
	
	level = 0
	cost = calculateMissplaced(initial) + level
	emptyTilePos = getXPos2D(initial, n**2)
	root = node(initial, emptyTilePos, cost, level, None, None)
	pq.put(root)

	while not pq.empty():
		liveNode = pq.get()

		if liveNode.cost == liveNode.level: # g = 0, tidak ada missplaced, ditemukan
			return liveNode, totalNodes

		for i in range(4):
			newEmptyTilePos = move(liveNode.emptyTilePos, i)
			if isValid(newEmptyTilePos[0], newEmptyTilePos[1]):
				child = newNode(newEmptyTilePos, liveNode, direction[i])
				if child != None:
					pq.put(child)
					totalNodes += 1
