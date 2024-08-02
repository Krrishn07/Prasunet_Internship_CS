# 🎯Prasunet_CS_03
# 🎯Password Complexity Checker

## Overview
This project focuses on developing a tool that assesses the complexity of passwords, ensuring they meet security standards. By analyzing various parameters such as length, character variety, and common patterns, this project aims to help users create strong and secure passwords.

## What I Learned
- **Password Security Principles**: Understanding the factors that contribute to a secure password and how to evaluate them.
- **Regular Expressions**: Utilizing regex for pattern matching to analyze password components effectively.
- **Algorithm Development**: Creating a robust algorithm to score password complexity based on defined security criteria.

## Project Highlights
- **Complexity Analysis**: Developed a tool that checks password strength by evaluating multiple security factors such as length, use of 
 uppercase and lowercase letters, numbers, and special characters.
- **Regex Implementation**:  Implemented regular expressions to identify weak patterns and enforce best practices in password creation.
- **User-Friendly Interface**: Designed a user interface for easy input of passwords and clear feedback on their complexity level.
  
## Fun Fact
🔒 Strong passwords are often the first line of defense against unauthorized access. An effective password complexity checker can help users stay secure in the digital world by promoting good password hygiene.

## Usage

### Prerequisites
- Python 3.x
- Regex library (`pip install re`)

### Steps
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your_username/Prasunet_Internship_CS.git
    ```
2. **Navigate to the Directory**:
    ```sh
    cd Prasunet_CS_03
    ```
3. **Run the Script**:
    ```sh
    python Password_Complexity_Checker.py
    ```
4. **Assign Image and Apply Encryption/Decryption**:
    Follow the on-screen instructions to input a password and receive feedback on its strength.

### Example
```python
# Checking password complexity
Input:  "Password123!"
Output: "Strong Password: Your password includes uppercase, lowercase, numbers, and special characters. Length: 11."

Input:  "weakpass"
Output: "Weak Password: Your password is too short and lacks numbers or special characters. Consider using a mix of character types for better security."
