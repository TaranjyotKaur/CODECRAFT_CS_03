import re


def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    # Digit Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character.")

    return score, feedback


def display_strength(score):
    if score <= 2:
        return "🔴 Weak"
    elif score <= 4:
        return "🟡 Moderate"
    else:
        return "🟢 Strong"


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")

    score, feedback = check_password_strength(password)
    strength = display_strength(score)

    print("\nPassword Strength:", strength)
    print("Score:", score, "/ 6")

    if feedback:
        print("\nSuggestions to improve:")
        for item in feedback:
            print(item)
    else:
        print("\n✅ Excellent password!")


if __name__ == "__main__":
    main()