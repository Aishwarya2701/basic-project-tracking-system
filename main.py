import tkinter as tk
from tkinter import ttk
from datetime import datetime

def add_project():
    project_name = entry_add.get()
    if project_name.strip():  # Ensure project name is not empty
        current_time = datetime.now()
        date_created = current_time.strftime("%Y-%m-%d")
        time_created = current_time.strftime("%H:%M:%S")
        listbox.insert("", tk.END, values=(len(listbox.get_children()) + 1, project_name, date_created, time_created))
        entry_add.delete(0, tk.END)  # Clear the entry field

def remove_project():
    selected_item = listbox.selection()
    if selected_item:  # Check if an item is selected
        listbox.delete(selected_item)
        # Update the serial numbers of remaining projects
        for i, item in enumerate(listbox.get_children(), start=1):
            listbox.item(item, values=(i,) + listbox.item(item, "values")[1:])

def rename_project(event=None):
    selected_item = listbox.selection()
    if selected_item:  # Check if an item is selected
        project_name = listbox.item(selected_item, "values")[1]
        entry_add.delete(0, tk.END)
        entry_add.insert(tk.END, project_name)
        entry_add.focus_set()  # Set focus to the entry field
        entry_add.bind("<Return>", lambda event: update_project(selected_item))  # Bind Enter key to update project name

def update_project(selected_item):
    new_name = entry_add.get().strip()
    if new_name:  # Ensure new name is not empty
        original_serial = listbox.item(selected_item, "values")[0]
        listbox.item(selected_item, values=(original_serial, new_name) + listbox.item(selected_item, "values")[2:])
    entry_add.delete(0, tk.END)  # Clear the entry field
    entry_add.unbind("<Return>")  # Unbind the Enter key event

# Create a root window
root = tk.Tk()
root.title("Project Manager")
root.geometry("900x600")  # Set the window size

# Text field for entering project name
entry_add = tk.Entry(root, width=70)  # Increased width to 70 characters
entry_add.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Button to add project
add_button = tk.Button(root, text="Add Project", command=add_project)
add_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Listbox to display projects
columns = ("Sr No.", "Project Name", "Date Created", "Time Created")
listbox = ttk.Treeview(root, columns=columns, show="headings")
listbox.heading("Sr No.", text="Sr No.")
listbox.heading("Project Name", text="Project Name")
listbox.heading("Date Created", text="Date Created")
listbox.heading("Time Created", text="Time Created")
listbox.column("Sr No.", width=50)
listbox.column("Project Name", width=200)
listbox.column("Date Created", width=150)
listbox.column("Time Created", width=150)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Context menu for right-click options
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Rename Project", command=rename_project)
context_menu.add_command(label="Remove Project", command=remove_project)

# Bind right-click event to listbox
listbox.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))

# Run the Tkinter event loop
root.mainloop()
