import random
import string

def generate_password(length):
    # Define characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the length is at least 6 characters
    if length < 6:
        print("Password length must be at least 6 characters.")
        return

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
