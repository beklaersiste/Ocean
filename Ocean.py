import random
from typing import List


class Dweller:
    def __init__(self, ocean, life, weight, satiety, speed, cooldown):
        self.__ocean: Ocean = ocean
        self.__location = [0, 0]
        self.__sex = random.randrange(2)
        self.__life = life
        self.__weight = weight
        self.__satiety = satiety
        self.__maxSatiety = satiety
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

    def getSex(self):
        return self.__sex

    def getLife(self):
        return self.__life

    def getWeight(self):
        return self.__weight

    def getSatiety(self):
        return self.__satiety

    def getSpeed(self):
        return self.__speed

    def getCooldown(self):
        return self.__cooldown

    def isHungry(self):
        if self.__satiety <= self.__maxSatiety / 2:
            return True
        else:
            return False

    def setLocation(self, location):
        self.__location[0] = location[0]
        self.__location[1] = location[1]

    def setSatiety(self, food_weight):
        self.__satiety = self.__satiety + food_weight
        if self.__satiety > self.__maxSatiety:
            self.__satiety = self.__maxSatiety

    def setCooldown(self):
        self.__cooldown = self.__maxCooldown if self.getSex() else 0

    @staticmethod
    def getRoute():
        route = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
        random.shuffle(route)
        return route

    def checkLocation(self):
        if self.__location[0] == self.__ocean.getSize() - 1:
            self.__location[0] = -1
        if self.__location[0] == - self.__ocean.getSize():
            self.__location[0] = 0
        if self.__location[1] == self.__ocean.getSize() - 1:
            self.__location[1] = -1
        if self.__location[1] == - self.__ocean.getSize():
            self.__location[1] = 0

    def makeMove(self):
        self.__life = self.__life - 1
        self.__satiety = self.__satiety - 1
        self.__cooldown = self.__cooldown - 1
        if self.__life > 0 and self.__satiety > 0:
            return True
        self.die()

    def moveTo(self, location):
        if isinstance(self.__ocean.getCell([self.__location[0] + location[0], self.__location[1] + location[1]]), Dweller):
            self.__ocean.getCell([self.__location[0] + location[0], self.__location[1] + location[1]]).die()
        self.__ocean.setCell('~~', self.__location)
        self.__location[0] = self.__location[0] + location[0]
        self.__location[1] = self.__location[1] + location[1]
        self.__ocean.setCell(self, self.__location)

    def move(self):
        for idx in self.getRoute():
            if str(self.__ocean.getCell([self.__location[0] + idx[0], self.__location[1] + idx[1]])) == '~~':
                self.moveTo(idx)
                return

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

    def getQueue(self):
        return self.__queue

    def getNewborn(self):
        return self.__newborn

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
