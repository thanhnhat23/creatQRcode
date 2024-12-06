import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
import os

def generateQRcode(url, filename):
    if not url:
        messagebox.showerror("Error", "Please enter URL to generate QR.")
        return
    try:
        if not filename.lower().endswith('.png'):
            filename += '.png'
        image = qrcode.make(url)
        image.save(filename)
        messagebox.showinfo("Completed", f"QR code has been created: {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Can't create QR: {str(e)}")

def selectURLandSave():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Errol", "Please enter URL.")
        return
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filename:
        generateQRcode(url, filename)

root = tk.Tk()
root.title("Generate QR code from URL")
root.geometry("400x200")

title_label = tk.Label(root, text="Generate QR code from URL", font=("Arial", 16))
title_label.pack(pady=20)

url_label = tk.Label(root, text="Enter URL to generate QR:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR", command=selectURLandSave)
generate_button.pack(pady=20)

root.mainloop()
