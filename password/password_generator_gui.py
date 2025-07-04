import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter desired password length:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="Password: ")
result_label.pack(pady=10)

root.mainloop()
