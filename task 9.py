
def summation(sum):
    sum_of_numbers = 0
    for num in range(0,1000):
        if (num % 3 ==0) or (num % 5 ==0):
            sum_of_numbers +=num

    return sum_of_numbers

print (summation(sum))
