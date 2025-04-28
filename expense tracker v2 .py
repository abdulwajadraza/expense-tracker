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

#defining a function to get valid date input
def get_valid_date(prompt):
    while True:
        date_input = input(prompt).strip()
        try:
            #try converting the input to date
            datetime.strftime(date_input, "%Y-%m-%d")
            return date_input #if no error, it will return the valid date
        except ValueError:
            print("Enter a valid date format! Please enter date in YYYY-MM-DD format.")


#defining a function to add expenses
def add_expenses():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category as food, vegetables, medicine, guests, traveling, education, misc.: ")
    description = input("Enter detailed description about the expense: ")
    today = datetime.now().strftime("%Y-%m-%d")
    use_today = input(f"Use today date ({today})? (y/n): ")
    if use_today == "y":
        date = today
    else:
        date = get_valid_date("Enter the date YYYY-MM-DD: ")

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
    total_expense()
    
#calculate total expenses
def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total expenses are: {total:.2f}")

#defining a function to filter expenses by category
def filter_by_cat ():
    category = input("Enter the category you want to filter by: ").strip().lower()
    found = False

    for i, exp in enumerate(expenses, start=1):
        if exp['category'].lower() == category:
            print(f"{i}. {exp['date']} - {exp['amount']:.2f} - {exp['category']} - {exp['description']}")
            found = True
    if not found:
        print(f"No expense found for '{category}'.")

#defining a function to filter expenses by date
def filter_by_date():
    today = datetime.now().strftime("%Y-%m-%d")
    use_today = input(f"Do you want to filter by today's date ({today})? (y/n): ").strip().lower()
    
    if use_today == "y":
        date = today
    else:
        date = get_valid_date("Enter the date YYYY-MM-DD: ")

    found = False

    for i, exp in enumerate(expenses, start=1):
        if exp['date'] == date:
            print(f"{i}. {exp['date']} - {exp['amount']} - {exp['category']} - {exp['description']}")
           

#defining a function to generate monthly expense report
def monthly_report ():
    month = input("Enter the month to get expense report for (fomrat YYYY:MM): ")
    total = 0
    found  = False

    for i, exp in enumerate(expenses, start=1):
        if exp["date"].startswith(month):
            print(f"{i}. {exp['date']} - {exp['amount']} - {exp['category']} - {exp['description']}")
            total += exp["amount"]
            found = True

    if found:
        print(f"Total spending for {month}: {total: .2f}")
    else:
        print(f"No expenses found for {month}.")



#defining main loop to run the program
def main():
    while True:
        print("\nExpense Tracker Options: ")
        print("1. Add Expenses")
        print("2. View expenses")
        print("3. View Total Spendings")
        print("4. Filter by Date")
        print("5. Filter by Category")
        print("6. Monthly Report")
        print("7. Quit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            filter_by_date()
        elif choice == "5":
            filter_by_cat()
        elif choice == "6":
            monthly_report()
        elif choice == "7":
            print("Good bye!")
            break
        else:
            print("Invalid choice, please select again.")

#load the expense at start
expenses = load_expenses()

#running the program
if __name__ == "__main__":
    main()
