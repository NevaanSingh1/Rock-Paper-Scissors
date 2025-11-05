import random

options = ['Rock', 'Paper', 'Scissors']
choice = random.choice(options)
user_input = input("Choose Rock, Paper, or Scissors, write the first letter in capitals: ")
print("Random choice:", choice)

if user_input == choice:
    print("It's a tie!")
elif user_input == "Rock" and choice == "Scissors":
    print("You win!")
elif user_input == "Scissors" and choice == "Rock":
    print("You lose!")
elif user_input == "Paper" and choice == "Rock":
    print("You win!")
elif user_input == "Rock" and choice == "Paper":
    print("You lose!")
elif user_input == "Scissors" and choice == "Paper":
    print("You win!")
elif user_input == "Paper" and choice == "Scissors":
    print("You lose!")
