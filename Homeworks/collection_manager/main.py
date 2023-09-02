from UI.root_view import RootView as CollectionManagerApp
import tkinter as tk
from DAL.database_setup import initialize_database, insert_dummy_data

if initialize_database():
    insert_dummy_data()

root = tk.Tk()
root.title("Collection Manager")
 
menu = CollectionManagerApp(root)
menu.pack()

root.mainloop()
