def maximum(numbers):

    maxi = 0
    for item in numbers:
        if int(item) > maxi:
            maxi = int(item)
    return maxi
