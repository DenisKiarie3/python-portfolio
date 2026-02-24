# simple_interest.py

def calculate_simple_interest(principle, rate, time):
    return principle * rate * time

p = float(input("Principle: "))
r = float(input("Rate (decimal): "))
t = float(input("Time (years): "))

interest = calculate_simple_interest(p, r, t)
print(f"Simple Interest: {interest:.2f}")