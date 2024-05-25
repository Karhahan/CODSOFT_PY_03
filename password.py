import random
import string

class PasswordGenerator:
    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password


# Example usage:
password_generator = PasswordGenerator()

while True:
    length = int(input("Enter the length of the password (or press Enter for default length of 12): ") or 12)
    
    if length <= 0:
        print("Invalid length. Please enter a positive integer.")
    else:
        password = password_generator.generate_password(length)
        print("Generated Password:", password)
        
        again = input("Generate another password? (yes/no): ").lower()
        if again != "yes":
            print("Exiting the program.")
            break
