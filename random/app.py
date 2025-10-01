import random


class Dice:
    def roll(self):
        a = random.randint(1,10)
        b = random.randint(1,10)
        return (a,b)


ob = Dice()
print(ob.roll())
