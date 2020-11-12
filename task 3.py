def checkno():
    m = ''
    e = ''
    m = int(input ('number'))
    e = int(input ('number'))

    if m == 65 or e == 65:
        return True
    elif int(m + e) == 65:
        return True
    else:
        return False

print(checkno())



