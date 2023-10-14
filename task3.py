import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    if length < 4:
        return "Error: Password length must be at least 4 characters."
    
    special_char = ''.join(random.choice(string.punctuation) for _ in range(1))
    num = ''.join(random.choice(string.digits) for _ in range(1))
    alpha = ''.join(random.choice(string.ascii_letters) for _ in range(2))
    remaining_length = length - 4
    
    password = special_char + num + alpha + ''.join(random.choice(characters) for _ in range(remaining_length))
    
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Error: Enter valid length.")
        else:
            password = generate_password(password_length)
            print("Generated Password:", password)
        another = input("Do you want to generate more passwords? (yes/no): ")
        if another.lower() != 'yes':
            break
    except ValueError:
        print("Error: Please enter a valid positive integer for the password length.")
