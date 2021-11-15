import pyautogui
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pyautogui.locateOnScreen("C:/Users/IamTr/OneDrive/Desktop/Python Projects/Quality of Life/WhatsApp Auto Reply/Clipboard.png", confidence = .6)
x = position1[0]
y = position1[1]

def get_message():
    global x, y

    position = pyautogui.locateOnScreen("C:/Users/IamTr/OneDrive/Desktop/Python Projects/Quality of Life/WhatsApp Auto Reply/Clipboard.png", confidence = .6)
    x = position[0]
    y = position[1]
    pyautogui.moveTo(x, y)
    pyautogui.moveTo(x + 70, y - 45)
    pyautogui.tripleClick()
    pyautogui.rightClick()
    pyautogui.moveRel(12, 15)
    pyautogui.click()
    whatsapp_message = pyperclip.paste()
    pyautogui.click()
    print("Message recieved: " + whatsapp_message)

    return whatsapp_message

def post_response(message):
    global x, y

    position = pyautogui.locateOnScreen("C:/Users/IamTr/OneDrive/Desktop/Python Projects/Quality of Life/WhatsApp Auto Reply/Clipboard.png")
    x = position[0]
    y = position[1]
    pyautogui.moveTo(x + 200, y + 20)
    pyautogui.click()
    pyautogui.typewrite(message, interval=0.01)

    pyautogui.typewrite("\n", interval=0.1)

def proccess_response(message):
    random_no = random.randint(0, 3)

    if "?" in str(message).lower():
        return "I'm A bot soo i dont know"

    else:
        if random_no == 0:
            return "Alright - Bot Response"
        elif random_no == 1:
            return "Cool - Bot Response"
        elif random_no == 2:
            return "Nice - Bot Response"
        elif random_no == 3:
            return "Okie Dokie - Bot Response"

def check_for_new_messages():
    pyautogui.moveTo(x + 50, y - 35)

    while True:
        try:
            position = pyautogui.locateOnScreen("C:/Users/IamTr/OneDrive/Desktop/Python Projects/Quality of Life/WhatsApp Auto Reply/Unread.png", confidence=.7)
            if position is not None:
                pyautogui.moveTo(position)
                pyautogui.moveRel(-100, 0)
                pyautogui.click()
                sleep(.5)
        except(Exception):
            print("No new other users with new messages located")
        if pyautogui.pixelMatchesColor(int(x + 50), int(y - 35), (38, 45, 49), tolerance=10):
            print("is_dark")
            processed_message = proccess_response(get_message())
            post_response(processed_message)
        else:
            print("No new messages yet...")
        sleep(5)

check_for_new_messages()
