import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

# Create a table for storing expenses if it doesn't already exist
cur.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    description TEXT,
    date TEXT
)
''')
conn.commit()

# Function to add a new expense
def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Rent, Transport): ")
        description = input("Enter description (optional): ")
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cur.execute(
            "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
            (amount, category, description, date)
        )
        conn.commit()
        print("✅ Expense added successfully!\n")

    except ValueError:
        print("❌ Invalid amount. Please enter a number.\n")

# Function to view all expenses
def view_expenses():
    cur.execute("SELECT * FROM expenses")
    expenses = cur.fetchall()

    if expenses:
        print("\n==== All Expenses ====")
        for expense in expenses:
            print(f"ID: {expense[0]} | Amount: ${expense[1]:.2f} | Category: {expense[2]} | Description: {expense[3]} | Date: {expense[4]}")
        print("")
    else:
        print("No expenses recorded yet.\n")

# Function to visualize spending by category
def visualize_expenses():
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cur.fetchall()

    if not data:
        print("No data to visualize.\n")
        return

    categories = [row[0] for row in data]
    totals = [row[1] for row in data]

    plt.figure(figsize=(6, 6))
    plt.pie(totals, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Expenses by Category")
    plt.show()

# Main menu loop
while True:
    print("====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Visualize Expenses")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        visualize_expenses()
    elif choice == '4':
        print("Goodbye! 👋🏾")
        break
    else:
        print("❌ Invalid choice. Please try again.\n")

# Close the database connection
conn.close()
