from collections import deque


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


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(cell) for cell in row))
        

def move(direction):
    pass
    

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

while True:
    print("*"  * 10)
    print_matrix(pattern)
    print("*"  * 10)
    
    if pattern[current_row][current_col] == 2:
        print("You won!")
        break
    elif pattern[current_row][current_col] == 0:
        pattern[current_row][current_col] = 'S'
        
    next_row = current_row + directions[2][0]
    next_col = current_col + directions[2][1]
   
    if (pattern[next_row][next_col] == 2):
        # print(f'next row: {next_row}, next col: {next_col}')
        # print(f'curr row: {current_row}, curr col: {current_col}')
        current_col = next_col
        current_row = next_row
        continue
    
    if (pattern[next_row][next_col] == 0):
        current_row = next_row
        current_col = next_col
        last_move = "left"
        continue
    
    next_row = current_row + directions[0][0]
    next_col = current_col + directions[0][1]
    
    if (pattern[next_row][next_col] == 2):
        current_col = next_col
        current_row = next_row
        continue
    
    if (pattern[next_row][next_col] == 0):
        last_move = "right"
        current_row = next_row
        current_col = next_col
        continue
    
    next_row = current_row + directions[3][0]
    next_col = current_col + directions[3][1]

    if (pattern[next_row][next_col] == 2):
        # print("TUKKK")
        # print(f'next row: {next_row}, next col: {next_col}')
        # print(f'curr row: {current_row}, curr col: {current_col}')
        current_col = next_col
        current_row = next_row
        continue
    
    if (pattern[next_row][next_col] == 0):
        current_row = next_row
        current_col = next_col
        last_move = "up"
        continue
    
    next_row = current_row + directions[1][0]
    next_col = current_col + directions[1][1]

    if (pattern[next_row][next_col] == 2):
        current_col = next_col
        current_row = next_row

        continue
    
    if (pattern[next_row][next_col] == 0):
        current_row = next_row
        current_col = next_col
        last_move = "down"
        continue
    
    # part 2
    
    if last_move != "":
        if last_move == 'right':
            next_row = current_row + directions[2][0]
            next_col = current_col + directions[2][1]
        elif last_move == 'left':
            next_row = current_row + directions[0][0]
            next_col = current_col + directions[0][1]
        elif last_move == 'down':
            next_row = current_row + directions[3][0]
            next_col = current_col + directions[3][1]
        elif last_move == 'up':
            next_row = current_row + directions[1][0]
            next_col = current_col + directions[1][1]
        if (pattern[next_row][next_col] == 'S'):
            pattern[current_row][current_col] = 'X'
            current_row = next_row
            current_col = next_col
            last_move = ""
            continue
    
    next_row = current_row + directions[2][0]
    next_col = current_col + directions[2][1]
    
    if (pattern[next_row][next_col] == 'S'):
        pattern[current_row][current_col] = 'X'
        current_row = next_row
        current_col = next_col
        continue
    

    
    next_row = current_row + directions[0][0]
    next_col = current_col + directions[0][1]
    
    if (pattern[next_row][next_col] == 'S'):
        pattern[current_row][current_col] = 'X'
        current_row = next_row
        current_col = next_col
        continue
    
    
    next_row = current_row + directions[3][0]
    next_col = current_col + directions[3][1]
    
    if (pattern[next_row][next_col] == 'S'):
        pattern[current_row][current_col] = 'X'
        current_row = next_row
        current_col = next_col
        continue
    
    next_row = current_row + directions[1][0]
    next_col = current_col + directions[1][1]
    
    if (pattern[next_row][next_col] == 'S'):
        pattern[current_row][current_col] = 'X'
        current_row = next_row
        current_col = next_col
        continue
    
#  ne e podredeno left right up down 2rata chast ot koda
    

    
    
    
   
