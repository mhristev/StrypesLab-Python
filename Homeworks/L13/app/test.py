from UI.root_view import RootView
import tkinter as tk

root = tk.Tk()
root.title("Movie App")
 
menu = RootView(root)
menu.pack()

root.mainloop()
