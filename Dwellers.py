from Ocean import Dweller

class Predator(Dweller):
    def __init__(self, ocean, sex):
        Dweller.__init__(self, ocean, sex)

    def makeMove(self):
        if not super().makeMove():
            self.move()

    def __str__(self):
        return 'XR'

class Herbivorous(Dweller):
    def __init__(self, ocean, sex):
        Dweller.__init__(self, ocean, sex)

    def makeMove(self):
        if not super().makeMove():
            self.move()

    def __str__(self):
        return 'XH'


class Plant(Dweller):
    def __init__(self, ocean):
        super().__init__(ocean, 0)

    def __str__(self):
        return 'P'

    def makeMove(self):
        if not super().makeMove():
            self.multiply()

    def multiply(self): pass


class Plankton(Plant):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return '::'


class Daphnia(Herbivorous):
    def __init__(self, sex):
        super().__init__(sex)

    def __str__(self):
        return '%%'


class ClownFish(Predator, Herbivorous):
    def __init__(self, ocean, sex):
        Dweller.__init__(self, ocean, sex)
        # Predator.__init__(self, sex)
        # Herbivorous.__init__(self, sex)

    def __str__(self):
        return '>@'


class Octopus(Predator):
    def __init__(self, sex):
        super().__init__(sex)

    def __str__(self):
        return 'oЖ'


class Tuna(Predator):
    def __init__(self, sex):
        super().__init__(sex)

    def __str__(self):
        return '>-'


class Shark(Predator):
    def __init__(self, ocean, sex):
        super().__init__(ocean, sex)

    def __str__(self):
        return 'A<'


class Whale(Herbivorous):
    def __init__(self, sex):
        super().__init__(sex)

    def __str__(self):
        return 'Qo'