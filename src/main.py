from mimetypes import init
import time
import os.path

from inputPuzzle import *
from node import *
from helper import *
from solver import *

n = 4

print("------------------WELCOME TO 15 PUZZLE SOLVER----------------------")
print("""

 ██╗███████╗    ██████╗ ██╗   ██╗███████╗███████╗██╗     ███████╗
███║██╔════╝    ██╔══██╗██║   ██║╚══███╔╝╚══███╔╝██║     ██╔════╝
╚██║███████╗    ██████╔╝██║   ██║  ███╔╝   ███╔╝ ██║     █████╗  
 ██║╚════██║    ██╔═══╝ ██║   ██║ ███╔╝   ███╔╝  ██║     ██╔══╝  
 ██║███████║    ██║     ╚██████╔╝███████╗███████╗███████╗███████╗
 ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝
                                                                 
""")

isRun = True

while(isRun):
	print("You can use initial puzzle from")
	print("1. File")
	print("2. Randomizer")
	opsi = int(input("Choose initial puzzle from: "))
	inputExist = False

	if opsi == 1:
		filename = input("Enter filename: ")
		if (os.path.exists("../test/" + filename)):
			initial = inputFromFile(filename)
			inputExist = True
		else:
			print("File not found")
	elif opsi == 2:
		initial = inputFromRandom()
		inputExist = True
	else:
		print("Invalid input")

	print()
	if (inputExist):
		print("Initial Puzzle:")
		printmatrix(initial)
		print()
		for i in range(1, n**2+1):
			print(f"{i} = {kurangI(initial, i)}")
		print(f"SumKurangI+X = {SumKurangIplusX(initial)}")
		print()

		if (isReachable(initial)):
			print("THIS PUZZLE IS SOLVEABLE:D\n")
			print("Please wait for a while...")
			start = time.time()
			solution, totalNodes = solve(initial)
			end = time.time()
			printRute(solution)
			print("---------------------------------------------------")
			print(f"Time elapsed 		: {end-start} seconds")
			print(f"Total nodes raised 	: {totalNodes}")
		else:
			print("THIS PUZZLE IS NOT SOLVEABLE :(")
	
	loop = input("Wanna try another puzzle? (y/n) ")
	if (loop.upper() == "Y"):
		isRun = True
	else:
		isRun = False
	