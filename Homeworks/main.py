from collections import deque
from enum import Enum

pattern = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 2 ,1 ,0 ,1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Direction(Enum):
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP = (-1, 0)

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(cell) for cell in row))
        
def move(current_row, current_col, pattern, moves_stack):
    for direction in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
        next_row = current_row + direction.value[0]
        next_col = current_col + direction.value[1]
        
        if pattern[next_row][next_col] == 2:
            return next_row, next_col
        
        if pattern[next_row][next_col] == 0:
            moves_stack.append((current_row, current_col))
            return next_row, next_col
    
    return current_row, current_col

rows = len(pattern)
cols = len(pattern[0])

start = pattern[1][1]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up

# left
# right
# up
# down

current_row, current_col = 1, 1
last_move = ""
curr_position = start

moves_stack = deque()

while True:
    if pattern[current_row][current_col] == 2:
        print("You won!")
        break
    elif pattern[current_row][current_col] == 0:
        pattern[current_row][current_col] = 'S'
    
    print("*"  * 10)
    print_matrix(pattern)
    print("*"  * 10)
    
    next_row, next_col = move(current_row, current_col, pattern, moves_stack)
    
    if (next_row, next_col) != (current_row, current_col):
        current_row, current_col = next_row, next_col
        continue
    
    pattern[current_row][current_col] = 'X'
    prev_move = moves_stack.pop()
    current_row, current_col = prev_move[0], prev_move[1]
    
   
