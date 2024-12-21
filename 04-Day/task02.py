import random

# Game Rock, Paper or Scissors

game_images = ["Rock", "Paper", "Sissors"]

user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Sissors: "))
if user_choise >=0 and user_choise <=2:
    print("You chose:")
    print(game_images[user_choise])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choise >= 3 or user_choise <0:
    print("You typed an invalid number. You lose!")
elif user_choise == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choise == 2:
    print("You lose")
elif computer_choice > user_choise:
    print("You lose!")
elif user_choise > computer_choice:
    print("You win!")
elif computer_choice == user_choise:
    print("It's draw")
