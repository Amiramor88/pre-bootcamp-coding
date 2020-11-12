def checkv():
    sent = input("type a sentence: ")
    vowels =""
    for char in sent:
        if char in "aeiouAEIOU":
            vowels += char
    return vowels

print(checkv())
