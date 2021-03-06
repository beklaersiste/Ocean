from Ocean import Dweller


class Plant(Dweller):
    def __init__(self, ocean, life, weight):
        super().__init__(ocean, life, weight, life, 0, 0)

    def __str__(self):
        return 'XP'

    def makeMove(self):
        if super().makeMove():
            self.checkLocation()
            self.multiply()

    def multiply(self):
        for idx in self.getRoute():
            if str(self.getOcean().getCell([self.getLocation()[0] + idx[0], self.getLocation()[1] + idx[1]])) == '~~':
                newborn = self.getHeir()
                self.getOcean().addDweller(newborn, [self.getLocation()[0] + idx[0], self.getLocation()[1] + idx[1]])
                break


class Animal(Dweller):
    def __init__(self, ocean, life, weight, satiety, speed, cooldown):
        super().__init__(ocean, life, weight, satiety, speed, cooldown)

    def __str__(self):
        return 'XA'

    def multiply(self):
        for idxPartner in self.getRoute():
            partner = self.getOcean().getCell(
                [self.getLocation()[0] + idxPartner[0], self.getLocation()[1] + idxPartner[1]])
            if type(partner) == type(self) and partner.getSex() != self.getSex() and self.getCooldown() <= 0 and partner.getCooldown() <= 0:
                for idx in self.getRoute():
                    if str(self.getOcean().getCell(
                            [self.getLocation()[0] + idx[0], self.getLocation()[1] + idx[1]])) == '~~':
                        newborn = self.getHeir()
                        self.getOcean().addDweller(newborn,
                                                   [self.getLocation()[0] + idx[0], self.getLocation()[1] + idx[1]])
                        self.restartCooldown()
                        partner.restartCooldown()
                        return True


class Herbivorous(Animal):
    def __init__(self, ocean, life, weight, satiety, speed, cooldown):
        super().__init__(ocean, life, weight, satiety, speed, cooldown)

    def __str__(self):
        return 'XH'

    def makeMove(self):
        if super().makeMove():
            for idx in range(self.getSpeed()):
                self.checkLocation()
                if self.getCooldown() <= 0:
                    if self.multiply():
                        return
                if self.eat():
                    return
                self.move()

    def eat(self):
        for idx in self.getRoute():
            victim = self.getOcean().getCell([self.getLocation()[0] + idx[0], self.getLocation()[1] + idx[1]])
            if isinstance(victim, Plant):
                self.increaseSatiety(victim.getWeight())
                self.moveTo(idx)
                return True


class Predator(Animal):
    def __init__(self, ocean, life, weight, satiety, speed, cooldown):
        super().__init__(ocean, life, weight, satiety, speed, cooldown)

    def makeMove(self):
        if super().makeMove():
            for idx in range(self.getSpeed()):
                self.checkLocation()
                if self.getCooldown() <= 0 and not self.isHungry():
                    if self.multiply():
                        return
                if self.eat():
                    return
                self.move()

    def __str__(self):
        return 'XR'

    def eat(self):
        for idx in self.getRoute():
            victim = self.getOcean().getCell([self.getLocation()[0] + idx[0], self.getLocation()[1] + idx[1]])
            if isinstance(victim, Animal) and self.getWeight() > victim.getWeight() > self.getWeight() / 5:
                self.increaseSatiety(victim.getWeight())
                self.moveTo(idx)
                return True


class Plankton(Plant):
    def __init__(self, ocean):
        super().__init__(ocean, 3, 1)

    def __str__(self):
        return '::'

    def getHeir(self):
        return Plankton(self.getOcean())


class Daphnia(Herbivorous):
    def __init__(self, ocean):
        super().__init__(ocean, 10, 2, 5, 1, 2)

    def __str__(self):
        return '%%'

    def getHeir(self):
        return Daphnia(self.getOcean())


class ClownFish(Predator):
    def __init__(self, ocean):
        super().__init__(ocean, 15, 5, 6, 2, 3)

    def __str__(self):
        return '>@'

    def getHeir(self):
        return ClownFish(self.getOcean())


class Octopus(Predator):
    def __init__(self, ocean):
        super().__init__(ocean, 30, 7, 10, 3, 6)

    def __str__(self):
        return 'o??'

    def getHeir(self):
        return Octopus(self.getOcean())


class Tuna(Predator):
    def __init__(self, ocean):
        super().__init__(ocean, 45, 12, 16, 2, 8)

    def __str__(self):
        return '>-'

    def getHeir(self):
        return Tuna(self.getOcean())


class Shark(Predator):
    def __init__(self, ocean):
        super().__init__(ocean, 60, 30, 20, 3, 10)

    def __str__(self):
        return 'A<'

    def getHeir(self):
        return Shark(self.getOcean())


class Whale(Herbivorous):
    def __init__(self, ocean):
        super().__init__(ocean, 100, 50, 30, 2, 15)

    def __str__(self):
        return 'Qo'

    def getHeir(self):
        return Whale(self.getOcean())
