def check3():
    firstno = ''
    secondno = ''

    firstno = input('enter no: ')
    secondno = input('enter no: ')
    adding = int(firstno) + int(secondno)
    num = '3'

    value1 = num in firstno
    value2 = num in secondno
    value3 = num in str(adding)

    if value1==True or value2==True and value3 == True:
        return True
    else:
        return False

print(check3())