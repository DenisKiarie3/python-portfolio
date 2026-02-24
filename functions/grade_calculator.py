# grade_calculator.py

def get_valid_score():
    """
    Prompts the user for a score between 0.0 and 1.0.
    Returns a valid float.
    Raises ValueError if invalid.
    """

    score_input = input("Enter a score between 0.0 and 1.0: ")
    score = float(score_input)

    if score < 0.0 or score > 1.0:
        raise ValueError("Score must be between 0.0 and 1.0.")
    return score

def calculate_grade(score):
    """
    Returns the letter grade based on score.
    """
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
    
def main():
    try:
        score = get_valid_score()
        grade = calculate_grade(score)
        print(f"Grade: {grade}")
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()