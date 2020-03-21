#!/usr/bin/python
""" Just count all the vowels and consonants """


def fun(string):
    """ something is missing. I can't get correct number of consonants in output
    I saw this game/trick in a video lecture in Python Bible, good series and modified
    it to make it a function so that it can be called again and again."""
    # string = input(" Say something ")
    vowels = 0 
    consonants = 0 
    for letter in string:
        if letter.lower() in "aeiou":
            vowels += 1
        elif letter == " ":
            pass
        else:
            consonants += consonants
    print(f"There are {vowels} vowels and {consonants} consonants in\
' {string} '")


fun(input("Say something ")) # I.C now
