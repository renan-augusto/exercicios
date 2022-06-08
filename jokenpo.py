rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

possibleChoices = [rock, paper, scissors]

userChoice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")
userChoiceStorage = 0

if userChoice == "0":
    userChoiceStorage = possibleChoices[0]
    print(f"Your choice is: {possibleChoices[0]}")
elif userChoice == "1":
    userChoiceStorage = possibleChoices[1]
    print(f"Your choice is: {possibleChoices[1]}")
elif userChoice == "2":
    userChoiceStorage = possibleChoices[2]
    print(f"Your choice is: {possibleChoices[2]}")
else:
    print("Error")

computerChoice = random.choice(possibleChoices)
print(f"The computer chooses: {computerChoice}")

if userChoiceStorage == possibleChoices[0] and computerChoice == rock:
    print("That´s a tie game/Empatou")
elif userChoiceStorage == possibleChoices[0] and computerChoice == paper:
    print("You lose!/Você perdeu!")
elif userChoiceStorage == possibleChoices[0] and computerChoice == scissors:
    print("You win!/Você Ganhou!")

if userChoiceStorage == possibleChoices[1] and computerChoice == rock:
    print("You win!/Você ganhou!")
elif userChoiceStorage == possibleChoices[1] and computerChoice == paper:
    print("That´s tie./Empate.")
elif userChoiceStorage == possibleChoices[1] and computerChoice == scissors:
    print("You lose!/Você perdeu!")

if userChoiceStorage == possibleChoices[2] and computerChoice == rock:
    print("You lose!/Você perdeu!")
elif userChoiceStorage == possibleChoices[2] and computerChoice == paper:
    print("You win!./Você ganhou!.")
elif userChoiceStorage == possibleChoices[2] and computerChoice == scissors:
    print("That´s a tie!/Empate.")
