def check_common(word1,word2):
   
    common = ""
    for char in word1.lower():
        if char in word2.lower():
            common +=char
    return common

print(check_common("house","computer"))
