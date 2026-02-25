# cli_payroll_system.py

def get_float_input(prompt):
    try:
        value = float(input(prompt))
        if value < 0:
            raise ValueError("Value must be non-negative.")
        return value
    except ValueError:
        raise ValueError("Invalid numeric input.")
    
def calculate_pay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        return regular_pay + overtime_pay
    
def process_employee():
    name = input("Employee Name: ")
    hours = get_float_input("Hours Worked: ")
    rate = get_float_input("Hourly Rate: ")

    gross_pay = calculate_pay(hours, rate)

    print("\n=== Payroll Summary ===")

    print(f"Employee: {name}")
    print(f"Gross Pay: {gross_pay:.2f}")

def main():
    print("=== Payroll System ===")
    print("1. Process payroll.")
    print("2. Exit.")

    choice = input("Select Option: ")

    if choice == "1":
        try:
            process_employee()
        except ValueError as error:
            print(f"Error: {error}")
    elif choice == "2":
        print("Exiting Payroll System.")
    else:
        print("Invalid Option.")

if __name__ == "__main__":
    main()
