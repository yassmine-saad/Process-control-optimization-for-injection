import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import datetime

class DetectionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Detection App")
        self.geometry("800x600")

        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.pages = {}
        for PageClass in (Page1, Page2):
            page_name = PageClass.__name__
            page = PageClass(self.container, self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("Page1")

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

class Page1(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Get the path to the desktop
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        # Background image
        background_image_path = os.path.join(desktop_path, "page1.jpg")
        background_image = Image.open(background_image_path)
        background_image = background_image.resize((800, 600), Image.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = ttk.Label(self, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        # Date
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        date_label = ttk.Label(self, text=current_date, font=("Helvetica", 14))
        date_label.place(x=10, y=10)

        # Detection button
        detection_button = ttk.Button(self, text="DETECTION", command=self.start_detection, style="Green.TButton")
        detection_button.place(relx=0.5, rely=0.5, anchor="center")

    def start_detection(self):
        self.controller.show_page("Page2")

class Page2(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Get the path to the desktop
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        # Background image
        background_image_path = os.path.join(desktop_path, "page2.jpg")
        background_image = Image.open(background_image_path)
        background_image = background_image.resize((800, 600), Image.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = ttk.Label(self, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        # Run the .bat file
        self.run_detection()

    def run_detection(self):
        # Run the .bat file
        subprocess.Popen(["start", os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'), "test houssem", "start-detection.bat")])

if __name__ == "__main__":
    app = DetectionApp()
    app.mainloop()