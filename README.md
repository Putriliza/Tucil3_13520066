# 15-PUZZLE SOLVER USING BRANCH AND BOUND ALGORITHM

### GENERAL INFORMATION
This is a program to solve the 15-Puzzle problem using branch and bound algorithm. The bound value of each node is the sum of the costs required to reach a node x from the root (depth level) with the estimated cost of node x to reach the goal. The estimated cost used is the number of  tiles that are missplaced to the goal state. This program use priority queue to store the raised nodes with the lower cost as priority.

This is the goal state for all instances of the 15-puzzle problem <br />
![goalstate](docs/Goal%20State.jpg)

### REQUIREMENTS
- [python 3](https://www.python.org/downloads/)
- [numpy](https://numpy.org/install/)


### HOW TO RUN
- First, clone this repository
    ```
    https://github.com/Putriliza/Tucil3_13520066.git
    ```
- Open in terminal
- Change directory to src
    ```
    cd src
    ```
- Then run
    ```
    python main.py
    ```

### USAGE
1. Once you run the ```main.py```, the program will ask you to choose the source for the initial state of puzzle.
    ```
    You can use initial puzzle from
    1. File
    2. Randomizer
    Choose initial puzzle from: (1-2)
    >>
    ```
2. If you choose from file, make sure the file is in ```\test``` folder. Then the program will ask you to input the filename and do not forget the file extensions.
WARNING: if you want to generate the initial puzzle with randomizer, it may took too long to solve the puzzle, sorry :( 
3. Then, program will show the result.

### AUTHOR
Putri Nurhaliza - 13520066 <br />
Tugas Kecil 3 IF2211 Algorithm Strategies <br />
Bandung Institute of Technology