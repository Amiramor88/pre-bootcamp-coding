def AreaTri():
    a = ''
    b = ''
    c = ''

    a = int(input('enter a number:'))
    b = int(input('enter a number:'))
    c = int(input('enter a number:'))

    import math

    s = (a + b + c)/2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    return Area
print(AreaTri())