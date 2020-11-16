def checkno(x,y):

    if x == 65 or y == 65:
        return True
    elif int(x + y) == 65:
        return True
    else:
        return False

print(checkno(15,50))



