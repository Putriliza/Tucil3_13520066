import time

import copy
from inputPuzzle import *
from queue import PriorityQueue


class node:	
	def __init__(self, puzzle, emptyTilePos, cost, level, parent):
		self.puzzle = puzzle
		self.parent = parent
		self.emptyTilePos = emptyTilePos
		self.cost = cost
		self.level = level

	def __lt__(self, nxt):
		return self.cost < nxt.cost

def calculateCost(puzzle) -> int:
	cost = 0
	for i in range(n):
		for j in range(n):
			if (puzzle[i][j] != final[i][j]):
				if puzzle[i][j] == 16:
					continue
				cost += 1
				
	return cost

def newNode(newTilePos, liveNode) -> node:

	new_puzzle = copy.deepcopy(liveNode.puzzle)

	x1, y1 = liveNode.emptyTilePos
	x2, y2 = newTilePos
	new_puzzle[x1][y1], new_puzzle[x2][y2] = new_puzzle[x2][y2], new_puzzle[x1][y1]

	cost = calculateCost(new_puzzle)

	level = liveNode.level + 1
	cost = cost + level		# g + f
	new_node = node(new_puzzle, newTilePos,
					cost, level, liveNode)
	return new_node

def printPuzzle(puzzle):
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == 16:
                print("-", end=" ")
            else:
                print("%d " % (puzzle[i][j]), end = " ")
			
        print()

def isValid(x, y):
	return x >= 0 and x < n and y >= 0 and y < n

def printRute(root):
	
	if root == None:
		return
	printRute(root.parent)
	print(f"Cost: {root.cost}, Level: {root.level}")
	printPuzzle(root.puzzle)
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
				global totalNodes
				totalNodes += 1
				pq.put(child)

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


n = 4

row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

totalNodes = 0

initial = inputFromFile("t4.txt")

final = [[ 1, 2, 3, 4],
		 [5, 6, 7, 8],
		 [9, 10, 11 , 12],
		 [13, 14, 15, 16]]

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