import tkinter as tk
from tkinter import ttk

def set_theme(theme):
    ttk.Style().theme_use(theme)

root = tk.Tk()
root.title("Ttk Menu Buttons")

# Create the message label
msg = ttk.Label(root, font="TkDefaultFont", wraplength="4i", justify="left",
                text="Ttk is the new Tk themed widget set, and one widget that is available in themed form is the menubutton. Below are some themed menu buttons that allow you to pick the current theme in use. Notice how picking a theme changes the way that the menu buttons themselves look, and that the central menu button is styled differently (in a way that is normally suitable for toolbars). However, there are no themed menus; the standard Tk menus were judged to have a sufficiently good look-and-feel on all platforms, especially as they are implemented as native controls in many places.")
msg.pack(side="top", fill="x")
ttk.Separator(root).pack(side="top", fill="x")

# Create menu buttons
menu_styles = [
    ("Select a theme", "above"),
    ("Select a theme", "left"),
    ("Select a theme", "right"),
    ("Select a theme", "flush", "TMenubutton.Toolbutton"),
    ("Select a theme", "below")
]

for text, direction, *styles in menu_styles:
    button = ttk.Menubutton(root, text=text, direction=direction)
    button_menu = tk.Menu(button, tearoff=0)
    button["menu"] = button_menu
    for theme in ttk.Style().theme_names():
        button_menu.add_command(label=theme, command=lambda t=theme: set_theme(t))
    if styles:
        button_style = ttk.Style()
        button_style.configure(styles[0], **(styles[1] if styles[1:] else {}))
    button.pack(side="top", padx=3, pady=2)


# Create a frame to contain the buttons
frame = ttk.Frame(root)
frame.pack(fill="x")

# Create a frame to expand vertically
expand_frame = ttk.Frame(root)
expand_frame.pack(fill="both", expand=True)

# Create see/dismiss buttons
ttk.Separator(root).pack(side="bottom", fill="x")
ttk.Button(root, text="See Code").pack(side="bottom", fill="x")
ttk.Button(root, text="Dismiss").pack(side="bottom", fill="x")

root.mainloop()
