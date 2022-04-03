import time
import os.path
from inputPuzzle import *
from node import *
from helper import *
from solver import *


print("------------------WELCOME TO 15 PUZZLE SOLVER----------------------")
print("""

 ██╗███████╗    ██████╗ ██╗   ██╗███████╗███████╗██╗     ███████╗
███║██╔════╝    ██╔══██╗██║   ██║╚══███╔╝╚══███╔╝██║     ██╔════╝
╚██║███████╗    ██████╔╝██║   ██║  ███╔╝   ███╔╝ ██║     █████╗  
 ██║╚════██║    ██╔═══╝ ██║   ██║ ███╔╝   ███╔╝  ██║     ██╔══╝  
 ██║███████║    ██║     ╚██████╔╝███████╗███████╗███████╗███████╗
 ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝
                                                                 
""")

n = 4			# puzzle size is n x n
isRun = True

while(isRun):
	print("You can use initial puzzle from")
	print("1. File")
	print("2. Randomizer")
	opsi = int(input("Choose initial puzzle from: (1-2) \n>> "))
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
		print("Nilai Kurang(i)")
		for i in range(1, n**2+1):
			print(f"Kurang({i}) = {kurangI(initial, i)}")
		print(f"SumKurangI+X = {SumKurangIplusX(initial)}")
		print()

		if (isReachable(initial)):
			print("THIS PUZZLE IS SOLVEABLE:D\n")
			print("Please wait for a while...\n")
			start = time.time()
			solution, totalNodes = solve(initial)
			end = time.time()
			printRute(solution)
			print("---------------------------------------------------")
			print(f"Time elapsed 		: {end-start} seconds")
			print(f"Total nodes raised 	: {totalNodes}")
		else:
			print("THIS PUZZLE IS NOT SOLVEABLE :(")
		print()
	
	loop = input("Wanna try another puzzle? (y/n) \n>> ")
	if (loop.upper() == "Y"):
		isRun = True
		print()
	else:
		print("--------------------THANK YOU--------------------")
		isRun = False
	