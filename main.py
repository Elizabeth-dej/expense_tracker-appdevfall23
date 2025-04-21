import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
import csv

# Connect to SQLite database
conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

# Create table if not exists
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

predefined_categories = ["Food", "Rent", "Transport", "Utilities", "Entertainment", "Shopping", "Health", "Other"]

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        print("Choose a category:")
        for i, cat in enumerate(predefined_categories, 1):
            print(f"{i}. {cat}")
        cat_choice = int(input("Enter the category number: "))
        category = predefined_categories[cat_choice - 1]
        description = input("Enter description (optional): ")
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cur.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                    (amount, category, description, date))
        conn.commit()
        print("\u2705 Expense added successfully!\n")

    except (ValueError, IndexError):
        print("\u274C Invalid input. Please try again.\n")

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

def filter_expenses():
    print("Filter by:")
    print("1. Category")
    print("2. Date (YYYY-MM-DD)")
    choice = input("Enter your choice: ")

    if choice == '1':
        category = input("Enter category name: ")
        cur.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    elif choice == '2':
        date = input("Enter date (YYYY-MM-DD): ")
        cur.execute("SELECT * FROM expenses WHERE date LIKE ?", (f"{date}%",))
    else:
        print("\u274C Invalid choice.\n")
        return

    expenses = cur.fetchall()
    if expenses:
        for expense in expenses:
            print(f"ID: {expense[0]} | Amount: ${expense[1]:.2f} | Category: {expense[2]} | Description: {expense[3]} | Date: {expense[4]}")
    else:
        print("No matching expenses found.\n")

def delete_expense():
    try:
        expense_id = int(input("Enter the ID of the expense to delete: "))
        cur.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        print("\u2705 Expense deleted successfully!\n")
    except ValueError:
        print("\u274C Invalid ID.\n")

def edit_expense():
    try:
        expense_id = int(input("Enter the ID of the expense to edit: "))
        cur.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
        expense = cur.fetchone()
        if expense:
            print(f"Current values: Amount=${expense[1]}, Category={expense[2]}, Description={expense[3]}")
            amount = float(input("Enter new amount: "))
            print("Choose new category:")
            for i, cat in enumerate(predefined_categories, 1):
                print(f"{i}. {cat}")
            cat_choice = int(input("Enter the category number: "))
            category = predefined_categories[cat_choice - 1]
            description = input("Enter new description: ")

            cur.execute("UPDATE expenses SET amount=?, category=?, description=? WHERE id=?",
                        (amount, category, description, expense_id))
            conn.commit()
            print("\u2705 Expense updated successfully!\n")
        else:
            print("\u274C Expense not found.\n")
    except (ValueError, IndexError):
        print("\u274C Invalid input.\n")

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

def export_to_csv():
    cur.execute("SELECT * FROM expenses")
    expenses = cur.fetchall()
    if not expenses:
        print("No data to export.\n")
        return
    with open("expenses_export.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Amount", "Category", "Description", "Date"])
        writer.writerows(expenses)
    print("\u2705 Expenses exported to expenses_export.csv\n")

def main():
    while True:
        print("====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses")
        print("4. Edit Expense")
        print("5. Delete Expense")
        print("6. Visualize Expenses")
        print("7. Export Expenses to CSV")
        print("8. Exit")
        choice = input("Choose an option (1-8): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_expenses()
        elif choice == '4':
            edit_expense()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            visualize_expenses()
        elif choice == '7':
            export_to_csv()
        elif choice == '8':
            print("Goodbye! \U0001F44B")
            break
        else:
            print("\u274C Invalid choice. Please try again.\n")

    conn.close()

if __name__ == "__main__":
    main()
