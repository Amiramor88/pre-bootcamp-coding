def check_for_no_3(x,y):
    
    add_x_y = int(x) + int(y)
    num = '3'

    value3 = num in str(add_x_y)

    if (x = 3 or y =3) and value3:
        return True
    else:
        return False

print(check3_for_no_3(3,60))
