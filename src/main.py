import time
import numpy as np

import copy
from inputPuzzle import *
from queue import PriorityQueue
from node import *
from helper import *
from solver import *


n = 4
initial = inputFromFile("t3.txt")


print("Initial Matrix:")
printmatrix(initial)
print()
for i in range(1, n**2+1):
	print(f"{i} = {kurangI(initial, i)}")
print(f"SumKurangI+X = {SumKurangIplusX(initial)}")
print()

if (isReachable(initial)):
	print("THIS PUZZLE CAN BE SOLVED :D\n")
	start = time.time()
	solution, totalNodes = solve(initial)
	end = time.time()
	printRute(solution)
	print("---------------------------------------------------")
	print(f"Time elapsed 		: {end-start} seconds")
	print(f"Total nodes raised 	: {totalNodes}")
else:
	print("THIS PUZZLE CAN NOT BE SOLVED :(")