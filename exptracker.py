import tkinter as tk
from tkinter import StringVar
import sqlite3
from Matplotlib import pyplot as plt

# Define the main window
root = tk.Tk()
root.title("Personal Expense Tracker")

# Create the labels and entries
date_label = tk.Label(root, text="Date:")
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=5, pady=5)

category_label = tk.Label(root, text="Category:")
category_label.grid(row=1, column=0, padx=5, pady=5)
category = ["Food", "Shopping", "Entertainment", "Utilities", "Transportation", "Health", "Education", "Other"]
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1, padx=5, pady=5)

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=2, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

notes_label = tk.Label(root, text="Notes:")
notes_label.grid(row=3, column=0, padx=5, pady=5)
notes_entry = tk.Entry(root)
notes_entry.grid(row=3, column=1, padx=5, pady=5)

# Define the variables
def get_entry_values():
    """Get the values from the entries."""
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    notes = notes_entry.get()
    return date, category, amount, notes

# Print the entries
print(f"Date: {date}\nCategory: {category}\nAmount: {amount}\nNotes: {notes}")

# Clear inputs after submission
date_entry.delete(0, tk.END)
amount_entry.delete(0, tk.END)
notes_entry.delete(0, tk.END)

# Dropdown menu for category
category_var = StringVar(root)
category_var.set(category[0])
category_dropdown = tk.OptionMenu(root, category_var, *category)
category_dropdown.grid(row=1, column=1, padx=5, pady=5)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=get_entry_values)
submit_button.grid(row=4, column=1, padx=5, pady=5)

# Start the main loop
root.mainloop()

# Connect to the database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create the table
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (date text, category text, amount real, notes text)''')

# Insert new entry into the database
date, category, amount, notes = get_entry_values()
c.execute("INSERT INTO expenses VALUES (?, ?, ?, ?)", (date, category, amount, notes))

# Commit the changes
conn.commit()

# Data Validation and Error Handling
try:
    if date == '':
        raise ValueError
    if category == '':
        raise ValueError
    if amount == str(''):
        raise ValueError
    if notes == '':
        raise ValueError
except ValueError:
    print("Error: Please fill in all required fields.")
    exit()
# Make sure that the date is in the correct format

# Add a delete button
# Add a search function

