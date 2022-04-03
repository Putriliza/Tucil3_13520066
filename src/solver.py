import time
import numpy as np

import copy

from sklearn.metrics import top_k_accuracy_score
from inputPuzzle import *
from queue import PriorityQueue
from node import *
from helper import *

row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

final = np.array([[ 1, 2, 3, 4],
		 [5, 6, 7, 8],
		 [9, 10, 11 , 12],
		 [13, 14, 15, 16]])

visitedMatrix = {}

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

def calculateCost(matrix) -> int:
	cost = 0
	for i in range(n):
		for j in range(n):
			if (matrix[i][j] != final[i][j]):
				if matrix[i][j] == 16:
					continue
				cost += 1
				
	return cost

def solve(initial):
	pq = PriorityQueue()
	totalNodes = 0

	cost = calculateCost(initial)
	
	emptyTilePos = getXPos2D(initial, 16)
	root = node(initial, emptyTilePos, cost, 0, None)
	pq.put(root)

	while not pq.empty():
		liveNode = pq.get()

		if liveNode.cost == liveNode.level: # g = 0, tidak ada missplaced, ditemukan
			return liveNode, totalNodes
            
		for i in range(n):
			newTilePos = [
                liveNode.emptyTilePos[0] + row[i],
                liveNode.emptyTilePos[1] + col[i], ]
			if isValid(newTilePos[0], newTilePos[1]):
				child = newNode(newTilePos, liveNode)
				if child != None:
					pq.put(child)
					totalNodes += 1
