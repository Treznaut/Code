while True: #While True loop runs forever
    unit = input("What unit do you want to use? (Celsius/Farhenheit/Kelvin) ").lower() #asks for user input and puts it in lower case
    if unit == "celsius" or unit == "farhenheit" or unit == "kelvin": #checks what unit they use
        break  
    else:
        print("Invalid unit")

num = float(input("What is the temperature? "))

if unit == "celsius":
    celsius = num
    farhenheit = num * 1.8 + 32
    kelvin = num + 273.15
    print(f"Celsius: {celsius}")
    print(f"Farhenheit: {farhenheit}")
    print(f"Kelvin: {kelvin}")

if unit == "farhenheit":
    farhenheit = num
    celsius = (num - 32) * 0.55
    kelvin = (num - 32) * 0.55 + 273.15
    print(f"Celsius: {celsius}")
    print(f"Farhenheit: {farhenheit}")
    print(f"Kelvin: {kelvin}")
    
if unit == "kelvin":
    kelvin = num
    farhenheit = (num - 273.15) * 1.8 + 32
    celsius = num - 273.15 
    print(f"Celsius: {celsius}")
    print(f"Farhenheit: {farhenheit}")
    print(f"Kelvin: {kelvin}")
    