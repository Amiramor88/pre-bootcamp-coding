def area_of_triangle(a,b,c):

    import math

    s = (a + b + c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    return area
print(area_of_triangle(14,11,16))
