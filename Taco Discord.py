import pyautogui, time

time.sleep(3)

while True:
    pyautogui.write("!w")
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(2)
    pyautogui.write("!tip")
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(300)
    pyautogui.write("!tip")
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(300)