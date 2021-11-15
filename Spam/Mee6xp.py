import pyautogui as p
from time import sleep as s

s(3)

while True:
    p.write("Dave has recently started balding")
    p.keyDown("enter")
    p.keyUp("enter")
    s(60)