# Class node, store information of a puzzle node
class node:	
	def __init__(self, matrix, emptyTilePos, cost, level, parent, prevMove):
		self.matrix = matrix					# matrix representation of the puzzle
		self.emptyTilePos = emptyTilePos		# position of empty tile
		self.cost = cost						# c(i) = f(i) + g(i)
		self.level = level						# depth from root
		self.parent = parent					# node of parent
		self.prevMove = prevMove				# previous move of empty tile to reach this node

	# set priority when enqueue a node to the priority queue based on cost
	def __lt__(self, next):
		if self.cost == next.cost:
			return self.level > next.level
		return self.cost < next.cost