import tkinter as tk
from tkinter import StringVar

# Define the main window
root = tk.Tk()
root.title("Personal Expense Tracker")

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


