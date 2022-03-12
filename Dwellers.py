import copy

from Ocean import Dweller


class Predator(Dweller):
    def __init__(self, ocean, life):
        Dweller.__init__(self, ocean, life)

    def makeMove(self):
        if super().makeMove():
            self.move()

    def __str__(self):
        return 'XR'


class Herbivorous(Dweller):
    def __init__(self, ocean, life):
        Dweller.__init__(self, ocean, life)

    def makeMove(self):
        if super().makeMove():
            self.move()

    def __str__(self):
        return 'XH'


class Plant(Dweller):
    def __init__(self, ocean, life):
        super().__init__(ocean, life)

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


class Plankton(Plant):
    def __init__(self, ocean):
        super().__init__(ocean, 3)

    def __str__(self):
        return '::'

    def getHeir(self):
        return Plankton(self.getOcean())


class Daphnia(Herbivorous):
    def __init__(self, sex):
        super().__init__(sex)

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
