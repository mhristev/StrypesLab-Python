import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import uuid
from datetime import datetime
import shutil

from BL.managers.author_manager import AuthorManager
from BL.managers.developer_manager import DeveloperManager
from BL.managers.director_manager import DirectorManager
from BL.managers.book_manager import BookManager
from BL.managers.game_manager import GameManager
from BL.managers.movie_manager import MovieManager
from BL.models.director import Director
from BL.models.author import Author
from BL.models.developer import Developer
from BL.models.movie import Movie
from BL.models.book import Book
from BL.models.game import Game

class CreateMediaView(tk.Toplevel):
    def __init__(self, parent, media_type, callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.callback = callback
        if media_type.lower() == "movies":
            self.movie_manager = MovieManager()
        if media_type.lower() == "books":
            self.book_manager = BookManager()
        if media_type.lower() == "games":
            self.game_manager = GameManager()
        
        self.title(f"Create {media_type.capitalize()[:-1]}")
        left_frame = tk.Frame(self)
        left_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(left_frame, text="Title:").grid(row=0, column=0, sticky="w")
        self.title_entry = tk.Entry(left_frame)
        self.title_entry.grid(row=0, column=1)

        tk.Label(left_frame, text="Genre:").grid(row=1, column=0, sticky="w")
        self.genre_entry = tk.Entry(left_frame)
        self.genre_entry.grid(row=1, column=1)

        
        if media_type.lower() == "movies":
            tk.Label(left_frame, text="Director:").grid(row=2, column=0, sticky="w")
            self.director_combobox = ttk.Combobox(left_frame)
            self.director_combobox.grid(row=2, column=1)
          
            self.director_manager = DirectorManager()
            self.director_names = self.director_manager.get_all_directors()
            self.director_combobox['values'] = self.director_names

            tk.Label(left_frame, text="Runtime (minutes):").grid(row=3, column=0, sticky="w")
            self.runtime_entry = tk.Entry(left_frame, validate="key")
            self.runtime_entry.configure(validatecommand=(self.runtime_entry.register(self.validate_int), "%P"))
            self.runtime_entry.grid(row=3, column=1)

            tk.Label(left_frame, text="Language:").grid(row=5, column=0, sticky="w")
            self.language_var = tk.StringVar()
            self.language_combobox = ttk.Combobox(left_frame, textvariable=self.language_var, state="readonly")
            self.language_combobox['values'] = ["English", "Spanish", "French", "German", "Japanese", "Bulgarian", "Other"]
            self.language_combobox.grid(row=5, column=1)
            self.language_combobox.bind("<Key>", self.prevent_custom_input)
            
            tk.Label(left_frame, text="Country:").grid(row=6, column=0, sticky="w")
            self.country_entry = ttk.Entry(left_frame)
            self.country_entry.grid(row=6, column=1)

        elif media_type.lower() == "books":
            tk.Label(left_frame, text="Author:").grid(row=2, column=0, sticky="w")
            self.author_combobox = ttk.Combobox(left_frame)
            self.author_combobox.grid(row=2, column=1)
          
            self.author_manager = AuthorManager()
            self.author_names = self.author_manager.get_all_authors()
            self.author_combobox['values'] = self.author_names
            
            tk.Label(left_frame, text="Page Count:").grid(row=3, column=0, sticky="w")
            self.page_count_entry = tk.Entry(left_frame, validate="key")
            self.page_count_entry.configure(validatecommand=(self.page_count_entry.register(self.validate_int), "%P"))
            self.page_count_entry.grid(row=3, column=1)

            tk.Label(left_frame, text="Language:").grid(row=5, column=0, sticky="w")
            self.language_var = tk.StringVar()
            self.language_combobox = ttk.Combobox(left_frame, textvariable=self.language_var, state="readonly")
            self.language_combobox['values'] = ["English", "Spanish", "French", "German", "Japanese", "Bulgarian", "Other"]
            self.language_combobox.grid(row=5, column=1)
            self.language_combobox.bind("<Key>", self.prevent_custom_input)
            
            tk.Label(left_frame, text="Country:").grid(row=6, column=0, sticky="w")
            self.country_entry = tk.Entry(left_frame)
            self.country_entry.grid(row=6, column=1)


        elif media_type.lower() == "games":
            tk.Label(left_frame, text="Developer:").grid(row=2, column=0, sticky="w")
            self.developer_combobox = ttk.Combobox(left_frame)
            self.developer_combobox.grid(row=2, column=1)
          
            self.developer_manager = DeveloperManager()
            self.developer_names = self.developer_manager.get_all_developers()
            self.developer_combobox['values'] = self.developer_names
            
            
            tk.Label(left_frame, text="Platform:").grid(row=3, column=0, sticky="w")
            self.platform_entry = tk.Entry(left_frame)
            self.platform_entry.grid(row=3, column=1)

            self.multiplayer_var = tk.BooleanVar()
            self.multiplayer_check = tk.Checkbutton(left_frame, text="Multiplayer Mode:", variable=self.multiplayer_var)
            self.multiplayer_check.grid(row=4, column=0, columnspan=2)

        right_frame = tk.Frame(self)
        right_frame.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(right_frame, text="Release Date (yyyy-mm-dd):").grid(row=0, column=0, sticky="w")
        self.release_entry = ttk.Entry(right_frame)
        self.release_entry.grid(row=0, column=1)

        tk.Label(right_frame, text="Synopsis:").grid(row=1, column=0, sticky="w")
        self.synopsis_text = tk.Text(right_frame, height=5, width=30)
        self.synopsis_text.grid(row=1, column=1)

        self.image_path = None
        self.image_label = tk.Label(right_frame, text="Select Image:")
        self.image_label.grid(row=2, column=0, sticky="w")
        self.browse_button = tk.Button(right_frame, text="Browse", command=self.browse_image)
        self.browse_button.grid(row=2, column=1)

        tk.Button(right_frame, text=f"Create {media_type.capitalize()}", command=self.create_media).grid(row=3, column=0, columnspan=2)
    
    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
        if file_path:
            self.image_path = file_path
            self.image_label.config(text="Image selected")
            
    def save_image(self):
        try:
            if self.image_path == "":
                messagebox.showerror("Error", "Select image file.")
                return
            image_filename = os.path.basename(self.image_path)
            image_name, image_extension = os.path.splitext(image_filename)
            uid = str(uuid.uuid4())
            new_image_filename = f"{uid}{image_extension}"
            
            dest_path = os.path.join("imgs", new_image_filename)
            os.makedirs("imgs", exist_ok=True)
            shutil.copy2(self.image_path, dest_path) 
            

            return dest_path
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def prevent_custom_input(self, event):
        self.language_var.set(self.language_var.get())
    
    def is_valid_date_format(self, date_string):
        try:
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    def create_media(self):
        title = self.title_entry.get()
        genre = self.genre_entry.get()
        release_date = self.release_entry.get()
        synopsis = self.synopsis_text.get("1.0", tk.END).strip()
        
        
        if self.image_path == None:
            messagebox.showerror("Error", "Please choose an image")
            return
        
        if title == "" or genre == "" or release_date == "" or synopsis == "":
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
        
        if self.is_valid_date_format(release_date) is False:
            messagebox.showerror("Error", "Invalid date format")
            return
        
        if hasattr(self, 'director_combobox'):
            director = self.director_combobox.get()
            runtime_in_minutes = self.runtime_entry.get()
            language = self.language_var.get()
            country = self.country_entry.get()
            
            director_id = None
            new_dir_name = ""
            
            if director == "" or language == "" or country == "":
                messagebox.showerror("Error", "Please fill in all required fields.")
                return
            
            if self.director_combobox.current() == -1:
                director_id= None
                new_dir_name = director.strip()
            else:
                director_id = director.split(' ')[0]
            
            
            dest_path = self.save_image()
            movie = Movie(id=0, title=title, 
                          genre=genre, release_date=release_date, \
                          director=Director(director_id, new_dir_name), runtime_in_minutes=runtime_in_minutes, \
                          language=language, country=country, synopsis=synopsis, image_path=dest_path \
                          )

            movie_id = self.movie_manager.create_movie(movie)
            self.callback(movie_id)
            messagebox.showinfo("Success", f"Movie created successfully!")
            self.destroy()
        elif hasattr(self, 'author_combobox'):
            author = self.author_combobox.get()
            page_count = int(self.page_count_entry.get())
            language = self.language_var.get()
                        
            if author == "" or language == "":
                messagebox.showerror("Error", "Please fill in all required fields.")
                return
            
            author_id = None
            new_auth_name = ""
            dest_path = self.save_image()
            if self.author_combobox.current() == -1:
                author_id = None
                new_auth_name = author.strip()
            else:
                author_id = author.split(' ')[0]
            
            
            book = Book (id=0, title=title, genre=genre, release_date=release_date, synopsis=synopsis, \
                        author=Author(author_id, new_auth_name), page_count=page_count, language=language, image_path=dest_path)

            book_id = self.book_manager.create_book(book)
            self.callback(book_id)
            messagebox.showinfo("Success", f"Book created successfully!")
            self.destroy()
            
        elif hasattr(self, 'developer_combobox'):
            developer = self.developer_combobox.get()
            platform = self.platform_entry.get()
            multiplayer_mode = self.multiplayer_var.get()
            dest_path = self.save_image()
            if developer == "" or platform == "":
                messagebox.showerror("Error", "Please fill in all required fields.")
                return
            
            dev_id = None
            new_dev_name = ""
            if self.developer_combobox.current() == -1:
                dev_id = None
                new_dev_name = developer.strip()
            else:
                dev_id = developer.split(' ')[0]
             
            game = Game(id=0, title=title, genre=genre, release_date=release_date, synopsis=synopsis, \
                developer=Developer(id=dev_id, name=new_dev_name), platform=platform, image_path=dest_path, multiplayer_mode=multiplayer_mode)
            
            game_id = self.game_manager.create_game(game)
            self.callback(game_id)
            messagebox.showinfo("Success", f"Game created successfully!")
            self.destroy()

    def validate_int(self, value):
        try:
            if value == "" or int(value) >= 0:
                return True
            else:
                return False
        except ValueError:
            return False