import random
import tkinter as tk

class HangmanGame:
    def __init__(self, words_file):
        self.lives = 11
        self.guesses = []
        self.words_file = words_file
        self.word_to_guess = self.generate_word().strip().upper()
        
    def generate_word(self):
        with open(self.words_file, 'r') as file:
            lines = file.readlines()
        
        return random.choice(lines)
        
    def make_guess(self, letter):
        self.guesses.append(letter)
        if letter not in self.word_to_guess:
            self.lives -= 1
    
    def get_game_status_message(self):
        if self.lives == 0:
            return True, f"Game Over!\nBetter luck next time! The word was {self.word_to_guess}"
    
        for letter in self.word_to_guess:
            if letter not in self.guesses:
                return False, ""
    
        return True, "Victory!\nCongratulations, you guessed the word!"

    def get_current_state(self):
        state = ""
        for char in self.word_to_guess:
            if char in self.guesses:
                state += char
            else:
                state += "_ "
        return state
    
    
class HangmanUI:
    def __init__(self, root):
        self.game = HangmanGame("words.txt")
        self.root = root
        self.root.title("Hangman Game")
        self.root.resizable(width=False, height=False)
        
        self.lives_label = tk.Label(root, text=f"Lives: {self.game.lives}")
        self.lives_label.pack()
        
        background_image = tk.PhotoImage(file="hang0.png")
        self.image_label = tk.Label(root, image=background_image)
        self.image_label.pack()
        
        self.status_label = tk.Label(root, text="Guess the word:")
        self.status_label.pack(pady=10) 
        
        self.word_label = tk.Label(root, text=self.game.get_current_state())
        self.word_label.pack(pady=20)
        
        self.alphabet_frame = tk.Frame(root)
        self.alphabet_frame.pack()
        
        cols = 10
        self.alphabet_buttons = []
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            button = tk.Button(self.alphabet_frame, text=letter, command=lambda l=letter: self.letter_clicked(l))
            button.grid(row=i // cols, column=i % cols, padx=2, pady=2)
            self.alphabet_buttons.append(button)
            
        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack(side="right")
        
    def letter_clicked(self, letter):
        for button in self.alphabet_buttons:
            if button["text"] == letter:
                button["state"] = tk.DISABLED
                self.game.make_guess(letter)
                self.word_label.config(text=self.game.get_current_state())
                self.lives_label.config(text=f"Lives: {self.game.lives}")   
                self.update_image() 
                status, msg = self.game.get_game_status_message()
                if status:
                    self.status_label.config(text=msg)
                    for b in self.alphabet_buttons:
                        b["state"] = tk.DISABLED
                break
    
    def restart_game(self):
        self.game = HangmanGame("words.txt")
        for b in self.alphabet_buttons:
            b["state"] = tk.ACTIVE
        self.status_label.config(text="")
        self.word_label.config(text=self.game.get_current_state())
        self.lives_label.config(text=f"Lives: {self.game.lives}")
        self.update_image()
            
    def update_image(self):
        new_image = tk.PhotoImage(file=f"hang{11 - self.game.lives}.png")
        self.image_label.config(image=new_image)
        self.image_label.image = new_image
        
        
root = tk.Tk()
hangman_ui = HangmanUI(root)
root.mainloop()
