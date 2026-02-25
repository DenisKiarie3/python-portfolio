# grade_manager.py

def calculate_grade(score):
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"
    
def add_student():
    try:
        name = input("Student Name: ")
        score = float(input("Score (0.0 - 1.0): "))

        if score < 0.0 or score > 1.0:
            raise ValueError("Score must be between 0.0 and 1.0.")
        
        grade = calculate_grade(score)

        student = {
            "name" : name,
            "score" : score,
            "grade" : grade
        }

        print("\n=== Student Record ===")
        print(f"Name: {student['name']}")
        print(f"Score: {student['score']:.2f}")
        print(f"Grade: {student['grade']}")

    except ValueError as error:
        print(f"Error: {error}")

def main():
    print("=== Grade Manager ===")
    print("1. Add Student")
    print("2. Exit")

    choice = input("Select Option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        print("Exiting Grade Manager.")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()