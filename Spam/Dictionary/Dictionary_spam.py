import pyautogui
import time
time.sleep(5)
f  = open("Python/Spam/Dictionary/Oxford.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    
    