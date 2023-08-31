from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

from BL.managers.author_manager import AuthorManager
from BL.managers.developer_manager import DeveloperManager
from BL.managers.director_manager import DirectorManager
from BL.models.author import Author
from BL.models.developer import Developer
from BL.models.director import Director
from .create_media_view import CreateMediaView
from BL.managers.book_manager import BookManager
from BL.managers.game_manager import GameManager
from BL.managers.movie_manager import MovieManager
from BL.models.book import Book
from BL.models.game import Game
from BL.models.movie import Movie
from PIL import Image, ImageTk

class RootView(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.tree = None
        self.collection_dropdown = None
        
        self.movie_manager = MovieManager()
        self.game_manager = GameManager()
        self.book_manager = BookManager()
        
        self.create_widgets()
        self.create_list()
        self.details_section = tk.Frame(self)
        self.details_section.pack(fill=tk.X)
        self.create_details_section(Movie())
        
    def create_widgets(self):
        menu_frame = tk.Frame(self)
        menu_frame.pack(fill=tk.X)

        collection_label = ttk.Label(menu_frame, text="Collection")
        collection_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.collection_dropdown = ttk.Combobox(menu_frame, values=["Movies", "Books", "Games"], width=10)
        self.collection_dropdown.pack(side=tk.LEFT, padx=(0, 100), pady=10)
        self.collection_dropdown.set("Movies")
        self.collection_dropdown.bind("<<ComboboxSelected>>", self.on_collection_selected)
        
        image_dir = 'imgs'
        image_path = os.path.join(image_dir, "remove.png")
        
        add_img = tk.PhotoImage(file=image_path).subsample(4, 4)
        button = ttk.Button(menu_frame,image=add_img,  text="Delete", compound="left", command=self.delete_selected)
        button.image = add_img
        button.pack(side=tk.RIGHT, padx=5, pady=2)
        
        image_path = os.path.join(image_dir, "plus.png")

        add_img = tk.PhotoImage(file=image_path).subsample(4, 4)
        button = ttk.Button(menu_frame,image=add_img,  text="Create", compound="left", command=self.open_create_media_window)
        button.image = add_img
        button.pack(side=tk.RIGHT, padx=5, pady=2)
        
    def create_list(self):
        movie_list_section = tk.Frame(self)
        movie_list_section.pack(fill=tk.X)
        
        frame = ttk.Frame(movie_list_section)
        frame.pack(padx=10, pady=10, fill="x")

        movie_list_label = ttk.Label(frame, text="Browse", font=("Helvetica", 20))
        movie_list_label.grid(row=0, column=0, padx=5)
        
        self.entry_search = ttk.Entry(frame)
        self.entry_search.grid(row=0, column=1, padx=(400, 5), sticky="e")

        self.search_by_var = tk.StringVar(value="Name")
        
        radio_name = ttk.Radiobutton(frame, text="Name", variable=self.search_by_var, value="Name")
        radio_genre = ttk.Radiobutton(frame, text="Genre", variable=self.search_by_var, value="Genre")
        radio_name.grid(row=0, column=9, padx=5)
        radio_genre.grid(row=0, column=10, padx=5)

        search_button = ttk.Button(frame, text="Search", command=self.search)
        search_button.grid(row=0, column=11, padx=5)
        
        search_button = ttk.Button(frame, text="Refresh", command=self.refresh_tree)
        search_button.grid(row=0, column=12, padx=5)

        self.tree = ttk.Treeview(movie_list_section, columns=("id", "title", "genre"), show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.heading("id", text="Id")
        self.tree.column("id", width=50, stretch=tk.NO)
        self.tree.heading("title", text="Title")
        self.tree.column("title", stretch=tk.YES)
        self.tree.heading("genre", text="Genre")
        self.tree.column("genre", stretch=tk.YES)
        
        movies = self.movie_manager.get_all_movies()
        
        for movie in movies:
            self.tree.insert("", "end", values=([movie.id, movie.title, movie.genre]))
            
        self.tree.bind("<<TreeviewSelect>>", self.on_media_select) 
    
    def refresh_tree(self):
        collection = self.collection_dropdown.get()
        self.clear_tree()
        
        filtered_items = None
        
        if collection == "Movies":
            filtered_items = self.movie_manager.get_all_movies()
        elif collection == "Books":
            filtered_items = self.book_manager.get_all_books()
        elif collection == "Games":
            filtered_items = self.game_manager.get_all_games()
        
        self.insert_filtered_items(filtered_items)
        
    def search(self):
        search_text = self.entry_search.get()
        search_by = self.search_by_var.get()
        collection = self.collection_dropdown.get()

        self.clear_tree()

        filtered_items = None

        if collection == "Movies":
            filtered_items = self.filter_movies(search_by, search_text)
        elif collection == "Books":
            filtered_items = self.filter_books(search_by, search_text)
        elif collection == "Games":
            filtered_items = self.filter_games(search_by, search_text)

        self.insert_filtered_items(filtered_items)

    def clear_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def insert_filtered_items(self, items):
        if items:
            for item in items:
                self.tree.insert("", "end", values=(item.id, item.title, item.genre))

    def filter_movies(self, search_by, search_text):
        if search_by == "Name":
            return self.movie_manager.get_movies_by_title(search_text)
        elif search_by == "Genre":
            return self.movie_manager.get_movies_by_genre(search_text)
        return []

    def filter_books(self, search_by, search_text):
        if search_by == "Name":
            return self.book_manager.get_books_by_title(search_text)
        elif search_by == "Genre":
            return self.book_manager.get_books_by_genre(search_text)
        return []

    def filter_games(self, search_by, search_text):
        if search_by == "Name":
            return self.game_manager.get_games_by_title(search_text)
        elif search_by == "Genre":
            return self.game_manager.get_games_by_genre(search_text)
        return []
    
    def resize_image(self, image_path, width, height):
        original_image = Image.open(image_path)
        original_width, original_height = original_image.size
        aspect_ratio = original_width / original_height

        new_width = width
        new_height = int(new_width / aspect_ratio)

        if new_height > height:
            new_height = height
            new_width = int(new_height * aspect_ratio)

        resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)
    
    def create_details_section(self, media):
        details_label = tk.Label(self.details_section, text="Media Details", font=("Helvetica", 20))
        details_label.pack(pady=10)

        labels_frame = tk.Frame(self.details_section)
        labels_frame.pack()
        if media.image_path == "":
            image_dir = 'imgs'
            media.image_path = os.path.join(image_dir, "cat.png")
        
        resized_image = self.resize_image(media.image_path, 150, 150)
        
        button = ttk.Label(labels_frame, image=resized_image)
        button.grid(row=0, column=0, rowspan=10, padx=30, pady=10, sticky="w")
        button.image = resized_image
        
        common_attrs = [
            ("Title:", media.title),
            ("Release Date (yyyy-mm-dd):", media.release_date),
            ("Genre:", media.genre),
            ("Synopsis:", media.synopsis)
        ]

        for i, (label_text, default_value) in enumerate(common_attrs):
            label = tk.Label(labels_frame, text=label_text, width=20, anchor="w")
            label.grid(row=i, column=1, sticky="w")

            entry = tk.Entry(labels_frame)
            entry.insert(0, default_value)  
            entry.grid(row=i, column=2, sticky="w")
                  
        if isinstance(media, Movie):
            label = tk.Label(labels_frame, text="Director:", width=20, anchor="w")
            label.grid(row=0, column=3, sticky="w")
            director_combobox = ttk.Combobox(labels_frame)
            director_combobox.grid(row=0, column=4)
          
            dir_manager = DirectorManager()
            dir_names = dir_manager.get_all_directors()
            director_combobox['values'] = dir_names
            
            for index, (id_, name) in enumerate(dir_names):
                if id_ == media.director.id and name == media.director.name:
                    director_combobox.current(index)
                    break
                
            tk.Label(labels_frame, text="Runtime(minutes):").grid(row=1, column=3, sticky="w")
            runtime_entry = tk.Entry(labels_frame, validate="key")
            runtime_entry.configure( validatecommand=(runtime_entry.register(self.validate_int), "%P"))
            runtime_entry.grid(row=1, column=4)
            runtime_entry.insert(0, media.runtime_in_minutes)

            tk.Label(labels_frame, text="Language:").grid(row=2, column=3, sticky="w")
            language_combobox = ttk.Combobox(labels_frame, state="readonly")
            language_combobox['values'] = ["English", "Spanish", "French", "German", "Japanese", "Bulgarian", "Other"]
            language_combobox.grid(row=2, column=4)
            language_combobox.set(media.language)
            
            label = tk.Label(labels_frame, text="Country:", width=20, anchor="w")
            label.grid(row=3, column=3, sticky="w")

            entry = tk.Entry(labels_frame)
            entry.insert(0, media.country)
            entry.grid(row=3, column=4, sticky="w")
            
        elif isinstance(media, Game):
            game_attrs = [
                ("Platform:", media.platform),
                # ("Multiplayer Mode (Yes/No):", "Yes" if media.multiplayer_mode else "No"),
            ]
            
            label = tk.Label(labels_frame, text="Developer:", width=20, anchor="w")
            label.grid(row=0, column=3, sticky="w")
            developer_combobox = ttk.Combobox(labels_frame)
            developer_combobox.grid(row=0, column=4)
          
            dev_manager = DeveloperManager()
            dev_names = dev_manager.get_all_developers()
            developer_combobox['values'] = dev_names
            
            for index, (id_, name) in enumerate(dev_names):
                if id_ == media.developer.id and name == media.developer.name:
                    developer_combobox.current(index)
                    break
                
            self.multiplayer_var = tk.IntVar()
            
            multiplayer_check = tk.Checkbutton(labels_frame, text="Multiplayer Mode", variable=self.multiplayer_var, onvalue=1, offvalue=0)
            multiplayer_check.grid(row=1, column=4)
            
            if media.multiplayer_mode:
                self.multiplayer_var.set(1)
            
            for i, (label_text, default_value) in enumerate(game_attrs):
                label = tk.Label(labels_frame, text=label_text, width=20, anchor="w")
                label.grid(row=i+2, column=3, sticky="w")

                entry = tk.Entry(labels_frame)
                entry.insert(0, default_value)
                entry.grid(row=i+2, column=4, sticky="w")
        
        elif isinstance(media, Book):
            label = tk.Label(labels_frame, text="Author:", width=20, anchor="w")
            label.grid(row=0, column=3, sticky="w")
            author_combobox = ttk.Combobox(labels_frame)
            author_combobox.grid(row=0, column=4)
          
            author_manager = AuthorManager()
            author_names = author_manager.get_all_authors()
            author_combobox['values'] = author_names
            
            for index, (id_, name) in enumerate(author_names):
                if id_ == media.author.id and name == media.author.name:
                    author_combobox.current(index)
                    break
            
            tk.Label(labels_frame, text="Page Count:").grid(row=1, column=3, sticky="w")
            page_count_entry = tk.Entry(labels_frame, validate="key")
            page_count_entry.configure( validatecommand=(page_count_entry.register(self.validate_int), "%P"))
            page_count_entry.grid(row=1, column=4)
            page_count_entry.insert(0, media.page_count)

            tk.Label(labels_frame, text="Language:").grid(row=2, column=3, sticky="w")
            language_combobox = ttk.Combobox(labels_frame ,state="readonly")
            language_combobox['values'] = ["English", "Spanish", "French", "German", "Japanese", "Bulgarian", "Other"]
            language_combobox.grid(row=2, column=4)
            language_combobox.set(media.language)
                
        button = ttk.Button(labels_frame, text="Save", compound="left", command=self.update_media)
        button.grid(row=10, column=4)

    def validate_int(self, value):
        try:
            if value == "" or int(value) >= 0:
                return True
            else:
                return False
        except ValueError:
            return False
        
    def update_media(self):
        selected_id = None
        selected_index = self.tree.selection()
        if selected_index:
            item_values = self.tree.item(selected_index[0], "values")
            if item_values:
                selected_id = item_values[0]

        if not selected_id:
            return

        values = [selected_id]
        media_type = self.detect_media_type()
        
        if not media_type:
            return

        for child in self.details_section.winfo_children():
            if isinstance(child, tk.Frame):
                for c in child.winfo_children():
                    if isinstance(c, tk.Checkbutton):
                        values.append(self.multiplayer_var.get())
                    elif isinstance(c, tk.Label):
                        txt = c.cget("text")
                        if txt == "Author:":
                            media_type = "book"
                        elif txt == "Director:":
                            media_type = "movie"
                        elif txt == "Developer:":
                            media_type = "game"
                    elif isinstance(c, ttk.Combobox):
                        selected_value = c.get()
                        if selected_value in ["English", "Spanish", "French", "German", "Japanese", "Bulgarian", "Other"]:
                            values.append(selected_value)
                            continue
                            
                        name = ""
                        id = None
                        if c.current() == -1:
                            name = selected_value.strip()
                        else:
                            id = selected_value.split(' ')[0]
                        if name == '' and id is None:
                            messagebox.showerror("Error", "Empty fields!")
                            return
                        values.append(id)
                        values.append(name)
                    elif isinstance(c, tk.Entry):
                        value = c.get()
                        if value == '':
                            messagebox.showerror("Error", "Empty fields! in entry")
                            return
                        values.append(value)

        if self.is_valid_date_format(values[2]) is False:
            messagebox.showerror("Error", "Invalid date format")
            return

        if media_type == "book":
            media_id, title, release_date, genre, synopsis, author_id, author_name, page_count, language = values
            book = Book(id=media_id, title=title, release_date=release_date, genre=genre, page_count=page_count, synopsis=synopsis, language=language, image_path="", author=Author(author_id, author_name))
            self.book_manager.update_book(book)
        elif media_type == "game":
            media_id, title, release_date, genre, synopsis, developer_id, developer_name, multiplayer_mode, platform = values
            game = Game(id=media_id, title=title, release_date=release_date, genre=genre, synopsis=synopsis, image_path="", developer=Developer(developer_id, developer_name), platform=platform, multiplayer_mode=multiplayer_mode)
            self.game_manager.update_game(game)
        elif media_type == "movie":
            media_id, title, release_date, genre, synopsis, director_id, director_name, runtime, language, country = values
            movie = Movie(id=media_id, title=title, release_date=release_date, genre=genre, synopsis=synopsis, director=Director(director_id, director_name), runtime_in_minutes=runtime, language=language, country=country, image_path="")
            self.movie_manager.update_movie(movie)

        self.update_row(media_id=values[0], new_name=values[1], new_genre=values[3])
        messagebox.showinfo("Success", f"Media updated successfully!")
        
    def update_row(self, media_id, new_name, new_genre):
        item_id = None
        for item in self.tree.get_children():
            if self.tree.item(item, "values")[0] == media_id:
                item_id = item
                break
        
        if item_id:
            self.tree.item(item_id, values=(media_id, new_name, new_genre)) 
       
    def detect_media_type(self):
        children = self.details_section.winfo_children()
        for child in children:
            if isinstance(child, tk.Frame):
                for c in child.winfo_children():
                    if isinstance(c, tk.Label):
                        txt = c.cget("text")
                        if txt == "Author:":
                            return "book"
                        elif txt == "Director:":
                            return "movie"
                        elif txt == "Developer:":
                            return "game"
        return None
    
    def is_valid_date_format(self, date_string):
        try:
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def on_media_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item[0], "values")
            if item_values:
                id = item_values[0]
                media = None
                if self.collection_dropdown.get() == "Movies":
                    media = self.movie_manager.get_movie_by_id(id)
                elif self.collection_dropdown.get() == "Books":
                    media = self.book_manager.get_book_by_id(id)
                elif self.collection_dropdown.get() == "Games":
                    media = self.game_manager.get_game_by_id(id)
                
                for child in self.details_section.winfo_children():
                    child.destroy()
                
                self.create_details_section(media)

        
    def open_create_media_window(self):
        def callback(text):
                if self.collection_dropdown.get() == "Movies":
                    media = self.movie_manager.get_movie_by_id(text)
                    self.tree.insert("", "end", values=([media.id, media.title, media.genre]))
                elif self.collection_dropdown.get() == "Books":
                    media = self.book_manager.get_book_by_id(text)
                    self.tree.insert("", "end", values=([media.id, media.title, media.genre]))
                elif self.collection_dropdown.get() == "Games":
                    media = self.game_manager.get_game_by_id(text)
                    self.tree.insert("", "end", values=([media.id, media.title, media.genre]))
            
        create_movie_window = CreateMediaView(self, self.collection_dropdown.get(), callback=callback)
        create_movie_window.protocol("WM_DELETE_WINDOW", create_movie_window.destroy)
        create_movie_window.grab_set()
        create_movie_window.focus_force()
        
    def delete_selected(self):
        selected_index = self.tree.selection()
        if selected_index:
                item_values = self.tree.item(selected_index[0], "values")
                if item_values:
                    id = item_values[0]
                    confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected item?")
                    if confirm:
                        self.tree.delete(selected_index)
                        self.movie_manager.delete_movie(id)
                        first_item_id = self.tree.get_children()[0]
                        self.tree.selection_set(first_item_id)    
                
    def on_collection_selected(self, event):
        selected_collection = self.collection_dropdown.get()
        collection = None
        self.tree.delete(*self.tree.get_children())
        if selected_collection == "Movies":
            collection = self.movie_manager.get_all_movies()
        elif selected_collection == "Games":
            collection = self.game_manager.get_all_games()
        elif selected_collection == "Books":
            collection = self.book_manager.get_all_books()
        
        for c in collection:
                self.tree.insert("", "end", values=([c.id, c.title, c.genre]))