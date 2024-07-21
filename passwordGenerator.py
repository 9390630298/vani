import tkinter as tk
from tkinter import ttk
import random
import string


def generate_password(length=12):
    if length < 4:  # Ensure minimum length for a reasonable password
        raise ValueError("Password length should be at least 4")

    # Characters to choose from
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has at least one of each: upper, lower, digit, special
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)


def generate_password_button_click():
    length = int(length_entry.get())
    password = generate_password(length)
    password_entry.config(state=tk.NORMAL)  # Enable entry for writing
    password_entry.delete(0, tk.END)  # Clear any existing password
    password_entry.insert(0, password)  # Insert generated password
    password_entry.config(state=tk.DISABLED)  # Disable entry after displaying


# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create a custom style for the widgets
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), foreground='blue')  # Change label font and color
style.configure('TEntry', font=('Arial', 12))  # Change entry font

# Create labels and entries for password generation
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = ttk.Entry(root, width=10)
length_entry.insert(0, "12")  # Default password length
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password_button_click)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

password_label = ttk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)

password_entry = ttk.Entry(root, width=30)
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
