import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os


root = tk.Tk()
root.title("Movie App")

            
menu = CustomMenuFrame(root, padding=10)
menu.pack()

# Create the section for movie details and editing


# name_var = tk.StringVar()
# name_label = tk.Label(movie_details_section, text="Name:", bg="#2E2E2E", fg="white")
# name_label.pack()
# name_entry = tk.Entry(movie_details_section, textvariable=name_var)
# name_entry.pack()

# save_name_button = tk.Button(movie_details_section, text="Save Name", command=save_movie_changes, bg="#FF9900", fg="black")
# save_name_button.pack()

root.mainloop()
