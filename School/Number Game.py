import random as r

print("Let's play the number game you have to guess the numbers")
print("Easy Mode: 4 digits and tells you the place you got right")
print("Normal Mode: 4 digits and and dosen't tell you the place you got right")
print("Hard Mode: 5 digits and dosen't tells you the place you got right")
mode = input("What Mode do you want to play? Easy, Normal, Hard ").lower().title()

def easy():
    onen = r.randint(0,9)
    secn = r.randint(0,9)
    thrn = r.randint(0,9)
    foun = r.randint(0,9)
    while True:
        oneguess = int(input("Guess the first number: "))
        secguess = int(input("Guess the second number: "))
        thiguess = int(input("Guess the third number: "))
        fouguess = int(input("Guess the fourth number: "))
        if oneguess == onen:
            print("You got the first number right!")
        if secguess == secn:
            print("You got the second number right!")
        if thiguess == thrn:
            print("You got the third number right!")
        if fouguess == foun:
            print("You got the fourth number right!")
        if oneguess == onen and secguess == secn and thiguess == thrn and fouguess == foun:
            print("Well done you won!")
            break

def med():
    onen = r.randint(0,9)
    secn = r.randint(0,9)
    thrn = r.randint(0,9)
    foun = r.randint(0,9)
    re = 0
    while True:
        oneguess = int(input("Guess the first number: "))
        secguess = int(input("Guess the second number: "))
        thiguess = int(input("Guess the third number: "))
        fouguess = int(input("Guess the fourth number: "))
        if oneguess == onen:
            re += 1
        if secguess == secn:
            re += 1
        if thiguess == thrn:
            re += 1
        if fouguess == foun:
            re += 1
        print("You got {} right try again".format(re))
        if oneguess == onen and secguess == secn and thiguess == thrn and fouguess == foun:
            print("Well done you won!")
            break

def hard():
    onen = r.randint(0,9)
    secn = r.randint(0,9)
    thrn = r.randint(0,9)
    foun = r.randint(0,9)
    fivn = r.randint(0,9)
    re = 0
    while True:
        oneguess = int(input("Guess the first number: "))
        secguess = int(input("Guess the second number: "))
        thiguess = int(input("Guess the third number: "))
        fouguess = int(input("Guess the fourth number: "))
        fivguess = int(input("Guess the fifth number: "))
        if oneguess == onen:
            re += 1
        if secguess == secn:
            re += 1
        if thiguess == thrn:
            re += 1
        if fouguess == foun:
            re += 1
        if fivguess == fivn:
            re += 1
        print("You got {} right try again".format(re))
        if oneguess == onen and secguess == secn and thiguess == thrn and fouguess == foun:
            print("Well done you won!")
            break

if mode == "Easy":
    easy()  
elif mode == "Normal":
    med()
elif mode == "Hard":
    hard()