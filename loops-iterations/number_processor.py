# number_processor.py
def get_non_negative_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Number must be non-negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a number.")

def main():
    while True:
        try:
            count = int(input("How many numbers will you enter? "))
            if count <= 0:
                print("Count must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter an integer.")

    numbers = []

    for i in range(count):
        num = get_non_negative_number(f"Enter number {i + 1}: ")
        numbers.append(num)

    total = sum(numbers)
    average = total/count
    maximum = max(numbers)
    minimum = min(numbers)

    print("\n--- Report ---")
    print(f"Numbers entered: {numbers}")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

if __name__ == "__main__":
    main()