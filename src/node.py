class node:	
	def __init__(self, matrix, emptyTilePos, cost, level, parent):
		self.matrix = matrix
		self.emptyTilePos = emptyTilePos
		self.cost = cost
		self.level = level
		self.parent = parent

	def __lt__(self, next):
		return self.cost < next.cost