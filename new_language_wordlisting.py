#!/usr/bin/python
""" This will careate a funny langauge """

WORDS = input("Say something ").lower().split()
NEW_WORD_LIST = []
WORD_LIST = []
for word in WORDS:
    if word[0] in "aeiou":
        word = word + "yay"
        NEW_WORD_LIST.append(word)
    else:
        while word[0] not in "aeiou":
            if len(word) < 2:
                print(f"{word} is not an English word adding o to {word}")
            word = word + 'o'
            word = word[1:]+word[0]
        word = word+"ay"
        WORD_LIST.append(word)
print(NEW_WORD_LIST, WORD_LIST, "from ", WORDS)
