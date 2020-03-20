knt = 0
vvl = 0
string = input("Say something ")
for x in string:
    if x.lower() in "aieou":
        knt = knt + 1
    elif x == " ":
        pass
    else:
        vvl = vvl + 1
print(f"There are {vvl} vowels and {knt} consonants in {string} ")
