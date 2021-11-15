import random as r
structures = ["101", "1001", "010"]
# 1 - constonant
# 0 - vowel
word = ""

constanants =  ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

structure = structures[0]


for j in structure:
    if j == "1":
        letter = r.choice(constanants)
    else:
        letter = r.choice(vowels)
    word += letter

print(word)