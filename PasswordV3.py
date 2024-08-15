def validPassword(password):
    # Initialize counters for different character types
    upper = lower = digit = special_char = 0
    
    # Check if the password length is at least 8 characters
    if len(password) >= 8:
        # Iterate through each character in the password
        for char in password:
            # Check if the character is an uppercase letter
            if char.isupper():
                upper += 1
            # Check if the character is a lowercase letter
            elif char.islower():
                lower += 1
            # Check if the character is a digit
            elif char.isdigit():
                digit += 1
            # Check if the character is a special character (not alphanumeric and not a space)
            elif not char.isalnum() and not char.isspace():
                special_char += 1
        
        # Check if the password contains at least one of each required character type
        if upper >= 1 and lower >= 1 and digit >= 1 and special_char >= 1:
            print("Strong Password and Valid")
        else:
            print("Invalid Password")
    else:
        print("Password Length Too Short, Password Length Must Be 8.")

def main():
    # Get user input for the password
    user_password = input("Enter your password: ")
    # Validate the entered password
    validPassword(user_password)

# Run the main function
if __name__ == "__main__":
    main()
