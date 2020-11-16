def check_vowel(word):
    vowels =""
    for char in word:
        if char in "aeiouAEIOU":
            vowels += char
    return vowels

print(check_vowel("height"))
