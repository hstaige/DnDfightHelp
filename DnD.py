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


def createNPCfighters(combats):
    numCombats = int(input('How many enemys are there? '))
    for idx in range(numCombats):  # creates all npc combatants
        idx = str(idx + 1)
        name = 'Enemy' + ' ' + idx
        name = combatant(name, 1, 2)
        combats.append(name)

    return combats


def addPCs(combats):
    numPlayers = int(input('How many PCs are there? '))
    for idx in range(numPlayers):
        playerName = input('What is the name of PC %d? ' % (idx+1))
        PC = combatant(playerName, 0, 2)
        combats.append(PC)

    return combats


def printFighters(roster):
    for fighter in roster:
        print('%-2d %s' % (fighter.initiative, fighter.name))
    print('All Done!\n')


def goDownList(roster):
    roster.append(roster[0])
    roster.pop(0)
    return roster


def mainGameLoop(roster):
    notExiting = True
    timer = 0

    printFighters(roster)

    while notExiting:
        if keyboard.is_pressed('n') and timer > 10000: #Ends Turn
            roster = goDownList(roster)
            printFighters(roster)
            timer = 0
        if keyboard.is_pressed('e'): #Exits program
            notExiting = False
        if keyboard.is_pressed('a') and timer>10000: #Makes attack
            attacker = roster[0]
            attacker.makeAttack(roster,1)
            timer = 0

        timer += 1 #prevents multiple inputs


class combatant():
    def __init__(self, name, enemOrFriend, dexMod):
        self.name = name
        self.enemOrFriend = enemOrFriend
        self.initiative = rollD20() + dexMod
        self.hp = int(input("what is this fighters current HP? "))
    def makeAttack(self, roster,targetIdx):
        deadIdxs = []
        print('\n')
        dmg = int(input('How much damage does this attack deal? '))
        for idx in range(targetIdx):
            roster[idx].hp -= dmg
            if roster[idx].hp <= 0:
                print("%s has died!\n" % (roster[idx].name))
                deadIdxs.append(idx)
        return deadIdxs



def main():
    combats = []

    combats = createNPCfighters(combats)
    combats = addPCs(combats)
    combats = sortByIntiative(combats)
    print('\n')
    print('\n')

    mainGameLoop(combats)


if __name__ == '__main__':
    main()
