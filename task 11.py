word1 = input("type in a word: ")
word2 = input("type in a word: ")
for char in word1.lower():
    if char in word2.lower():
        print(char)
