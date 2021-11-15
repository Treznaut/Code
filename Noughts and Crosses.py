import random as r

def no_bot():
    line1 = ["-", "-", "-"] 
    line2 = ["-", "-", "-"]
    line3 = ["-", "-", "-"]
def yes_bot():
    line1 = ["-", "-", "-"] 
    line2 = ["-", "-", "-"]
    line3 = ["-", "-", "-"]

while True:
    bot = input("Wanna play against a bot? y/n ").strip().lower()
    if bot == "y":
        print("You are playing with a bot")
        break
    elif bot == "n":
        print("You are not playing with a bot")
        break
    else:
        print("Please use correct formatting!")


