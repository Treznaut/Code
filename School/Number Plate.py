import re

#Input for the number plate they want to check
num_plate = input("Input the number plate ")

#Uses re to check if the number plate submitted against a pattern
matched = re.match("[a-z][0-9][a-z][0-9]+", num_plate)
#Uses boolean to show if the input matches the pattern
is_match = bool(matched)
print(is_match)