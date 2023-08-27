import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        buttons = [
            'CE', 'AC', '±', 'sqrt',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'mc', 'm+', 'm-', 'mr',
            '!'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: self.button_click(b)).grid(row=row, column=col, sticky="nsew")
            tk.Grid.columnconfigure(root, col, weight=1) 
            col += 1

            if col > 3:
                col = 0
                row += 1
        
        self.memory = 0
        self.operand1 = ''
        self.operand2 = ''
        self.operation = ''
        
    def button_click(self, button):
        if button in '0123456789.':
            self.handle_digit_input(button)
        elif button in '+-*/':
            self.handle_operator_input(button)
        elif button == 'sqrt':
            self.handle_square_root()
        elif button == '!':
            self.handle_factorial()
        elif button in ['CE', 'AC']:
            self.handle_clear(button)
        elif button == '±':
            self.handle_sign_change()
        elif button in ['mc', 'm+', 'm-', 'mr']:
            self.handle_memory(button)
        elif button == '=':
            self.handle_equals()
    
    def handle_equals(self):
        if self.operand1 and self.operand2 and self.operation:
            self.perform_operation()
            self.operand2 = ''
            self.operation = ''
            self.update_display_operand(1)
    
    def handle_memory(self, button):
        if button == 'mc':
            self.memory = 0
        elif button == 'm+':
            opr = self.get_active_operand()
            if opr:
                self.memory += float(opr)
        elif button == 'm-':
            opr = self.get_active_operand()
            if opr:
                self.memory -= float(opr)
        elif button == 'mr':
            if self.operand1 == '':
                self.operand1 = str(self.memory)
                self.update_display_operand(1)
            else:
                self.operand2 = str(self.memory)
                self.update_display_operand(2)        
    
    def get_active_operand(self):
        return self.operand1 if not self.operation else self.operand2
    
    def toggle_sign(self, value):
            return str(-float(value)) if value and value[0] != '-' else str(abs(float(value)))
    
    def handle_sign_change(self):
        if self.operand1 != '' or self.operand2 != '':
            if not self.operation:
                self.operand1 = self.toggle_sign(self.operand1)
                self.update_display_operand(1)
            else:
                self.operand2 = self.toggle_sign(self.operand2)
                self.update_display_operand(2)
    
    def handle_clear(self, button):
        if button == 'CE':
            if not self.operation:
                self.operand1 = ''
                self.update_display_operand(1)
            else:
                self.operand2 = ''
                self.update_display_operand(2)
        else:  # AC
            self.operand1 = ''
            self.operand2 = ''
            self.operation = ''
            self.update_display_operand(1)
        
    def handle_digit_input(self, digit):
        if not self.operation:
            self.operand1 += digit
            self.update_display_operand(1)
        else:
            self.operand2 += digit
            self.update_display_operand(2)

    def handle_square_root(self):
        try:
            value = float(self.operand1)
            result = math.sqrt(value)
            self.operand1 = str(result)
            self.update_display_operand(1)
        except ValueError:
            self.show_error("Invalid input for square root")

    def handle_operator_input(self, operator):
        if self.operand1:
            self.perform_operation()
            if self.operand1 != '' and self.operand2 != '':
                self.update_display_operand(1)

            self.operation = operator
            self.operand2 = ''  
    
    def handle_factorial(self):
        try:
            value = int(self.operand1)
            result = math.factorial(value)
            self.operand1 = str(result)
            self.update_display_operand(1)
        except ValueError:
            self.show_error("Invalid input for factorial")       
    
    def format_numeric_string(self,s):
        try:
            splited = s.split('.')
            if splited[-1] == '':
                return s
            numeric_value = float(s)
            if numeric_value.is_integer():
                formatted_string = str(int(numeric_value))
            else:
                formatted_string = str(numeric_value) 
            return formatted_string
        except ValueError:
            return s
        
    def update_display_operand(self, number):
        if number == 1:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.format_numeric_string(self.operand1))
        elif number == 2:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.format_numeric_string(self.operand2))
        
    def perform_operation(self):
        if self.operand1 and self.operand2 and self.operation:
            try:
                operand1 = float(self.operand1)
                operand2 = float(self.operand2)
                if self.operation == '+':
                    self.operand1 = str(operand1 + operand2)
                elif self.operation == '-':
                    self.operand1 = str(operand1 - operand2)
                elif self.operation == '*':
                    self.operand1 = str(operand1 * operand2)
                elif self.operation == '/':
                    self.operand1 = str(operand1 / operand2)
            except ZeroDivisionError:
                self.show_error("Division by zero")
            except ValueError:
                self.show_error("Invalid input for operation")
    
    def show_error(self, message):
        messagebox.showerror("Error", message)
        
root = tk.Tk()
Calculator(root)
root.mainloop()
