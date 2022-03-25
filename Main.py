import os
import json
import random

from Ocean import Ocean
import Dwellers

clear = lambda: os.system("cls")


class Interface:
    def __init__(self):
        self.ocean: Ocean

    def start(self):
        print("0. create new ocean\n1. load saved ocean\n2. random ocean")
        match self.input(0, 1):
            case 0:
                self.__newOcean()
            case 1:
                self.__download()
            case _:
                print("Error")
                return
        self.__printOcean()

    @staticmethod
    def input(begin, end):
        while True:
            key = input()
            if key.isdigit():
                if end >= int(key) >= begin:
                    return int(key)
            elif key == '':
                return begin
            print("invalid input, please try again")

    def __makeDweller (self, image):
        dwellersType = {'::': Dwellers.Plankton(self.ocean),
                        '%%': Dwellers.Daphnia(self.ocean),
                        '>@': Dwellers.ClownFish(self.ocean),
                        'oЖ': Dwellers.Octopus(self.ocean),
                        '>-': Dwellers.Tuna(self.ocean),
                        'A<': Dwellers.Shark(self.ocean),
                        'Qo': Dwellers.Whale(self.ocean)}
        return dwellersType[image]

    def __printMenu(self):
        clear()
        print("0. back to ocean\n1. create new ocean\n2. load saved ocean\n3. save ocean\n4. exit")
        match self.input(0, 4):
            case 0:
                self.__printOcean()
            case 1:
                self.__newOcean()
                self.__printOcean()
            case 2:
                self.__download()
                self.__printOcean()
            case 3:
                self.__save()
                self.__printOcean()
            case 4:
                self.__exit()

    def __printOcean(self):
        clear()
        self.ocean.print()
        print("0. next step\n1. call menu\n2. add dweller\n3. kill dweller")
        match self.input(0, 3):
            case 0:
                self.ocean.makeMove()
                self.__printOcean()
            case 1:
                self.__printMenu()
            case 2:
                self.__addDweller()
                self.__printOcean()
            case 3:
                self.__removeDweller()
                self.__printOcean()

    def __newOcean(self):
        print("enter ocean size: ")
        self.ocean = Ocean(self.input(2, 64))

    def __download(self):
        with open('Preservation.json') as file:
            data = json.load(file)
        self.ocean = Ocean(data['field size'])
        for characteristic in data['queue']:
            dweller = self.__makeDweller(characteristic['type'])
            dweller.setSex(characteristic['sex'])
            dweller.setLife(characteristic['life'])
            dweller.setWeight(characteristic['weight'])
            dweller.setSatiety(characteristic['satiety'])
            dweller.setSpeed(characteristic['speed'])
            dweller.setCooldown(characteristic['cooldown'])
            self.ocean.addDweller(dweller, characteristic['location'])
        self.ocean.makeMove()
        for characteristic in data['newborn']:
            newborn = self.__makeDweller(characteristic['type'])
            newborn.setSex(characteristic['sex'])
            self.ocean.addDweller(newborn, characteristic['location'])

    def __save(self):
        data = {'field size': self.ocean.getSize(), 'queue': [], 'newborn': []}
        for dweller in self.ocean.getQueue():
            if isinstance(dweller, Dwellers.Dweller):
                data['queue'].append({
                    'type': str(dweller),
                    'location': dweller.getLocation(),
                    'sex': dweller.getSex(),
                    'life': dweller.getLife(),
                    'weight': dweller.getWeight(),
                    'satiety': dweller.getSatiety(),
                    'speed': dweller.getSpeed(),
                    'cooldown': dweller.getCooldown()
                })
        for newborn in self.ocean.getNewborn():
            if isinstance(newborn, Dwellers.Dweller):
                data['newborn'].append({
                    'type': str(newborn),
                    'sex': newborn.getSex(),
                })
        with open('Preservation.json', 'w') as file:
            json.dump(data, file, indent=4)

    def __addDweller(self):
        print("choose location:\nline - ", end='')
        xСoordinate = self.input(0, self.ocean.getSize()-1)
        print("column - ", end='')
        yСoordinate = self.input(0, self.ocean.getSize() - 1)
        if str(self.ocean.getCell([xСoordinate, yСoordinate])) != '~~':
            print("attention! this cell is occupied")
        print("choose creature:\n0. CANCEL\n1. plankton\n2. daphnia\n3. clown fish\n4. octopus\n5. tuna\n6. shark\n7. whale")
        match self.input(0, 7):
            case 0:
                pass
            case 1:
                self.ocean.addDweller(Dwellers.Plankton(self.ocean), (xСoordinate, yСoordinate))
            case 2:
                self.ocean.addDweller(Dwellers.Daphnia(self.ocean), (xСoordinate, yСoordinate))
            case 3:
                self.ocean.addDweller(Dwellers.ClownFish(self.ocean), (xСoordinate, yСoordinate))
            case 4:
                self.ocean.addDweller(Dwellers.Octopus(self.ocean), (xСoordinate, yСoordinate))
            case 5:
                self.ocean.addDweller(Dwellers.Tuna(self.ocean), (xСoordinate, yСoordinate))
            case 6:
                self.ocean.addDweller(Dwellers.Shark(self.ocean), (xСoordinate, yСoordinate))
            case 7:
                self.ocean.addDweller(Dwellers.Whale(self.ocean), (xСoordinate, yСoordinate))

    def __removeDweller(self):
        print("choose location:\nline - ", end='')
        xСoordinate = self.input(0, self.ocean.getSize() - 1)
        print("column - ", end='')
        yСoordinate = self.input(0, self.ocean.getSize() - 1)
        dweller = self.ocean.getCell((xСoordinate, yСoordinate))
        if isinstance(dweller, Dwellers.Dweller):
            self.ocean.removeDweller(dweller)

    @staticmethod
    def __exit():
        clear()
        print("program has ended")
        return


interface = Interface()
interface.start()

