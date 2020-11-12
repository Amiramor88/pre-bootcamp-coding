m = ''
e = ''
m = int(input ('number'))
e = int(input ('number'))

if m == 65 or e == 65:
    print("True")
elif int(m + e) == 65:
    print("True")
else:
    print("False")