numbers = []

n = int(input("How many numbers will you enter: "))

for i in range (0,n):
    newnum = int(input('enter a number:'))
    numbers.append(newnum)

maxi = 0
for item in numbers:
    if item > maxi:
        maxi = item

print(maxi)