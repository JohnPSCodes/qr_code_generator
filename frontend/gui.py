import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.qr_generator import QRGenerator
from backend.utils import validate_url
from PIL import ImageTk,Image

class QRApp:
    def __init__(self,root):
        self.root =  root 
        self.root.title("QR Code Generator")
        self.root.geometry("300x400")
        self.root.maxsize(300,400)
        self.root.minsize(300,400)

        # Style config using ttk
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Thick.TButton",
            font=("Segoe UI", 20, "bold"),
            padding=(12,8)
        )

        style.configure(
            "Modern.TEntry",
            padding=5,
            relief="flat"
        )

        # QR placeholder
        placeholder = Image.open(r"frontend/resources/qr_generator_placeholder.jpg")
        placeholder = placeholder.resize((200, 200))
        self.placeholder_img = ImageTk.PhotoImage(placeholder)

        # Windows content
        self.qr_label = ttk.Label(self.root,image=self.placeholder_img)
        self.qr_label.pack(pady=15)

        self.url_label = tk.Label(self.root,text="Introduce your URL here:")
        self.url_label.pack()
        self.url_entry = ttk.Entry(self.root,width=40)
        self.url_entry.pack(pady=5)

        self.generate_button = ttk.Button(self.root,text="Generate QR",command=self.generate_qr)
        self.generate_button.pack(pady=5)

        self.save_button = ttk.Button(self.root,text="Save QR",command=self.save_qr)
        self.save_button.pack(pady=5)

        self.qr_generator = None
    
    def generate_qr(self):
        """Generate and show the QR code"""
        url = self.url_entry.get()
        if validate_url(url):
            self.qr_generator = QRGenerator(url)
            self.qr_generator.generate_qr_code()
            qr_image = self.qr_generator.get_qr_image()
            self.display_qr(qr_image)
        else:
            messagebox.showerror("Error","Invalid URL")
    
    def display_qr(self,qr_img):
        """Shows the QR code image in the GUI"""
        qr_img = qr_img.resize((200,200)) # Redimenzionate
        qr_img_tk = ImageTk.PhotoImage(qr_img)
        self.qr_label.config(image=qr_img_tk)
        self.qr_label.image = qr_img_tk
    
    def save_qr(self):
        """Saves the QR code as an image in the disk storage"""
        if self.qr_generator:
            filename = "qr_code.png"
            self.qr_generator.save_qr(filename)
            messagebox.showinfo("Completed",f"QR saved as {filename}")
        else:
            messagebox.showerror("Error","Generate the QR first")