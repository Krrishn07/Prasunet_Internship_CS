'''

Task-03      : Password Complexity Checker
File Name    : Prasunet_CS_03
Organization : Prasunet Pvt.Ltd. Company

'''

# Importing regular expressions module
import re

# Function to check if password meets minimum length requirement
def check_length(password):
    return len(password) >= 8

# Function to check if password contains at least one uppercase letter
def check_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

# Function to check if password contains at least one lowercase letter
def check_lowercase(password):
    return bool(re.search(r'[a-z]', password))

# Function to check if password contains at least one digit
def check_number(password):
    return bool(re.search(r'[0-9]', password))

# Function to check if password contains at least one special character
def check_special_characters(password):
    return bool(re.search(r'[!@#$%^&*()_+{}|:"<>?,./;[\]]', password))

# Function to provide feedback on password requirements
def password_feedback(password):
    feedback = []
    
    if not password or password.isspace():
        feedback.append("Password cannot be empty or contain only spaces.")
        return feedback  # No need to check further if the password is invalid

    if not check_length(password):
        feedback.append("Password should be at least 8 characters long.")
    if not check_uppercase(password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not check_lowercase(password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not check_number(password):
        feedback.append("Password should contain at least one number.")
    if not check_special_characters(password):
        feedback.append("Password should contain at least one special character.")
    
    return feedback

# Simplified scoring system for password strength
def password_checker(password):
    # Immediate check for empty or space-only passwords
    if not password or password.isspace():
        return "Very Weak"

    # Points for different criteria
    length_points = 1 if check_length(password) else 0
    uppercase_points = 1 if check_uppercase(password) else 0
    lowercase_points = 1 if check_lowercase(password) else 0
    number_points = 1 if check_number(password) else 0
    special_characters_points = 1 if check_special_characters(password) else 0

    # Calculate total points
    total_points = length_points + uppercase_points + lowercase_points + number_points + special_characters_points

    # Determine strength
    if total_points == 5:
        return "Very Strong"
    elif total_points == 4:
        return "Strong"
    elif total_points == 3:
        return "Moderate"
    elif total_points == 2:
        return "Weak"
    else:
        return "Very Weak"

# Main function to interact with the user and execute the password checker
def main():
    print("\n****** Password Complexity Checker ******")

    while True:
        password = input("\nEnter the password (or type 'exit' to quit): ")
        
        if password.lower() == 'exit':
            print("Exiting the password checker. Goodbye!\n")
            break
        
        strength = password_checker(password)
        feedback = password_feedback(password)
        
        print(f"\nStrength: {strength}")
        print("Feedback:")
        print("---------------------------------------------------------")

        if not feedback:
            print("- Password meets all requirements.")
        else:
            for message in feedback:
                print(f"- {message}")

if __name__ == "__main__":
    main()
