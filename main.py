
import json


class ExpenseTracker:

    def __init__(self):
        self.filename = "expenses.json"
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("Expense file is empty or incorrect.")
            return []

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        title = input("Enter expense name: ")

        if title == "":
            print("Expense name cannot be empty.")
            return

        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

        except ValueError:
            print("Please enter a valid amount.")
            return

        expense_id = 1

        for expense in self.expenses:
            if expense["id"] >= expense_id:
                expense_id = expense["id"] + 1

        expense = {
            "id": expense_id,
            "title": title,
            "amount": amount
        }

        self.expenses.append(expense)
        self.save_expenses()

        print("Expense added successfully!")

    def list_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found.")
            return

        print("\n----- All Expenses -----")

        for expense in self.expenses:
            print("ID:", expense["id"])
            print("Name:", expense["title"])
            print("Amount: Rs.", expense["amount"])
            print("-------------------")

    def delete_expense(self):
        if len(self.expenses) == 0:
            print("No expenses available to delete.")
            return

        self.list_expenses()

        try:
            expense_id = int(input("\nEnter expense ID to delete: "))

        except ValueError:
            print("Please enter a valid ID.")
            return

        for expense in self.expenses:
            if expense["id"] == expense_id:
                self.expenses.remove(expense)
                self.save_expenses()
                print("Expense deleted successfully!")
                return

        print("Expense ID not found.")

    def total_expenses(self):
        total = 0

        for expense in self.expenses:
            total = total + expense["amount"]

        print("\nTotal Expenses: Rs.", total)


def main():

    tracker = ExpenseTracker()

    while True:
        print("\n----- EXPENSE TRACKER -----")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Delete Expense")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.list_expenses()

        elif choice == "3":
            tracker.delete_expense()

        elif choice == "4":
            tracker.total_expenses()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
            
        else:
            print("Invalid selection. Please choose number between (1 to 5).")

if __name__ == "__main__":
     
     main()