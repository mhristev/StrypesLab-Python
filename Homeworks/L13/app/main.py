import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import json


class Movie:
    def __init__(self, id, name, year):
        self.id = id
        self.name = name
        self.year = year

    def to_dispay_in_tree(self):
        return [self.id, self.name]
    

# def save_movie_changes():
#     selected_movie = current_selected_movie.get()
#     selected_movie["name"] = name_var.get()
#     update_movie_info()

# Create the main window
root = tk.Tk()
root.title("Movie App")

# Use a dark theme-like color scheme
root.configure()
# root.option_add("*TButton*highlightBackground", "#2E2E2E")
# root.option_add("*TButton*highlightColor", "#2E2E2E")
# root.option_add("*TButton*highlightThickness", 0)

# Create the top menu

class CreateMovieWindow(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title("Create Movie")

        # Create and place widgets for movie creation form
        tk.Label(self, text="Title:").pack()
        self.title_entry = tk.Entry(self)
        self.title_entry.pack()

        tk.Label(self, text="Genre:").pack()
        self.genre_entry = tk.Entry(self)
        self.genre_entry.pack()

        tk.Label(self, text="Director:").pack()
        self.director_entry = tk.Entry(self)
        self.director_entry.pack()

        self.image_path = None
        self.image_label = tk.Label(self, text="Select Image:")
        self.image_label.pack()
        self.browse_button = tk.Button(self, text="Browse", command=self.browse_image)
        self.browse_button.pack()

        tk.Button(self, text="Create Movie", command=self.create_movie).pack()

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
        if file_path:
            self.image_path = file_path
            self.image_label.config(text="Image selected")

    def create_movie(self):
        title = self.title_entry.get()
        genre = self.genre_entry.get()
        director = self.director_entry.get()

        if title and genre and director and self.image_path:
            try:
                # Save the movie details and image
                image_filename = os.path.basename(self.image_path)
                dest_path = os.path.join("imgs", image_filename)
                os.makedirs("imgs", exist_ok=True)
                os.rename(self.image_path, dest_path)  # Move the image to "imgs" folder
                messagebox.showinfo("Success", f"Movie '{title}' created successfully!")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please fill in all fields and select an image.")

class CustomMenuFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.tree = None
        self.selected_movie_info_label = None
        
        self.create_widgets()
        self.create_list()
        self.create_movie_details_section()
 
        
    def create_widgets(self):
        
        menu_frame = tk.Frame(self)
        menu_frame.pack(fill=tk.X)
        
        # Create label
        collection_label = ttk.Label(menu_frame, text="Collection")
        collection_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Create dropdown menu
        collection_dropdown = ttk.Combobox(menu_frame, values=["Movies", "Books", "Games"], width=10)
        collection_dropdown.pack(side=tk.LEFT, padx=(0, 100), pady=10)

        add_img = tk.PhotoImage(file="remove.png").subsample(4, 4)
        button = ttk.Button(menu_frame,image=add_img,  text="Delete", compound="left", command=self.delete_selected)
        button.image = add_img
        button.pack(side=tk.RIGHT, padx=5, pady=2)
        
        # Create buttons
        add_img = tk.PhotoImage(file="plus.png").subsample(4, 4)
        button = ttk.Button(menu_frame,image=add_img,  text="Create", compound="left", command=self.create_movie_window)
        button.image = add_img
        button.pack(side=tk.RIGHT, padx=5, pady=2)
        
    def create_list(self):
        # Create the section for list of movies
        movie_list_section = tk.Frame(self)
        movie_list_section.pack(fill=tk.X)
        
        movie_list_label = ttk.Label(movie_list_section, text="Browse", font=("Helvetica", 16))
        movie_list_label.pack()
        
        
        self.tree = ttk.Treeview(movie_list_section, columns=("id", "name"), show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.heading("id", text="Id")
        self.tree.column("id", width=50, stretch=tk.NO)
        self.tree.heading("name", text="Name")
        self.tree.column("name", stretch=tk.YES)
        
        
        movies = [
            Movie(1, "Movie 1", 2020),
            Movie(2, "Movie 2", 2018),
            Movie(3, "Movie 3", 2022),
        ] 
        
        for movie in movies:
            self.tree.insert("", "end", values=(movie.to_dispay_in_tree()))

        self.tree.bind("<ButtonRelease-1>", self.on_movie_select) 
        
    def create_movie_details_section(self):
        movie_details_section = tk.Frame(self)
        movie_details_section.pack(fill=tk.X)

        movie_details_label = tk.Label(movie_details_section, text="Movie Details", font=("Helvetica", 16))
        movie_details_label.pack()

        self.selected_movie_info_label = tk.Label(movie_details_section, text="Select a movie to see details.", font=("Helvetica", 12), justify=tk.LEFT, bg="#2E2E2E", fg="white")
        self.selected_movie_info_label.pack()
        
        
    def on_movie_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item[0], "values")
            if item_values:
                id = item_values[0]
                name = item_values[1]
                self.selected_movie_info_label.config(text=f"Selected Movie:\nID:  {id}\nName: {name}")
                # self.name_var.set(selected_movie['name'])
                print(f"Selected: Id={id}, Name={name}")
        
    def create_movie_window(self):
        create_movie_window = CreateMovieWindow(self)
        
    def delete_selected(self):
        selected_index = self.tree.selection()
        if selected_index:
            confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected item?")
            if confirm:
                self.tree.delete(selected_index)
            
            
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
