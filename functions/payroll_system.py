# payroll_system.py
def get_float_input(prompt):
    """
    Safely gets a float input from the user.
    Raises ValueError if invalid.
    """
    value = float(input(prompt))
    if value < 0:
        raise ValueError("Input must be non-negative.")
    return value

def calculate_regular_pay(hours, rate):
    """
    Calculates regular pay for up to 40 hours.
    """
    return min(hours, 40) * rate

def calculate_overtime_pay(hours, rate):
    """
    Calculates overtime pay for hours above 40.
    """
    if hours > 40:
        overtime_hours = hours - 40
        return overtime_hours * rate * 1.5
    return 0

def calculate_total_pay(hours, rate):
    """
    Returns total gross pay
    """
    regular = calculate_regular_pay(hours, rate)
    overtime = calculate_overtime_pay(hours, rate)
    return regular + overtime

def main():
    try:
        hours = get_float_input("Enter hours worked: ")
        rate = get_float_input("Enter hourly rate: ")
        total_pay = calculate_total_pay(hours, rate)
        print(f"Gross Pay: {total_pay:.2f}")
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()