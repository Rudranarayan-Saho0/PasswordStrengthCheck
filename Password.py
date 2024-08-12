# A Simple Python Program to Check the Strength of a Password
print("Let's Check Your Password Strong Or Not!")  # Prompt the user to check their password strength
#Creiteria For a Strong Password
print("Creiteria For a Strong Password:\n 1. uppercase letters\n 2. lowercase letters\n 3. digits\n 4. special characters\n 5. Minimum Length 8")
password = input("Enter Your Password: ")  # Input the password from the user
has_Upper = False  # Flag to check for uppercase letters
has_Lower = False  # Flag to check for lowercase letters
has_Digit = False  # Flag to check for digits
has_Special = False  # Flag to check for special characters

special_Characters = '!@#$%^&*()_+-'  # List of special characters to check against

# Loop through each character in the password
for char in password:
    if char.isupper():  # Check if the character is an uppercase letter
        has_Upper = True
    elif char.islower():  # Check if the character is a lowercase letter
        has_Lower = True
    elif char.isdigit():  # Check if the character is a digit
        has_Digit = True
    elif char in special_Characters:  # Check if the character is a special character
        has_Special = True

# Determine if the password is strong based on the flags
if has_Upper and has_Lower and has_Digit and has_Special:
    print("your Password is Strong")  # Print if the password is strong
else:
    print("Your Password Is Weak, Set A Strong Password ")  # Print if the password is weak

