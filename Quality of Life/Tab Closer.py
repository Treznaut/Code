import pyautogui as pag
from time import sleep

tabs = 0

stop = int(input("How many tabs before it asks you to stop? "))

print("Use this to count how many tabs you had open")

sleep(3)


while True:
    for i in range(stop):
        pag.keyDown("ctrl")
        pag.keyDown("w")
        pag.keyUp("ctrl")
        pag.keyUp("w")
        tabs += 1
    print(f"You have closed {tabs} tabs")
    while True:
        stop1 = input("Would you like to stop? y/n ").lower()
        if stop1 == "y":
            print("You have succesfully stopped!")
            break
        elif stop1 == "n":
            print("The tab closing will continue!")
            sleep(3)
            break
        else:
            print("Please use correct formating! \'y\' for carry on and \'n\' for stop")
    if stop1 == "y":
        break        

