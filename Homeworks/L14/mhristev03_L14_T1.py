import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk, ImageFilter, ImageOps
import os

aspect_ratios = {
    "1:1": 1.0,
    "3:2": 3 / 2,
    "4:3": 4 / 3,
    "5:4": 5 / 4,
    "16:9": 16 / 9,
    "9:16": 9 / 16,
}

class ImageViewer:
    def __init__(self, root):
        self.history = [] 
        self.rotation_angle = 0
        self.current_image = None
        self.displayed_image_tk = None
        
        self.root = root
        self.root.title("Image Viewer")
        
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        self.info_name_label = tk.Label(frame, text="")
        self.info_name_label.pack()
        
        self.info_label = tk.Label(frame, text="")
        self.info_label.pack()
        
        self.label = tk.Label(frame, text="Select an image...")
        self.label.pack(fill=tk.BOTH, expand=True)
        
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        self.load_button = tk.Button(frame, text="Load Image", command=self.load_image)
        self.load_button.grid(row=0, column=0)
        
        self.undo_button = tk.Button(frame, text="Undo", command=self.undo)
        self.undo_button.grid(row=0, column=1)
        
        self.save_button = tk.Button(frame, text="Save", command=self.save_image)
        self.save_button.grid(row=0, column=2, sticky="e")
        
        self.label_filters = tk.Label(self.root, text="Filters", font=("", 14, "bold"))
        self.label_filters.pack(fill=tk.BOTH, expand=True)
        
        frame = tk.Frame(root)
        frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        self.filter_button = tk.Button(frame, text="Grayscale", command=lambda:self.apply_filter("grayscale"))
        self.filter_button.grid(row=0, column=0)
        
        self.filter_button = tk.Button(frame, text="Blur", command=lambda:self.apply_filter("blur"))
        self.filter_button.grid(row=0, column=1)
        
        self.filter_button = tk.Button(frame, text="Contour", command=lambda:self.apply_filter("contour"))
        self.filter_button.grid(row=0, column=2)
        
        self.filter_button = tk.Button(frame, text="Detail", command=lambda:self.apply_filter("detail"))
        self.filter_button.grid(row=1, column=0)
        
        self.filter_button = tk.Button(frame, text="Sharpen", command=lambda:self.apply_filter("sharpen"))
        self.filter_button.grid(row=1, column=1)
        
        self.filter_button = tk.Button(frame, text="Smooth", command=lambda:self.apply_filter("smooth"))
        self.filter_button.grid(row=1, column=2)
        
        self.label_transform = tk.Label(self.root, text="Transformations", font=("", 14, "bold"))
        self.label_transform.pack(fill=tk.BOTH, expand=True)
        
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        self.rotate_button = tk.Button(frame, text="Rotate", command=self.rotate_image)
        self.rotate_button.grid(row=0, column=0)
        
        self.horizontal_flip_button = tk.Button(frame, text="Horizontal Flip", command=self.flip_horizontal)
        self.horizontal_flip_button.grid(row=0, column=1)
        
        self.vertical_flip_button = tk.Button(frame, text="Vertical Flip", command=self.flip_vertical)
        self.vertical_flip_button.grid(row=0, column=2)
        
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        self.aspect_ratio_label = tk.Label(frame, text="Aspect Ratio:")
        self.aspect_ratio_label.grid(row=0, column=0, padx=5)

        self.aspect_ratio_combobox = ttk.Combobox(frame, values=list(aspect_ratios.keys()))
        self.aspect_ratio_combobox.grid(row=0, column=1, padx=5)
        self.aspect_ratio_combobox.set("1:1")
        
        self.filter_button = tk.Button(frame, text="Resize", command=self.resize_image)
        self.filter_button.grid(row=0, column=2, padx=5)
        
    
    def save_image(self):
        if self.current_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
            if file_path:
                self.current_image.save(file_path)
                messagebox.showinfo("Success", f"Image saved successfully!")
    
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")])
        if file_path:
            self.display_image(file_path)
    
    def undo(self):
        if self.history:
            self.history.pop()
            if self.history:
                self.current_image = self.history[-1].copy()
            else:
                self.current_image = self.current_image.copy()
            self.update_info_label()
            self.display_image_state()
            
    def save_image_to_history(self):
        self.history.append(self.current_image.copy())
        
    def display_image_state(self):
        self.displayed_image_tk = ImageTk.PhotoImage(self.current_image)
        self.label.config(image=self.displayed_image_tk)
        
    def display_image(self, img_path):
        self.current_image = Image.open(img_path)
        self.current_image.thumbnail((600, 600))
        self.displayed_image_tk = ImageTk.PhotoImage(self.current_image)
        self.label.config(image=self.displayed_image_tk)
        
        image_filename = os.path.basename(img_path)
        image_name, image_extension = os.path.splitext(image_filename)
        
        self.info_name_label.config(text=f"Name: {image_name}\nType: {self.current_image.format}")
        self.update_info_label()
        self.history.append(self.current_image.copy())
    
    def update_info_label(self):
        image_size = f"Size: {self.current_image.width} x {self.current_image.height}"
        image_mode = f"Mode: {self.current_image.mode}"
        info_text = f"{image_size}\n{image_mode}"
        self.info_label.config(text=info_text)
        
    def rotate_image(self):
        if self.current_image:
            self.rotation_angle += 90
            self.current_image = self.current_image.rotate(self.rotation_angle)
            self.displayed_image_tk = ImageTk.PhotoImage(self.current_image)
            self.save_image_to_history()
            self.display_modified_image()
    
    def flip_horizontal(self):
        if self.current_image:
            self.save_image_to_history()
            self.current_image = ImageOps.mirror(self.current_image)
            self.displayed_image_tk = ImageTk.PhotoImage(self.current_image)
            self.display_modified_image()
    
    def flip_vertical(self):
        if self.current_image:
            self.save_image_to_history()
            self.current_image = ImageOps.flip(self.current_image)
            self.displayed_image_tk = ImageTk.PhotoImage(self.current_image)
            self.display_modified_image()
    
    def display_modified_image(self):
        self.label.config(image=self.displayed_image_tk)
        self.label.image = self.displayed_image_tk

    def apply_filter(self, filter_name):
        if self.current_image:
            filtered_image = None
            if filter_name == "blur":
                filtered_image = self.current_image.filter(ImageFilter.BLUR) 
            elif filter_name == "contour":
                filtered_image = self.current_image.filter(ImageFilter.CONTOUR)
            elif filter_name == "sharpen":
                filtered_image = self.current_image.filter(ImageFilter.SHARPEN)
            elif filter_name == "smooth":
                filtered_image = self.current_image.filter(ImageFilter.SMOOTH) 
            elif filter_name == "detail":
                filtered_image = self.current_image.filter(ImageFilter.DETAIL)
            elif filter_name == "grayscale":
                filtered_image = self.current_image.convert("L") 
            
            filtered_image_tk = ImageTk.PhotoImage(filtered_image)
            self.label.config(image=filtered_image_tk)
            self.label.image = filtered_image_tk
            self.current_image = filtered_image
            self.displayed_image_tk = filtered_image_tk
            self.save_image_to_history()
            self.update_info_label()
            self.display_modified_image()
    
    def resize_image(self):
        if self.current_image:
            selected_aspect_ratio_name = self.aspect_ratio_combobox.get()
            selected_aspect_ratio = aspect_ratios[selected_aspect_ratio_name]

            new_width = int(self.current_image.height * selected_aspect_ratio)
            new_height = self.current_image.height 

            resized_img = self.current_image.resize((new_width, new_height))
            resized_img_tk = ImageTk.PhotoImage(resized_img)
            self.label.config(image=resized_img_tk)
            self.label.image = resized_img_tk
            self.displayed_image_tk = resized_img_tk
            self.current_image = resized_img
            self.update_info_label()
            self.save_image_to_history()
    
root = tk.Tk()
app = ImageViewer(root)
root.mainloop()
