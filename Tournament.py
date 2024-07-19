import random

class Tournament:
    p1points = 0
    p2points = 0

    # def __init__(self):
    # self.run_tournament
    def run_tournament(self):
        x = 2
        amount_of_rounds = 10
        for y in range(amount_of_rounds):
            x = self.tit_for_tat(x)
            x = self.potentially_mutate(x)
            player1 = x
            x = self.scout(y)
            x = self.potentially_mutate(x)
            player2 = x

            print(player1, player2)

            self.calculate_points(player1, player2)
            #print(self.p1points, self.p2points)

        print(self.p1points, self.p2points)
        self.write_to_file(self.p1points, self.p2points)



    def potentially_mutate(self, x):

        rand = random.randint(0, 20)

        if rand == 0 and x == 0:
            x = 1
            print("mutate 1")

        if rand == 0 and x == 1:
            x = 0
            print("mutate 0")

        return x


    def write_to_file(self, x, y):
        o = open("results.txt", "a")
        o.write("\n" + str(x) + " " + str(y))
        o.close()

    def calculate_points(self, p1, p2):

        if p1 == 0 and p2 == 0:
            self.p1points += 1
            self.p2points += 1

        if p1 == 1 and p2 == 0:
            self.p2points += 10

        if p1 == 0 and p2 == 1:
            self.p1points += 10

        if p1 == 1 and p2 == 1:
            self.p1points += 3
            self.p2points += 3

        print(self.p1points, self.p2points)


    def tit_for_tat(self, x):

        if x == 0:
            return 0

        if x == 1:
            return 1

        if x == 2:
            return 1

    def tat_for_tit(self, x):

        if x == 0:
            return 1

        if x == 1:
            return 0

        if x == 2:
            return 0


    def always_defect(self):
        return 0


    def always_cooperate(self):
        return 1


    def random_answer(self):
        return random.randint(0, 1)


    def scout(self, y):

        if (y/5).is_integer():
            return 0
        return 1

try1 = Tournament()

try1.run_tournament()
