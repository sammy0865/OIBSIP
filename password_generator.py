import random
import string


def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


while True:
    print("\n=== Random Password Generator ===")

    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        print("\nChoose character types:")
        print("1. Letters")
        print("2. Numbers")
        print("3. Symbols")

        choices = input("Enter your choices (example: 123): ")

        use_letters = "1" in choices
        use_numbers = "2" in choices
        use_symbols = "3" in choices

        if sum([use_letters, use_numbers, use_symbols]) < 2:
            print("Please select at least 2 character types.")
            continue

        password = generate_password(
            length,
            use_letters,
            use_numbers,
            use_symbols
        )

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != "y":
            print("Thank you for using the Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")