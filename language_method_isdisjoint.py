#!/usr/bin/python
""" Set method isdisjoint is used here """
NEW_SENTENCE = []
WORDS = input("Say something ").lower().split()
for word in WORDS:
    if word[0] in "aeiou":
        word = word + "yay"
        NEW_SENTENCE.append(word)
    else:
        if set('aeiou').isdisjoint(word):
            word = word + "oay"
        else:
            while word[0] not in 'aeiou':
                word = word[1:] + word[0]
            word = word + 'ay'
        NEW_SENTENCE.append(word)
print(NEW_SENTENCE)
