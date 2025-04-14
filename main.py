import sqlite3
from datetime import datetime

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

# Create a table for storing expenses if it doesn't already exist
cur.execute('''CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                category TEXT,
                description TEXT,
                date TEXT
                )''')

conn.commit()

# Function to add a new expense
def add_expense(amount, category, description):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                (amount, category, description, date))
    conn.commit()
    print("Expense added successfully.")

# Function to view all expenses
def view_expenses():
    cur.execute("SELECT * FROM expenses")
    expenses = cur.fetchall()
    if expenses:
        for expense in expenses:
            print(f"ID: {expense[0]} | Amount: ${expense[1]} | Category: {expense[2]} | Description: {expense[3]} | Date: {expense[4]}")
    else:
        print("No expenses recorded yet.")

# Main menu
while True:
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Visualize Expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Rent, Transport): ")
        description = input("Enter description (optional): ")
        add_expense(amount, category, description)
        
    elif choice == '2':
        view_expenses()
        
    elif choice == '3':
        visualize_expenses()
        
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
