import pyautogui as pg
from time import sleep as s

s(3)

for i in range(31):
    try:
       target = pg.locateOnScreen('HumanBenchmark/Aim/Target.png', confidence=0.7)
       pg.moveTo(target)
       pg.click()
    except:
        print("Not yet")