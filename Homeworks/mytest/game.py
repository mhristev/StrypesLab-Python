
import tkinter as tk
from collections import deque
from enum import Enum
from time import sleep

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
    def __init__(self, root, pattern):
        self.pattern = pattern
        self.moves_stack = deque()
        self.current_row = 0
        self.current_col = 0
        self.root = root
        
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.draw_maze()

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
    
    
    def draw_maze(self):
        for row in range(len(self.pattern)):
            for col in range(len(self.pattern[0])):
                x1 = col * 20
                y1 = row * 20
                x2 = x1 + 20
                y2 = y1 + 20
                
                
                if self.pattern[row][col] == PATH:
                    color = "white" 
                elif self.pattern[row][col] == WALKED:
                    color = "yellow"
                elif self.pattern[row][col] == WALL: 
                    color = "black"
                elif self.pattern[row][col] == BACK_WALKED:
                    color = "red"
                elif self.pattern[row][col] == TRESSURE:
                    color = "green"
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                    
                if row == self.current_row and col == self.current_col:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="red")
                    
    def solveMaze(self, x, y):
        self.current_row = x
        self.current_col = y
        while True:
            self.canvas.delete("all")  # Clear the canvas
            self.draw_maze()
            # self.root.after(4000, self.draw_maze)
            
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


# class MazeGame:
#     def __init__(self, root, maze):
#         self.root = root
#         self.maze = maze
#         self.current_row, self.current_col = self.find_start_position()
        
#         self.canvas = tk.Canvas(root, width=400, height=400)
#         self.canvas.pack()
        
#         self.draw_maze()
        
#     def draw_maze(self):
#         for row in range(len(self.maze)):
#             for col in range(len(self.maze[0])):
#                 x1 = col * 20
#                 y1 = row * 20
#                 x2 = x1 + 20
#                 y2 = y1 + 20
                
                
#                 if self.maze[row][col] == 0:
#                     color = "white" 
#                 elif self.maze[row][col] == 'S':
#                     color = "yellow"
#                 else: 
#                     color = "black"
#                 self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                
#                 if self.maze[row][col] == 2:
#                     self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="green")
                    
#                 if row == self.current_row and col == self.current_col:
#                     self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="red")
                    
#     def find_start_position(self):
#         for row in range(len(self.maze)):
#             for col in range(len(self.maze[0])):
#                 if self.maze[row][col] == 0:
#                     return row, col
    
#     def is_valid_move(self, row, col):
#         return 0 <= row < len(self.maze) and 0 <= col < len(self.maze[0]) and self.maze[row][col] != 1
    
#     def move(self, direction):
#         new_row, new_col = self.current_row + direction[0], self.current_col + direction[1]
        
#         if self.is_valid_move(new_row, new_col):
#             self.current_row, self.current_col = new_row, new_col
#             self.maze[self.current_row][self.current_col] = 'S'
#             self.canvas.delete("all")  # Clear the canvas
#             self.draw_maze()
            

def main():
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
    
    root = tk.Tk()
    root.title("Maze Game")
    
    game = MazeSolver(root, maze)
    game.solveMaze(1, 1)
    
    # game = MazeGame(root, maze)
    
    # def on_right():
    #     game.move((0, 1))
        
    # def on_left():
    #     game.move((0, -1))
        
    # def on_up():
    #     game.move((-1, 0))
        
    # def on_down():
    #     game.move((1, 0))
        
    # right_button = tk.Button(root, text="Right", command=on_right)
    # right_button.pack(side="right")
    
    # left_button = tk.Button(root, text="Left", command=on_left)
    # left_button.pack(side="left")
    
    # up_button = tk.Button(root, text="Up", command=on_up)
    # up_button.pack(side="top")
    
    # down_button = tk.Button(root, text="Down", command=on_down)
    # down_button.pack(side="bottom")
    
    root.mainloop()

if __name__ == "__main__":
    main()
