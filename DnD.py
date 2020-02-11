import random
import math
import keyboard

def rollD20():
    return random.randint(1, 20)


def sortByIntiative(arr):
    num = len(arr)
    for i in range(num):
        for j in range(0, num - i - 1):
            if arr[j].initiative > arr[j + 1].initiative:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    for i in range(math.floor(num / 2)):
        arr[i], arr[num - i - 1] = arr[num - i - 1], arr[i]

    return arr


def printFighters(roster):
    for fighter in roster:
        print('%-2d %s' % (fighter.initiative, fighter.name))
    print('All Done!\n\n')


def goDownList(roster):
    roster.append(roster[0])
    roster.pop(0)
    return roster


def mainGameLoop(roster):
    notExiting = True
    timer = 0

    while notExiting:
        if keyboard.is_pressed('n') and timer > 10000:
            roster = goDownList(roster)
            printFighters(roster)
            timer = 0
        if keyboard.is_pressed('e'):
            notExiting = False
        timer += 1


class combatant():
    def __init__(self, name, enemOrFriend, dexMod):
        self.name = name
        self.enemOrFriend = enemOrFriend
        self.initiative = rollD20() + dexMod

def main():
    combats = []

    numCombats = input('How many combatants are there? ')
    for idx in range(int(numCombats)):  # creates all combatants
        idx = str(idx + 1)
        name = 'combatant' + idx
        name = combatant(name, 1, 2)
        combats.append(name)

    combats = sortByIntiative(combats)

    mainGameLoop(combats)
main()
