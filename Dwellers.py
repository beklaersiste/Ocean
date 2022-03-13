from Ocean import Dweller


class Plant(Dweller):
    def __init__(self, ocean, life, weight):
        super().__init__(ocean, life, weight, life, 0)

    def __str__(self):
        return 'P'

    def makeMove(self):
        if super().makeMove():
            self.multiply()

    def multiply(self):
        for idx in self.getRoute():
            if str(self.getOcean().getCell([self.getLocation()[0] + idx[0], self.getLocation()[1] + idx[1]])) == '~~':
                newborn = self.getHeir()
                self.getOcean().addDweller(newborn, [self.getLocation()[0] + idx[0], self.getLocation()[1] + idx[1]])
                break


class Herbivorous(Dweller):
    def __init__(self, ocean, life, weight, hunger, speed):
        Dweller.__init__(self, ocean, life, weight, hunger, speed)

    def __str__(self):
        return 'XH'

    def makeMove(self):
        if super().makeMove():
            for idx in range(self.getSpeed()):
                if not self.eat():
                    self.move()

    def eat(self):
        for idx in self.getRoute():
            victim = self.getOcean().getCell([self.getLocation()[0] + idx[0], self.getLocation()[1] + idx[1]])
            if isinstance(victim, Plant):
                self.setHunger(victim.getWeight())
                self.moveTo(idx)
                return True


class Predator(Dweller):
    def __init__(self, ocean, life, weight, hunger, speed):
        Dweller.__init__(self, ocean, life, weight, hunger, speed)

    def makeMove(self):
        if super().makeMove():
            self.move()

    def __str__(self):
        return 'XR'


class Plankton(Plant):
    def __init__(self, ocean):
        super().__init__(ocean, 3, 1)

    def __str__(self):
        return '::'

    def getHeir(self):
        return Plankton(self.getOcean())


class Daphnia(Herbivorous):
    def __init__(self, ocean):
        super().__init__(ocean, 10, 2, 5, 1)

    def __str__(self):
        return '%%'


class ClownFish(Predator):
    def __init__(self, ocean):
        super().__init__(ocean, 7)
        # Predator.__init__(self)
        # Herbivorous.__init__(self)

    def __str__(self):
        return '>@'


class Octopus(Predator):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'oЖ'


class Tuna(Predator):
    def __init__(self, sex):
        super().__init__(sex)

    def __str__(self):
        return '>-'


class Shark(Predator):
    def __init__(self, ocean):
        super().__init__(ocean, 100000)

    def __str__(self):
        return 'A<'


class Whale(Herbivorous):
    def __init__(self, sex):
        super().__init__(sex)

    def __str__(self):
        return 'Qo'
