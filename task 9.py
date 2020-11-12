
def summation():
    sumof = 0
    for num in range(0,1000):
        if (num % 3 ==0) or (num % 5 ==0):
            sumof+=num

    return sumof

print (summation())