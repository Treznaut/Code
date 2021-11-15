import random as r

symbols = ["🍒", "🍍", "🍓", "⭐", "🔔", "💀"]

money = 100
cost = 20

while True:
    money -= cost
    slot1 = r.choice(symbols)
    slot2 = r.choice(symbols)
    slot3 = r.choice(symbols)

    slots = []
    slots.append(slot1)
    slots.append(slot2)
    slots.append(slot3)

    print("||||||||||||||||")
    print("|||{}||{}||{}|||".format(slot1, slot2, slot3))
    print("||||||||||||||||")
    
    if  slot1 == "💀" and slot2 == "💀" and slot3 == "💀":
        print("You got 3 skulls you lose all your money!")
        money -= money
    if slot1 == "💀" and slot2 == "💀":
        print("You got 2 skulls you lose £1!")
        money -= 100
    if slot1 == "💀" and slot3 == "💀":
        print("You got 2 skulls you lose £1!")
        money -= 100
    if slot2 == "💀" and slot3 == "💀":
        print("You got 2 skulls you lose £1!")
        money -= 100
    if  slot1 == "🔔" and slot2 == "🔔" and slot3 == "🔔":
        print("You got 3 bells you get £5!")
        money += 500
    if slots[0] == slots[1] and slots[0] == slots[2] and slots[1] == slots[2]:
        print("You got all 3 the same you win £1!")
        money += 100 
    if slots[0] == slots[1] or slots[0] == slots[2] or slots[1] == slots[2]:
        print("You got 2 the same you win 50p!")
        money += 50
    if slots[0] != slots[1] and slots[0] != slots[2] and slots[1] != slots[2]:
        print("You got none the same you win nothing!")

    print(f"You have {money}p")

    while True:
        again = input("Want to go again? (y/n) ")
        if again == "y":
            break
        if again == "n":
            break
    if again == "n":
            break