def temp():
    temptype = input("Please enter 'C' for celius and 'F' for farenheit: ")
    tempno = int(input("What's the temperature?"))

    if temptype == "F" or temptype == "f":
        Celsius = (tempno - 32) * 5/9
        return Celsius
    elif temptype == "C" or temptype == "c":
        Farenheit = ((tempno * 9)/5) + 32
        return Farenheit
    else:
        return "Please stop playing and enter 'F' or 'C'"


print(temp())

