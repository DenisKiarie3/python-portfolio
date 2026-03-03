# expense_tracker.py

def get_none_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount must be non-negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a number.")

def main():
    expenses = []
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("Select an option (1 - 4): ")

        if choice == "1":
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = get_none_negative_float("Enter amount: ")
            expenses.append({"category": category, "description": description, "amount": amount})
            print("Expense added successfully!")

        elif choice == "2":
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\n--- All Expenses ---")
                for idx, exp in enumerate(expenses, 1):
                    print(f"{idx}. {exp['category']} | {exp['description']} | ${exp['amount']:.2f}")
        
        elif choice == "3":
            total = sum(exp["amount"] for exp in expenses)
            print(f"Total expenses: $ {total:.2f}")

        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-4.")

if __name__ == "__main__":
    main()