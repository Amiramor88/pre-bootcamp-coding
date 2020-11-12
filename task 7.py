temptype = input("Please enter 'C' for celius and 'F' for farenheit: ")
tempno = int(input("What's the temperature?"))

if temptype == "F" or temptype == "f":
    Celsius = (tempno - 32) * 5/9
    print(Celsius)
elif temptype == "C" or temptype == "c":
    Farenheit = ((tempno * 9)/5) + 32
    print(Farenheit)
else:
    print("Please stop playing and enter 'F' or 'C'")

