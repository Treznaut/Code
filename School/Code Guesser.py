from random import randint as r

length = int(input("How long is the code? "))

maxi = 9 
big = 9
guess = "0000"
zeros = 0
part = ""

for i in range(length - 1):
    big *= 10
    maxi += big

while True:
    zeros = 0
    part = ""
    if len(guess) != length:
        zeros = length - len(guess)
        for i in range(zeros):
            part = part + "0"
            final = part + guess
            guess = final
    print(guess)
    guess = int(guess)
    if guess >= maxi:
        break
    guess += 1
    guess = str(guess)


