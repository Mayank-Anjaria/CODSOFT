#Task 4 Rock,Paper and Scissors Game

import random

def users_choice():
    while True:
        print("\nChoose 1 for rock (🪨)")
        print("\nChoose 2 for paper (📄)")
        print("\nChoose 3 for scissors (✂️)")
        user_choice = input("\nEnter your choice : ")
        if user_choice in ["1", "2", "3"]:
            return user_choice
        else:
            print("\nInvalid choice. Please choose 1 for rock, 2 for paper, or 3 for scissors.")

def computers_choice():
    return random.choice(["1", "2", "3"])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "\nIt's a tie!"
    elif (user_choice == "1" and computer_choice == "3") or \
         (user_choice == "3" and computer_choice == "2") or \
         (user_choice == "2" and computer_choice == "1"):
        return "\nYou win!"
    else:
        return "\nYou lose!"

def play():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = users_choice()
        computer_choice = computers_choice()
        print(f"\nYour choice : {'🪨' if user_choice == '1' else '📄' if user_choice == '2' else '✂️'}")
        print(f"\nComputer's choice : {'🪨' if computer_choice == '1' else '📄' if computer_choice == '2' else '✂️'}")
        result = winner(user_choice, computer_choice)
        print(result)
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1
        print(f"\nScore - You : {user_score}, Computer : {computer_score}")
        play_again = input("\nDo you want to play again? (y/n) : ")
        if play_again.lower() != "y":
            break

print("\nWelcome to Rock-Paper-Scissors!")

play()

print("\nThanks for playing!\n")