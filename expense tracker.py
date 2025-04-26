#expense tracker app
#importing required libraries such as json, os etc.
import json
import os
from datetime import datetime

#defining a function of load existing expenses 
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    return[]

#defining save expenses function to save expenses in a expenses file
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

#defining a function to add expenses
def add_expenses():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category as food, vegetables, medicine, guests, traveling, education, misc.: ")
    description = input("Enter detailed description about the expense: ")
    date = datetime.now().strftime("%Y-%m-%d") #to enter today date

    expenses.append({
        "amount" : amount,
        "category" : category,
        "description" : description,
        "date" : date
    })
    save_expenses()
    print("Expense added successfully!")

#view all expneses
def view_expenses():
    if not expenses:
        print("No expense added yet")
        return
    
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} - {exp['amount']:.2f} - {exp['category']} - {exp['description']}")

#calculate total expenses
def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total expenses are: {total:.2f}")

#defining main loof to run the program

def main():
    while True:
        print("\nExpense Tracker Options: ")
        print("1. Add Expenses")
        print("2. View expenses")
        print("3. View Total Spendings")
        print("4. Quit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Good by!")
            break
        else:
            print("Invalid choice, please select again.")

#load the expense at start
expenses = load_expenses()

#running the program
if __name__ == "__main__":
    main()

