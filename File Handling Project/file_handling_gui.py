import os
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, scrolledtext

# Main Window
root = tk.Tk()
root.title("File Handling Project")
root.geometry("500x400")
root.config(bg="#f0f0f0")


# Function to show files
def show_files():
    files = os.listdir()
    txt_area.delete(1.0, tk.END)
    txt_area.insert(tk.END, "Available Files:\n\n")
    for file in files:
        txt_area.insert(tk.END, file + "\n")


# Function to create a file
def create_file():
    filename = simpledialog.askstring("Create File", "Enter file name (without .txt):")
    if filename:
        filename += ".txt"
        if os.path.exists(filename):
            messagebox.showwarning("Warning", "File already exists!")
        else:
            content = simpledialog.askstring("File Content", "Enter text to write:")
            with open(filename, "w") as f:
                if content:
                    f.write(content)
            messagebox.showinfo("Success", f"File '{filename}' created successfully!")


# Function to read a file
def read_file():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, "r") as f:
            content = f.read()
            txt_area.delete(1.0, tk.END)
            txt_area.insert(tk.END, content)


# Function to update a file
def update_file():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        option = simpledialog.askinteger(
            "Update File", "1. Overwrite\n2. Append\n3. Rename\nEnter your choice:"
        )
        if option == 1:
            content = simpledialog.askstring("Overwrite", "Enter new content:")
            with open(filename, "w") as f:
                f.write(content)
            messagebox.showinfo("Success", "File overwritten successfully!")
        elif option == 2:
            content = simpledialog.askstring("Append", "Enter content to append:")
            with open(filename, "a") as f:
                f.write(content)
            messagebox.showinfo("Success", "Content appended successfully!")
        elif option == 3:
            new_name = simpledialog.askstring(
                "Rename", "Enter new file name (without .txt):"
            )
            if new_name:
                os.rename(filename, new_name + ".txt")
                messagebox.showinfo("Success", "File renamed successfully!")


# Function to delete a file
def delete_file():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete {os.path.basename(filename)}?",
        )
        if confirm:
            os.remove(filename)
            messagebox.showinfo("Success", "File deleted successfully!")


# Buttons
btn_create = tk.Button(root, text="Create File", width=15, command=create_file)
btn_read = tk.Button(root, text="Read File", width=15, command=read_file)
btn_update = tk.Button(root, text="Update File", width=15, command=update_file)
btn_delete = tk.Button(root, text="Delete File", width=15, command=delete_file)
btn_show = tk.Button(root, text="Show Files", width=15, command=show_files)

btn_create.pack(pady=5)
btn_read.pack(pady=5)
btn_update.pack(pady=5)
btn_delete.pack(pady=5)
btn_show.pack(pady=5)

# Text area for showing file contents
txt_area = scrolledtext.ScrolledText(root, width=60, height=10)
txt_area.pack(pady=10)

root.mainloop()
