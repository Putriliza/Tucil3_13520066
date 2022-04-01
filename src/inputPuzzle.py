import random
import numpy as np

def inputFromFile(filename):
    dir = "../test/" + filename
    file = open(dir, "r")
    content =  (open(dir).read().split())
    file.close()
    puzzle = np.zeros((4,4), dtype=int)
    for i in range(0, 16):
        puzzle[i // 4, i % 4] = int(content[i])
    return puzzle

def inputFromRandom():
    tmp = random.sample(range(0, 16), 16)
    puzzle = np.zeros((4,4), dtype=int)
    for i in range(0, 16):
        puzzle[i // 4, i % 4] = tmp[i]
    return puzzle