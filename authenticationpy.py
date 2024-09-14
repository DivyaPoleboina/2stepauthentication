import random
import string

def create_password():
    password = input("Create your password: ")
    
    if len(password) <= 8:
        print("Password must be longer than 8 characters.")
        return None
    
    missing_requirements = []
    
    if not any(char.islower() for char in password):
        missing_requirements.append("lowercase letter")
    
    if not any(char.isupper() for char in password):
        missing_requirements.append("uppercase letter")
    
    if not any(char.isdigit() for char in password):
        missing_requirements.append("digit")
    
    if not any(char in string.punctuation for char in password):
        missing_requirements.append("symbol")
    
    if missing_requirements:
        print("Your password is missing the following: ", ", ".join(missing_requirements))
        return None
    
    return password

def verify_password(original_password):
    max_attempts = 3  # Allow up to 3 attempts
    attempts = 0
    while attempts < max_attempts:
        entered_password = input("Please re-enter your password for verification: ")
        if entered_password == original_password:
            print("Password verified successfully!")
            return True
        else:
            print("Password verification failed. Please try again.")
        attempts += 1
    return False

def generate_captcha(length=6):
    captcha_characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choices(captcha_characters, k=length))
    return captcha

def verify_captcha():
    max_attempts = 3  # Allow up to 3 attempts
    attempts = 0
    while attempts < max_attempts:
        captcha = generate_captcha()  # Generate new CAPTCHA for each attempt
        print(f"CAPTCHA: {captcha}")
        entered_captcha = input("Enter the CAPTCHA shown: ")
        if entered_captcha == captcha:
            print("CAPTCHA verified successfully!")
            return True
        else:
            print("CAPTCHA verification failed. A new CAPTCHA is generated.")
        attempts += 1
    return False

# Example usage
password = None
while not password:
    password = create_password()

# Verify the password
if verify_password(password):
    # Generate and verify CAPTCHA
    if verify_captcha():
        print("Password setup and verification complete.")
    else:
        print("CAPTCHA verification failed after multiple attempts.")
else:
    print("Password verification failed after multiple attempts.")
