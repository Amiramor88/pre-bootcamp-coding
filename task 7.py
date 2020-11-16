def temp(num,type_of_temp):
    
    if type_of_temp == "F" or type_of_temp == "f":
        Celsius = (num - 32) * 5/9
        return Celsius
    elif type_of_temp == "C" or type_of_temp == "c":
        Farenheit = ((num * 9)/5) + 32
        return Farenheit
    else:
        return "Incorrect Values entered'"


print(temp(342,"C"))

