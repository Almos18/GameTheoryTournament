import random

class Tournament:

    #def __init__(self):
    #self.run_tournament

    def run_tournament(self):
        x = 2
        for y in range(10):
            x = self.tit_for_tat(x)
            p1 = x
            x = self.random_answer()
            p2 = x
            print(p1, p2)


    def tit_for_tat(self, x):

        if x == 0:
            return 0

        if x == 1:
            return 1

        if x == 2:
            return 1


    def random_answer(self):
        return random.randint(0, 1)


try1 = Tournament()

try1.run_tournament()