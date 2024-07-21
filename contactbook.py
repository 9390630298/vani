import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Define custom styles
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 12), foreground='black')  # Label style
        self.style.configure('TButton', font=('Helvetica', 12))  # Button style
        self.style.configure('TFrame', background='#e0f7fa')  # Frame background color

        # Main frame
        main_frame = ttk.Frame(self.root, padding=(20, 10))
        main_frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Contact list frame
        contact_list_frame = ttk.Frame(main_frame)
        contact_list_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)

        # Contacts listbox
        self.contacts_listbox = tk.Listbox(contact_list_frame, font=('Helvetica', 12), width=30, height=10)
        self.contacts_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)

        # Buttons
        add_button = ttk.Button(buttons_frame, text="Add Contact", command=self.add_contact)
        add_button.pack(pady=5, fill=tk.X)

        edit_button = ttk.Button(buttons_frame, text="Edit Contact", command=self.edit_contact)
        edit_button.pack(pady=5, fill=tk.X)

        delete_button = ttk.Button(buttons_frame, text="Delete Contact", command=self.delete_contact)
        delete_button.pack(pady=5, fill=tk.X)

        search_button = ttk.Button(buttons_frame, text="Search by Last Name", command=self.search_contact)
        search_button.pack(pady=5, fill=tk.X)

        # Set grid weights to make the frames resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Example contacts (replace with your data handling logic)
        self.contacts = ["John Doe", "Jane Smith", "Alice Johnson"]
        self.update_contacts_list()

    def update_contacts_list(self):
        # Clear existing list
        self.contacts_listbox.delete(0, tk.END)

        # Sort contacts by last name (assuming last name is separated by space)
        sorted_contacts = sorted(self.contacts, key=lambda contact: contact.split()[-1])

        # Add sorted contacts to listbox
        for contact in sorted_contacts:
            self.contacts_listbox.insert(tk.END, contact)

    def add_contact(self):
        # Function for adding a contact
        first_name = simpledialog.askstring("Add Contact", "Enter first name:")
        if first_name:
            last_name = simpledialog.askstring("Add Contact", "Enter last name:")
            if last_name:
                new_contact = f"{first_name} {last_name}"
                self.contacts.append(new_contact)
                self.update_contacts_list()

    def edit_contact(self):
        # Function for editing a contact
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts_listbox.get(selected_index)
            new_name = simpledialog.askstring("Edit Contact", "Enter new name:", initialvalue=selected_contact)
            if new_name:
                self.contacts[selected_index[0]] = new_name
                self.update_contacts_list()

    def delete_contact(self):
        # Function for deleting a contact
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]
            self.update_contacts_list()

    def search_contact(self):
        # Function for searching a contact by last name
        last_name = simpledialog.askstring("Search Contact", "Enter last name:")
        if last_name:
            matches = [contact for contact in self.contacts if contact.split()[-1] == last_name]
            if matches:
                messagebox.showinfo("Search Results", "\n".join(matches))
            else:
                messagebox.showinfo("Search Results", "No contacts found with that last name.")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = ContactBookApp(root)
    root.mainloop()
