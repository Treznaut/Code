import pyautogui as pg
from time import sleep as s

#pyautogui.drag(30, 0, 2, button='left')  drag the mouse left 30 pixels over 2 seconds while holding down the left mouse button
#Point(x=10, y=78) (244, 244, 244)
#Point(x=1890, y=1058) (255, 255, 255)

s(5)

x_start = 10
y_start = 78

x_end = 1890
y_end = 1058

dif_x = 1880
dif_y = 980

move = 1

pg.moveTo(x_start, y_start)

s(1)

pg.mouseDown()
pg.drag(dif_x, move, 1, button='left')
pg.mouseUp()
