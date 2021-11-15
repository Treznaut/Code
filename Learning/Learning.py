var1 = 1 #Interger
var2 = "text" #String
var3 = 0.1 #Float
var4 = True #Boolean

list1 = [1, "text", 0.1, True]

var5 = list1[1]

list1.append("truck")
list1[0] = list1[0] + 3

#Types of bracket
#[] To find things within dictionaries, tuples and lists. Defines lists
#() To call functions (like print, int, and input) they take parameters. Defines Tuples
#{} Defines dictionaries and can do .format()

#Tuples  can't be mutated
coords = (6, 9)

#Function
def function(value1, value2):
    global var1 #Allows the use of this variable in the function
    print(str(value1))
    return value2-5

d = function("hello", 10)
print(str(d))

#Dictionaries stores keys and values
a = {
    "number": 10,
    "letter": "g",
    "sub": {"number2": 12, "letter2": "h"},
}

#Loops Loops Loops Loops Loops
#Types of Loop
#While loops, Only runs if a condition is met and runs again if a condition is still met
#For Loops, Is origanally definite

while True:
    print("Hi")
    while True:
        print("Hi2:ElectricBoogaloo")
        break

for i in range(5):
    print("Hi")
