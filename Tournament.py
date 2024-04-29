import random

class Tournament:


    #def __init__(self):
    #self.run_tournament

    def run_tournament(self):
        x = 2

        amount_of_rounds = 10
        for y in range(amount_of_rounds):
            x = self.tit_for_tat(x)
            p1 = x
            x = self.random_answer()
            p2 = x
            print(p1, p2)

            self.calculate_points(p1, p2)


    def calculate_points(self, p1, p2):
            global p1points
            global p2points

            if p1 == 0 & p2 == 0:
                p1points += 1
                p2points += 1

            if p1 == 1 & p2 == 0:
                p1points += 0
                p2points += 10

            if p1 == 0 & p2 == 1:
                p1points += 10
                p2points += 0

            if p1 == 1 & p2 == 1:
                p1points += 3
                p2points += 3




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