
import re

def is_valid_password(password):
    """
    Checks if a password meets the specified validation criteria.

    Criteria:
    - At least 1 lowercase letter [a-z]
    - At least 1 uppercase letter [A-Z]
    - At least 1 number [0-9]
    - At least 1 character from [$#@]
    - Minimum length of 6 characters
    - Maximum length of 16 characters

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    
    # Check the length of the password
    if len(password) < 6 or len(password) > 16:
        print("Password must be between 6 and 16 characters long.")
        return False

    # Check for at least one lowercase letter
    if not re.search("[a-z]", password):
        print("Password must contain at least one lowercase letter.")
        return False

    # Check for at least one uppercase letter
    if not re.search("[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return False

    # Check for at least one number
    if not re.search("[0-9]", password):
        print("Password must contain at least one number.")
        return False

    # Check for at least one special character
    if not re.search("[$#@]", password):
        print("Password must contain at least one of the following special characters: $, #, or @.")
        return False
        
    return True

# --- Main program loop ---
if __name__ == "__main__":
    while True:
        user_password = input("Enter a password to validate: ")
        
        if is_valid_password(user_password):
            print("Password is valid! ✅")
            break
        else:
            print("Password is not valid. Please try again. ❌")
            print("-" * 30)