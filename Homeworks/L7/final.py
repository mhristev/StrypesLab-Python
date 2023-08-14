from collections import deque
from enum import Enum

WALL = '#'
PATH = ''
WALKED = '.'
BACK_WALKED = 'x'
TRESSURE = 'g'

class Direction(Enum):
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP = (-1, 0)

class MazeSolver:
    def __init__(self, pattern):
        self.pattern = pattern
        self.moves_stack = deque()
        self.current_row = 0
        self.current_col = 0

    def move(self):
        for direction in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
            next_row = self.current_row + direction.value[0]
            next_col = self.current_col + direction.value[1]
            
            if self.pattern[next_row][next_col] == TRESSURE:
                return next_row, next_col
            
            if self.pattern[next_row][next_col] == PATH:
                self.moves_stack.append((self.current_row, self.current_col))
                return next_row, next_col
        
        return self.current_row, self.current_col
    
    def solveMaze(self, x, y):
        self.current_row = x
        self.current_col = y
        while True:
            if self.pattern[self.current_row][self.current_col] == TRESSURE:
                self.print_matrix()
                print("You won!")
                break
            elif self.pattern[self.current_row][self.current_col] == PATH:
                self.pattern[self.current_row][self.current_col] = WALKED
            
            next_row, next_col = self.move()
            
            if (next_row, next_col) != (self.current_row, self.current_col):
                self.current_row, self.current_col = next_row, next_col
                continue
            
            self.pattern[self.current_row][self.current_col] = BACK_WALKED
            prev_move = self.moves_stack.pop()
            self.current_row, self.current_col = prev_move
    
    def print_matrix(self):
        for row in self.pattern:
            print(' '.join(map(str, row)))



pattern = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '#'],
    ['#', '', '#', '#', '#', '#', '#', '#', '#', '', '#', '', '#', '#', '#', '#', '#', '#', '', '#'],
    ['#', '', '', '', '', '', '', '', '#', '', '#', '', '#', '', '#', '#', 'g' ,'#' ,'' ,'#'],
    ['#', '', '#', '#', '#', '#', '#', '#', '#', '', '#', '', '#', '', '#', '#', '', '#', '', '#'],
    ['#', '', '#', '', '', '', '', '', '', '', '', '', '#', '', '#', '#', '', '#', '', '#'],
    ['#', '', '#', '', '#', '#', '#', '', '#', '#', '#', '#', '#', '', '#', '#', '', '#', '', '#'],
    ['#', '', '#', '', '#', '', '#', '', '#', '', '', '', '', '', '#', '#', '', '#', '', '#'],
    ['#', '', '', '', '#', '', '', '', '', '', '#', '', '', '', '', '', '', '', '', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]



solver = MazeSolver(pattern)
solver.solveMaze(1, 1)
   
