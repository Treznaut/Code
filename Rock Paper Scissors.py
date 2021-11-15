import random

while True:
    choice = input("Rock, Paper or Scissors ").title()
    if choice == "Rock" or choice == "Paper" or choice == "Scissors":
        break
    else:
        print("Please spell correctly")

bot_list = ["Rock", "Paper", "Scissors"]
bot_choice = random.choice(bot_list)

print("You chose {} and the enemy chose {}".format(choice, bot_choice))

if choice == bot_choice:
    print("You Tied!")
elif choice == "Rock" and bot_choice == "Paper":
    print("You Lost!")
elif choice == "Rock" and bot_choice == "Scissors":
    print("You Won!")
elif choice == "Paper" and bot_choice == "Rock":
    print("You Won!")
elif choice == "Paper" and bot_choice == "Scissors":
    print("You Lost!")
elif choice == "Scissor" and bot_choice == "Rock":
    print("You Won!")
elif choice == "Scissor" and bot_choice == "Paper":
    print("You Won!")