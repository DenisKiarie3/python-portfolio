def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit -32) * 5/9

choice = input("Convert (C)elsius or (F)ahrenheit? ").lower()

if choice == "c":
    c = float(input("Enter Celsius: "))
    print(f"Fahrenheit: {celsius_to_fahrenheit(c):.2f}")
elif choice == "f":
    f = float(input("Enter Fahrenheit: "))
    print(f"Celsius: {fahrenheit_to_celsius(f):.2f}")
else:
    print("Invalid choice.")