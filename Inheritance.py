class Fish:
    def __init__(self, firstName, lastName="Fish"):
        self.firstName = firstName
        self.lastName = lastName

    def swim(self):
        print("Fish can swim")

    def aboutMe(self):
        print("Fish {0} - {1}".format(self.firstName, self.lastName))


class GoldFis(Fish):
    pass


g = GoldFis("Silver Line")
print(g.firstName)
g.aboutMe()

print("----------")


class Trout(Fish):
    def backwardSwim(self):
        print("Fish can swim backward")


t = Trout("WildTrout")
t.aboutMe()
t.swim()
t.backwardSwim()

print("----------")


class Shark(Fish):
    def __init__(self, firstName, lastName="Shark"):
        self.firstName = "Wild" + firstName
        self.lastName = lastName

    def swim(self):
        print("Shark can swim 100 miles per hour")


s = Shark("Sea")
s.aboutMe()
s.swim()

print("----------")


class Salmon(Fish):
    def __init__(self, firstName, lastName):
        self.healthInfo = "Its one of the healthy sea food"
        super().__init__(firstName, lastName)

    def swim(self):
        print("Tasty salom...")
        super().swim()


sl = Salmon("Brown", "Salmon")
sl.aboutMe()
sl.swim()
print("Health Info {0}".format(sl.healthInfo))

print("----------")


class WildSalmon(Salmon):
    pass


ws = WildSalmon("wild Horse", "Salmon")
ws.aboutMe()
ws.swim()

# ---------
print("----------")


class Fittness:
    def __init__(self, name):
        print("Welcome to Fitness club {0}".format(name))

    def messageFittnes(self):
        print("Gym operating hours chnaged due to waether")


class Recreational:
    def __init__(self, name):
        print("Welcome to Recreational club {0}".format(name))

    def messageRecreational(self):
        print("Recreational operating hours changed due to waether")


class Club(Recreational, Fittness):
    pass


c = Club("Senthil")
c.messageFittnes()
c.messageRecreational()
