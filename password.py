import random
import string

def password_generate(length, complexity):
    if complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "low":
        characters = string.ascii_letters
    else:
        print("Invalid input. Please enter a proper complexity level (high, medium, low)")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Generate your own password !")
    print('\n')
    
    while True:
        try:
            length = int(input("Enter the password length: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    while True:
        complexity = input("Enter the complexity of your password (high, medium, low): ").lower()
        if complexity in ["high", "medium", "low"]:
            break
        else:
            print("Invalid input. Please enter a proper complexity level.")
    
    password = password_generate(length, complexity)
    
    if password:
        print("Password Generated:", password)

if __name__ == "__main__":
    main()
