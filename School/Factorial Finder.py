#User chooses number they want the factorial of
num = int(input("Choose the number "))

#Creates variables for later
factorial = 1
numl = []

#Appends all the numbers that come before the number the user chose
for i in range(num - 1):
    numl.append(num)
    num -= 1

#Makes the factorial variable times by the
#number you chose and all the numbers that come before it
for i in numl:
    factorial *= i

print(factorial)