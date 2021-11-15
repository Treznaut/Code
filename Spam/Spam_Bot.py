import pyautogui
import time
stop = "no"
word = pyautogui.prompt(text='What do you want to spam?', title='Spam')
print("You are gonna spam {}. Spamming in:".format(word))
print(5)
time.sleep(1)
print(4)
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("Go!")
while stop == "no":
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    
    pyautogui.press("enter")
    time.sleep(0.2)
