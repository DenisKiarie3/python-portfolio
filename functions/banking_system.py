# banking_system.py

def deposit(balance, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    return balance + amount

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if amount > balance:
        raise ValueError("Insufficient funds.")
    return balance - amount

def main():
    balance = 1000.0

    print("=== Banking System ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")

    choice = input("Select Option: ")

    try:
        if choice == "1":
            amount = float(input("Amount to deposit: "))
            balance = deposit(balance, amount)
            print(f"New Balance: {balance:.2f}")
        elif choice == "2":
            amount = float(input("Amount to withdraw: "))
            balance = withdraw(balance, amount)
            print(f"New Balance: {balance:.2f}")
        elif choice == "3":
            print(f"Current Balance: {balance:.2f}")
        else:
            print("Invalid option.")
    except ValueError as error:
        print("Error: {error}")

if __name__ == "__main__":
    main()
