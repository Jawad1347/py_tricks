#!/usr/bin/python
""" I am lazy and I can't be bothered with unit testing and I know user may input things that may break this program\
But my main purpuse was only to wrtie an algorithm that can check if a number is AS or not.
"""


A = input("your number ")
B = [int(x)**3 for x in A]
C = 0
for i in B:
    C = C+i
if C == int(A):
    print("number is strong")
else:
    print("it is not strong number")
