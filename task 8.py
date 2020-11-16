def convert(time):
    
    
    hours = time // 60

    minutes = time % 60
    
    if hours == 1:
        return (str(hours) + " hour, " + str(minutes) + " minutes")
    elif minutes == 1:
        return (str(hours) + " hours, " + str(minutes) + " minute")
    elif hours == 1 and minutes == 1:
        return (str(hours) + " hour, " + str(minutes) + " minute")
    else:
        return ( str(hours) + " hours, " + str(minutes) + " minutes")

print(convert(167))
