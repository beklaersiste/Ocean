import random

class Dweller:
    def __init__(self, ocean, sex):
        self.__ocean: Ocean = ocean
        self.__location = [0, 0]
        self.__sex = sex
        self.__weight = 0
        self.__life = 0
        self.__hunger = 0
        self.__maxHunger = 0
        self.__speed = 0

    def __str__(self):
        return 'XX'

    def getLocation(self):
        return self.__location

    def setLocation(self, location):
        self.__location[0] = location[0]
        self.__location[1] = location[1]

    def makeMove(self):
        self.__life = self.__life - 1
        if self.__life < 0:
            self.die()
            return False

    def move(self):
        route = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
        random.shuffle(route)
        if self.__location[0] == self.__ocean.getSize() - 1:
            self.__location[0] = -1
        if self.__location[0] == - self.__ocean.getSize():
            self.__location[0] = 0
        if self.__location[1] == self.__ocean.getSize() - 1:
            self.__location[1] = -1
        if self.__location[1] == - self.__ocean.getSize():
            self.__location[1] = 0
        for idx in route:
            if str(self.__ocean.fieldInfo([self.__location[0] + idx[0], self.__location[1] + idx[1]])) == '~~':
                self.__ocean.setCell('~~', self.__location)
                if self.__location[0] + idx[0] >= self.__ocean.getSize():
                    self.__location[0] = 0
                else:
                    self.__location[0] = self.__location[0] + idx[0]
                if self.__location[1] + idx[1] >= self.__ocean.getSize():
                    self.__location[1] = 0
                else:
                    self.__location[1] = self.__location[1] + idx[1]
                self.__ocean.setCell(self, self.__location)
                break

    def eat(self):
        pass

    def multiply(self):
        pass

    def die(self):
        pass

    def getSex(self):
        return str(self.__sex)


class Ocean:
    def __init__(self, field_size):
        self.__field = [['~~'] * field_size for i in range(field_size)]
        self.__queue = []

    def getSize(self):
        return len(self.__field)

    def addDweller(self, dweller, location):
        self.__field[location[0]][location[1]] = dweller
        dweller.setLocation(location)

    def fieldInfo(self, location):
        return self.__field[location[0]][location[1]]

    def setCell(self, object, location):
        self.__field[location[0]][location[1]] = object

    def makeMove(self):
        pass

    def print(self):
        for row in self.__field:
            for element in row:
                print(str(element), end=' ')
            print()
