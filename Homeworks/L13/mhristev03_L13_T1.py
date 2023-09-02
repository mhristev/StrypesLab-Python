import tkinter as tk
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class RSSApp:
    def __init__(self, root):
        self.items = {}
        
        self.root = root
        self.root.title("Slashdot RSS Reader")

        self.title_label = tk.Label(root, text="Slashdot RSS Reader", font=("", 16, "bold"))
        self.title_label.pack(pady=10)

        self.listbox_frame = tk.Frame(root)
        self.listbox_frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(self.listbox_frame, selectmode=tk.SINGLE, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.scrollbar.configure(command=self.listbox.yview)

        self.content_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
        self.content_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.load_button = tk.Button(root, text="Load RSS", command=self.load_rss)
        self.load_button.pack(pady=10)

    
    def save_rss(self):
        url = "https://rss.slashdot.org/Slashdot/slashdot"
        local_filename = "slashdot.rss"
        urlretrieve(url, local_filename)
        print(f"File saved as {local_filename}")
    
    def load_rss(self):
        self.listbox.delete(0, tk.END)
        self.content_text.config(state=tk.NORMAL)
        self.content_text.delete("1.0", tk.END)
        
        self.save_rss()
        content = None
        
        with open("slashdot.rss", "r") as file:
            content = file.read()
        
        if content != None:
            item_start = 0
            item_start = content.find("<item ", item_start)
            
            while item_start != -1:
                item_end = content.find("</item>", item_start)
                item = content[item_start:item_end]
                
                title_start = item.find("<title>") + len("<title>")
                title_end = item.find("</title>", title_start)
                title = item[title_start:title_end]
                
                description_start = item.find("<description>") + len("<description>")
                description_end = item.find("</description>", description_start)
                description = item[description_start:description_end]
                cleaned_description = description.split("&lt;p&gt;&lt;")[0]

                self.listbox.insert(tk.END, title.strip())
                self.items[title.strip()] = cleaned_description.strip()

                item_start = item_end + len("</item>")
                item_start = content.find("<item ", item_start)

            self.content_text.config(state=tk.DISABLED)

    def on_select(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_entry = selected_index[0]
            selected_item_value = self.listbox.get(selected_entry) 
            self.display_description(self.items[selected_item_value])

    def display_description(self, content):
        self.content_text.config(state=tk.NORMAL)
        self.content_text.delete("1.0", tk.END)
        self.content_text.insert(tk.END, content)
        self.content_text.config(state=tk.DISABLED)


root = tk.Tk()
app = RSSApp(root)
root.mainloop()

