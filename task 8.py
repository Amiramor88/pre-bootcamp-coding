def convert():
    time =""

    time = int(input("how much time in minutes?"))

    hours = time // 60

    minutes = time % 60

    return ( str(hours) + " hours, " + str(minutes) + " minutes")

print(convert())