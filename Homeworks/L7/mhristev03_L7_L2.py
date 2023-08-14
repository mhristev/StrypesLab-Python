"""
    Създайте итеративна реализиция на алгоритъма за обхождане на лабиринт. 
    Използвайте списък, за да симулирате програмния стек. 
    Създайте функция printMaze, която чертае стените с '#', необходеният път с ' ', 
    обходеният в права посока с '.', и в обратна посока с 'x' и целта с 'g'. 
    Когато целта е постигната, използвайте функцията за да разпечатате 
    текущото състояние на лабиринта. 
    Функцията за обхождане трябва да се казва solveMaze(x,y) 
    и да приема параметри начални координати на търсенето. 
    Файлът трябва да се казва XXXXX_L7_T2.py, където XXXXX е вашето потребителско име в пощата, 
    с която сте регистрирани и да приема от командния ред (със sys.argv) 
    начални координати на търсенето в лабиринта.

"""
import tkinter as tk
from collections import deque
from enum import Enum
import sys

WALL = '#'
PATH = ''
WALKED = '.'
RETRACE = 'x'
TREASURE = 'g'

class Direction(Enum):
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP = (-1, 0)

class MazeSolver:
    def __init__(self, root, pattern):
        self.maze = pattern
        self.moves_stack = deque()
        self.current_row = 0
        self.current_col = 0
        self.root = root
        
        self.canvas = tk.Canvas(root, width=650, height=350)
        self.canvas.pack()
        self.draw_maze()

        self.game_status_label = tk.Label(root, text='', font=('', 19))
        self.game_status_label.pack()
    
    def move(self):
        for direction in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
            next_row = self.current_row + direction.value[0]
            next_col = self.current_col + direction.value[1]
            
            if self.maze[next_row][next_col] == TREASURE:
                return next_row, next_col
            
            if self.maze[next_row][next_col] == PATH:
                self.moves_stack.append((self.current_row, self.current_col))
                return next_row, next_col
        
        return self.current_row, self.current_col
    
    def draw_maze(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                x1 = col * 30
                y1 = row * 30
                x2 = x1 + 30
                y2 = y1 + 30
                if self.maze[row][col] == PATH:
                    color = 'white' 
                elif self.maze[row][col] == WALKED:
                    color = 'yellow'
                elif self.maze[row][col] == WALL: 
                    color = 'black'
                elif self.maze[row][col] == RETRACE:
                    color = 'red'
                elif self.maze[row][col] == TREASURE:
                    color = 'green'
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                    
                if row == self.current_row and col == self.current_col:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill='purple')
                    
    def solveMaze(self, x, y):
        if self.maze[x][y] == WALL or self.maze[x][y] == TREASURE:
            msg = 'Invalid starting position. Choose a different one.'
            print(msg)
            self.game_status_label.config(text=msg)
            return
        
        self.current_row = x
        self.current_col = y
        
        def step():
            self.canvas.delete('all')
            self.draw_maze()
            
            if self.maze[self.current_row][self.current_col] == TREASURE:
                self.print_matrix()
                self.game_status_label.config(text='Game Over - Maze Solved!')
                return 
            elif self.maze[self.current_row][self.current_col] == PATH:
                self.maze[self.current_row][self.current_col] = WALKED
            
            next_row, next_col = self.move()
            
            if (next_row, next_col) != (self.current_row, self.current_col):
                self.current_row, self.current_col = next_row, next_col
                self.root.after(175, step) 
                return
            
            self.maze[self.current_row][self.current_col] = RETRACE
            prev_move = self.moves_stack.pop()
            self.current_row, self.current_col = prev_move
            self.root.after(175, step)  
        
        if self.maze[self.current_row][self.current_col] != TREASURE:
            step()  
    
    def print_matrix(self):
        for row in self.maze:
            print(' '.join(map(str, row)))


maze = [
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

# maze1 = [
#     ['#', '#', '#', '#', '#', '#'],
#     ['#', '', '', '', '', '#'],
#     ['#', '#', '', '#', '', '#'],
#     ['#', '', '', '', '#', '#'],
#     ['#', '#', '#', '', '', 'g'],
#     ['#', '#', '#', '#', '#', '#']
# ]

# maze2 = [
#     ['#', '#', '#', '#', '#', '#'],
#     ['#', '', '', '', '', '#'],
#     ['#', '', '#', '#', '', '#'],
#     ['#', '', '', '', '#', '#'],
#     ['#', '', '#', '', '', 'g'],
#     ['#', '#', '#', '#', '#', '#']
# ]

# maze3 = [
#     ['#', '#', '#', '#', '#', '#'],
#     ['#', '', '', '', '', '#'],
#     ['#', '', '#', '', '#', '#'],
#     ['#', '', '#', '', '#', '#'],
#     ['#', '', '', '', '', 'g'],
#     ['#', '#', '#', '#', '#', '#']
# ]
# maze4 = [
#     ['#', '#', '#', '#', '#', '#'],
#     ['#', '', '', '', '', '#'],
#     ['#', '', '#', '', '', '#'],
#     ['#', '#', '#', '#', '', '#'],
#     ['#', '', '', '', '', 'g'],
#     ['#', '#', '#', '#', '#', '#']
# ]
# maze5 = [
#     ['#', '#', '#', '#', '#', '#'],
#     ['#', '', '', '', '', '#'],
#     ['#', '#', '#', '#', '', '#'],
#     ['#', '', '', '', '', '#'],
#     ['#', '#', '', '#', '', 'g'],
#     ['#', '#', '#', '#', '#', '#']
# ]
# maze6 = [
#     ['#', '#', '#', '#', '#', '#'],
#     ['#', '', '', '', '', '#'],
#     ['#', '#', '', '#', '', '#'],
#     ['#', '', '', '', '', '#'],
#     ['#', '', '#', '', '', 'g'],
#     ['#', '#', '#', '#', '#', '#']
# ]

root = tk.Tk()
root.title("Maze Solver")

game = MazeSolver(root, maze)
game.solveMaze(int(sys.argv[1]), int(sys.argv[2]))

root.mainloop()