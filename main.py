import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
import matplotlib.pyplot as plt

# Initializes an empty list to store expense data
expenses = []

# Predefined expense categories
categories = ["Food", "Entertainment", "Utilities", "Housing", "Shopping", "Transportation", "Other"]

# Start by defining the menu options
def add_expense():
    '''
    Function to add expense.
    '''
    print("Add Expense: ")
    expense = input("Expense Name: ")
    amount  = float(input("Amount: "))

    # Print the categories and allow the user to choose
    print("Choose a category")
    for i, category in enumerate(categories,start=1):
        print (i + ',' + category)
    try:
        category_choice = int(input("Enter the category number: "))
        category = category_choice - 1
    except (ValueError, IndexError):
        print("Invalid category choice")
        return

    date = input("Date  (YYYY-MM-DD): ")    
    
    # Create user validations here

    # Dictionary to define expense 
    expense = {
        "Name": name,
        "Amount": amount,
        "Category": category,
        "Date": date
    }
    expenses.append(expense)
    print("Expense added successfully!")

