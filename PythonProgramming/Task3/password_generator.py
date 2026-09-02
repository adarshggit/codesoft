import random
import string

print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length must be at least 4.")
            continue

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

        choice = input("\nGenerate another password? (yes/no): ").lower()

        if choice != "yes":
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")
