import numpy as np
import copy

from inputPuzzle import *
from queue import PriorityQueue
from node import *
from helper import *

# Store the final state of puzzle
final = np.array([[ 1, 2, 3, 4],
				  [5, 6, 7, 8],
				  [9, 10, 11 , 12],
				  [13, 14, 15, 16]])

# Store the name of direction of each move
direction = ['UP', 'RIGHT', 'DOWN', 'LEFT']

# Store the matrix that have been raised, unique
raisedMatrix = {}

# function to create new node
def newNode(liveNode, newEmptyTilePos, prevMove) -> node:
	newMatrix = copy.deepcopy(liveNode.matrix)

	x1, y1 = liveNode.emptyTilePos
	x2, y2 = newEmptyTilePos

	# change position of empty tile to the other tile based on previous move
	newMatrix[x1][y1], newMatrix[x2][y2] = newMatrix[x2][y2], newMatrix[x1][y1]

	level = liveNode.level + 1						# f(i)
	missplaced = calculateMissplaced(newMatrix)		# g(i)
	cost = level + missplaced						# c(i) = f(i) + g(i)

	if (newMatrix.tobytes() in raisedMatrix):
		# if matrix has been raised before, it wont be raised again
		return None
	else:
		# raised the new node
		raisedMatrix[newMatrix.tobytes()] = True
		newnode = node(newMatrix, newEmptyTilePos, cost, level, liveNode, prevMove)
		return newnode

# count how many missplaced tile in matrix
def calculateMissplaced(matrix) -> int:
	count = 0
	for i in range(n):
		for j in range(n):
			if (matrix[i][j] != final[i][j]):
				if matrix[i][j] == n**2:
					continue
				count += 1
	return count

# move empty tile to the position based on direction
def move(currentPos, i):
	# i = 0: move up
	# i = 1: move right
	# i = 2: move down
	# i = 3: move left
	moverow = [-1, 0, 1, 0]
	movecol = [0, 1, 0, -1]

	x1, y1 = currentPos
	return [x1 + moverow[i], y1 + movecol[i]]

# main algorithm to solve 15 puzzle based on Branch and Bound algorithm
def solve(initial):
	pq = PriorityQueue()
	totalNodes = 0
	level = 0
	cost = calculateMissplaced(initial) + level
	emptyTilePos = getXPos2D(initial, n**2)

	root = node(initial, emptyTilePos, cost, level, None, None)
	pq.put(root)

	# Loop until the prioqueue is empty or the goal is found
	while not pq.empty():
		# get the node with lowest cost
		liveNode = pq.get()

		if liveNode.cost == liveNode.level:
			# g = 0, no more missplaced tiles, goal found
			return liveNode, totalNodes

		for i in range(4):
			# move empty tile to the position based on 4 possible direction, and raised the new nodes
			newEmptyTilePos = move(liveNode.emptyTilePos, i)
			if isValid(newEmptyTilePos):
				child = newNode(liveNode, newEmptyTilePos, direction[i])
				if child != None:
					pq.put(child)
					totalNodes += 1
