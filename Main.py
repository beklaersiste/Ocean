import os
from Ocean import Ocean
import Dwellers



o: Ocean = Ocean(4)
# o.addDweller(Plankton(), [2, 2])
# o.addDweller(Daphnia('f'), [5, 2])
fish = Dwellers.ClownFish(o, 'f')
o.addDweller(fish, [1, 1])
shark = Dwellers.Shark(o, 'f')
o.addDweller(shark, [1, 2])

# o.addDweller(Octopus('f'), [4, 3])
# o.addDweller(Tuna('f'), [3, 6])
# o.addDweller(Shark('f'), [2, 5])
# o.addDweller(Whale('f'), [4, 4])
clear = lambda: os.system("cls")
# while True:
#     fish.move()
#     o.print()
#     input()
#     clear()

while True:
    clear()
    fish.move()
    shark.move()
    o.print()
    input()


