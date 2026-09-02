import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
tie_score = 0

print("===== ROCK PAPER SCISSORS =====")

while True:
    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice: ").lower()

    if user_choice == "1":
        user_choice = "rock"
    elif user_choice == "2":
        user_choice = "paper"
    elif user_choice == "3":
        user_choice = "scissors"
    elif user_choice in choices:
        pass
    else:
        print("Invalid choice.")
        continue

    computer_choice = random.choice(choices)

    print("\nYour choice:", user_choice)
    print("Computer choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: Tie!")
        tie_score += 1

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\n===== SCORE =====")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)
    print("Ties:", tie_score)

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("\nThanks for playing!")
        break
