import pyautogui as pag
from time import sleep

sleep(3)

while True:
    pag.keyDown("ctrl")
    pag.keyDown("t")
    pag.keyUp("ctrl")
    pag.keyUp("t")
