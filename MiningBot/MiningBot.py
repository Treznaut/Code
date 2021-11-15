#Eve Online Mining Bot By Tom
#If your reading this subscribe to Treznaut and solvingOverload on YouTube
#Imports pytesseract, pyautogui and sleep
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyautogui as pg
from time import sleep as s

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print("Tom's Eve Online Mining Bot \n    Starts in 5 seconds")

s(5)

undockMovement = 15

#Undocks and Goes to asteroid belt
def undock():
    #Checks if user is in the station
    global undockMovement
    try:
        undockb = pg.locateOnScreen('Undock.png', confidence=0.9)
        pg.moveTo(undockb)
        s(0.1)
        pg.click()
        s(15)
    except:
        print("User is not in a Station")
    #Goes to Asteroid belt
    miningt = pg.locateOnScreen('MiningTab.png', confidence=0.8)
    pg.moveTo(miningt)
    s(0.1)
    pg.click()
    s(1)
    typet = pg.locateOnScreen('Type.png', confidence=0.7)
    pg.moveTo(typet)
    s(0.1)
    pg.click()
    s(1)
    pg.move(0,undockMovement)
    pg.rightClick()
    pg.move(0,5)
    pg.click()
    #Sleeps So the ship can get to the Asteroid Field
    s(60)
    

#Docks User at Station 
def dock():
    print("Dock")

#Puts Ore in Item Hangar
def item_hangar():
    print("Item Hangar")

#Checks for Asteroids
def check():
    try:
        asteroid = pg.locateOnScreen('Asteroid.png', confidence=0.9)
    except:
        print("Asteroid Belt depleted")
        undockMovement += 15
        undock()

#Checks if Ore hold is full
def full():
    print("Full") 

#Completes the mining Process      
def mining():
    #undock()
    #check()
    asteroid = pg.locateOnScreen('Asteroid.png', confidence=0.6)
    s(0.1)
    pg.moveTo(asteroid)
    s(0.1)
    pg.rightClick()
    s(0.1)
    lock = pg.locateOnScreen('Lock.png', confidence=0.9)
    s(0.1)
    pg.moveTo(lock)
    s(0.1)
    pg.click()
    s(0.1)
    pg.press("q")
    s(10)
    pg.press("f1")
    s(0.1)
    pg.press("f2")
    s(0.1)
    pg.press("f3")
    s(0.1)
    pg.press("f4")
    s(0.1)
    pg.press("f5")
    #s(0.1)
    #pg.hotkey("shift", "f")

mining()
 