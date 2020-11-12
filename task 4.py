firstno = ''
secondno = ''

firstno = input('enter no: ')
secondno = input('enter no: ')
adding = int(firstno) + int(secondno)
num = '3'

value1 = num in firstno
value2 = num in str(adding)

if value1==True and value2 == True:
    print("TRUE")
else:
    print ("FALSE")