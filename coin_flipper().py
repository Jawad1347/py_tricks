import random


class Pound:
    """ This will print some coins """
    def __init__(self, rare=False):
        self.rare = rare
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5  # mm
        self.thickness = 3.13  # mm
        self.heads = True

    def __del__(self):
        print("Coin Spent")

    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):
        return random.choice([True, False])

    def flip2(self):
        choice = random.choice([True, False])
        self.heads = choice


coin1 = Pound()
print(coin1.colour)
coin1.rust()
print(coin1.colour)
coin1.clean()
print(coin1.colour)
print(coin1.heads)
# for i in range(10):
#     coin1.flip2()
#     if coin1.heads:
#         print("Head")
#     else:
#         print("Tail")

m = [coin1.flip() for x in range(100)]
print(m)
print(m.count(True), m.count(False))
