import random
from typing import List


class Dweller:
    def __init__(self, ocean, life, weight, hunger, speed, cooldown):
        self.__ocean: Ocean = ocean
        self.__location = [0, 0]
        self.__sex = random.randrange(2)
        self.__life = life
        self.__weight = weight
        self.__hunger = hunger
        self.__maxHunger = hunger
        self.__speed = speed
        self.__cooldown = int(cooldown / 3)
        self.__maxCooldown = cooldown

    def __str__(self):
        return 'XX'

    def getOcean(self):
        return self.__ocean

    def getHeir(self):
        pass

    def getLocation(self):
        return self.__location

    def getWeight(self):
        return self.__weight

    def getSex(self):
        return str(self.__sex)

    def getSpeed(self):
        return self.__speed

    def setLocation(self, location):
        self.__location[0] = location[0]
        self.__location[1] = location[1]

    def setHunger(self, food_weight):
        self.__hunger = self.__hunger + food_weight
        if self.__hunger > self.__maxHunger:
            self.__hunger = self.__maxHunger

    @staticmethod
    def getRoute():
        route = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
        random.shuffle(route)
        return route

    def makeMove(self):
        self.__life = self.__life - 1
        self.__hunger = self.__hunger - 1
        self.__cooldown = self.__cooldown - 1
        if (self.__life > 0) & (self.__hunger > 0):
            if self.__location[0] == self.__ocean.getSize() - 1:
                self.__location[0] = -1
            if self.__location[0] == - self.__ocean.getSize():
                self.__location[0] = 0
            if self.__location[1] == self.__ocean.getSize() - 1:
                self.__location[1] = -1
            if self.__location[1] == - self.__ocean.getSize():
                self.__location[1] = 0
            return True
        self.die()

    def moveTo(self, location):
        if isinstance(self.__ocean.getCell(location), Dweller):
            self.__ocean.getCell(location).die()
        self.__ocean.setCell('~~', self.__location)
        self.__location[0] = self.__location[0] + location[0]
        self.__location[1] = self.__location[1] + location[1]
        self.__ocean.setCell(self, self.__location)

    def move(self):
        for idx in self.getRoute():
            if str(self.__ocean.getCell([self.__location[0] + idx[0], self.__location[1] + idx[1]])) == '~~':
                self.moveTo(idx)
                break

    def eat(self):
        pass

    def multiply(self):
        pass

    def die(self):
        self.__ocean.removeDweller(self)


class Ocean:
    def __init__(self, field_size):
        self.__field = [['~~'] * field_size for i in range(field_size)]
        self.__queue = []
        self.__newborn: List[Dweller] = []

    def getSize(self):
        return len(self.__field)

    def addDweller(self, dweller, location):
        self.__field[location[0]][location[1]] = dweller
        dweller.setLocation(location)
        self.__newborn.append(dweller)

    def removeDweller(self, dweller):
        self.setCell('~~', dweller.getLocation())
        if self.__queue.count(dweller):
            self.__queue.insert(self.__queue.index(dweller), None)
            self.__queue.remove(dweller)
        elif self.__newborn.count(dweller):
            self.__newborn.remove(dweller)

    def getCell(self, location):
        return self.__field[location[0]][location[1]]

    def setCell(self, obj, location):
        self.__field[location[0]][location[1]] = obj

    def makeMove(self):
        for dweller in self.__queue:
            if dweller is not None:
                dweller.makeMove()
        self.__newborn.extend(self.__queue)
        self.__queue = sorted(list(filter(None, self.__newborn)), key=lambda iDweller: iDweller.getWeight())
        self.__newborn.clear()

    def print(self):
        for row in self.__field:
            for element in row:
                print(str(element), end=' ')
            print()