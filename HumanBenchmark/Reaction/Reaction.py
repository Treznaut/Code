import pyautogui as pg
from time import sleep as s

while True:
    try:
        pg.click('HumanBenchmark/Reaction/Green.png')
        s(1)
        pg.click()
    except:
        print("Not Yet")