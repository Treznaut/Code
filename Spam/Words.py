import random as r
from time import sleep as s
import pyautogui as pg

constanants =  ["b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]
word = ""

length = r.randint(4,10)

if length <= 6:
    vowel_no = r.randint(1,3)
elif length <= 8 and length > 6:
    vowel_no = r.randint(3,5)
else:
    vowel_no = r.randint(5,6)

for i in range(length):
    word += r.choice(constanants)

print(word)