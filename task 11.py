def checkcom():
    word1 = input("type in a word: ")
    word2 = input("type in a word: ")
    common = ""
    for char in word1.lower():
        if char in word2.lower():
            common +=char
    return common

print(checkcom())
