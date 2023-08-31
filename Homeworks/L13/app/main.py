from UI.root_view import RootView as FileManagerApp
import tkinter as tk
from DAL.database_setup import initialize_database, insert_dummy_data

if initialize_database():
    insert_dummy_data()

root = tk.Tk()
root.title("File Manager App")
 
menu = FileManagerApp(root)
menu.pack()

root.mainloop()
