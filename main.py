import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
import matplotlib.pyplot as plt
import os

# Initializes an empty list to store expense data
expenses = []

# Predefined expense categories
categories = ["Food", "Entertainment", "Utilities", "Housing", "Shopping", "Transportation", "Other"]

# Start by defining the menu options
# First function is an add expense function for users to add their expenses.
def add_expense():
    '''
    Function to add expense.
    '''
    print("Add Expense: ")
    expense_name = input("Expense Name: ")
    amount  = float(input("Amount: "))

    # Print the categories and allow the user to choose
    print("Choose a category")
    for i, category in enumerate(categories,start=1):
        print (str(i) + ',' + category)
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
        "Name": expense_name,
        "Amount": amount,
        "Category": category,
        "Date": date
    }
    expenses.append(expense)
    print("Expense added successfully!")

# Second Function is to save  expenses to a CSV
def save_to_csv():
    csv_file = "expenses.csv"

# Check if the CSV file exists and create a header row if it does
    file_exists = False
    try:
        with open(csv_file,"r") as file:
            if file.read(1):
                file_exists = True
    except FileNotFoundError:
        pass
    
    with open(csv_file, "a", newline="") as file:
        fieldnames = ["Name", "Amount", "Category", "Date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        for expense in expenses:
            writer.writerow(expense)
def edit_expense():
    if not expenses:
        print("No expenses to edit.")
        return

    print("Edit Expense:")
    
    # Display a numbered list of expenses for the user to choose from
    print("Select an expense to edit:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['Name']} - {expense['Date']}")

    try:
        expense_choice = int(input("Enter the expense number to edit: "))
    except ValueError:
        print("Invalid input. Please enter a valid expense number.")
        return

    if 1 <= expense_choice <= len(expenses):
        selected_expense = expenses[expense_choice - 1]
        print("Selected Expense:")
        print(f"Name: {selected_expense['Name']}")
        print(f"Amount: {selected_expense['Amount']}")
        print(f"Category: {selected_expense['Category']}")
        print(f"Date: {selected_expense['Date']}")
        
        print("\nEdit Expense Details:")

        name = input("Name (Press Enter to keep the current value): ")
        if name:
            selected_expense['Name'] = name

        amount = input("Amount (Press Enter to keep the current value): ")
        if amount:
            selected_expense['Amount'] = float(amount)

        print("Select a new category (Press Enter to keep the current value):")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        try:
            category_choice = int(input("Enter the category number: "))
        except (ValueError, IndexError):
            print("Invalid category choice. The category will remain unchanged.")
        else:
            selected_expense['Category'] = categories[category_choice - 1]

        date = input("Date (YYYY-MM-DD) (Press Enter to keep the current value): ")
        if date:
            selected_expense['Date'] = date

        print("Expense edited successfully.")
    else:
        print("Invalid expense number. Please enter a valid expense number.")


    #code for edit expense function
    #print("code not finished")
def delete_expense(): 
    if not expenses:
        print("No expenses to delete.")
        return

    print("Delete Expense:")
    
    # Display a numbered list of expenses for the user to choose from
    print("Select an expense to delete:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['Name']} - {expense['Date']}")

    try:
        expense_choice = int(input("Enter the expense number to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid expense number.")
        return

    if 1 <= expense_choice <= len(expenses):
        deleted_expense = expenses.pop(expense_choice - 1)
        print("Deleted Expense:")
        print(f"Name: {deleted_expense['Name']}")
        print(f"Amount: {deleted_expense['Amount']}")
        print(f"Category: {deleted_expense['Category']}")
        print(f"Date: {deleted_expense['Date']}")
        print("Expense deleted successfully.")
    else:
        print("Invalid expense number. Please enter a valid expense number.")

    #code for delete expense function
    #print("code not finished")
def view_expense():
    #code for view expense function
    #print("code not finished")
def generate_report():
    #code for generate report function
    print("code not finished")
def exit():
    #code for exit function
    print("code not finished")
def main():
    while True:    
        ''' 
        This is the main function to show to users 
        '''
        print("Welcome to the Expense tracker.")

        print("""
            Welcome to the Expense tracker.
            [1] - Add Expense
            [2] - Edit Expense
            [3] - Delete Expense
            [4] - View expenses
            [5] - Generate Report
            [6] - Exit
            """)
        
        action = input("What would you like to do? ")
        if action == "1":
            add_expense()
        elif action == "2":
            edit_expense()
        elif action == "3":
            delete_expense()
        elif action == "4":
            view_expense
        elif action == "5":
            generate_report()
        elif action == "6":
            exit()
        else:
            print("Invalid option. Please try again")
if __name__ == "__main__":
    main()
