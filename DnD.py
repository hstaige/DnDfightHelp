import random
import math
import keyboard
import time

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


def areYouTesting():
    timer = 0
    while timer < 100000:
        if keyboard.is_pressed('s'):#standard
            return True
        timer += 1
    else:
        return False


def createNPCfighters(combats,testing):

    if testing:
        numCombats = 9
        hp = 9
    else:
        numCombats = int(input('How many enemys are there? ')) #npc count input

    for idx in range(numCombats):  # creates all npc combatants
        idx = str(idx + 1)
        name = 'Enemy' + ' ' + idx
        if not testing:
            hp = int(input('What is the hp of enemy %d? ' % (idx+1)))
        name = combatant(name, 1, 2, hp)
        combats.append(name)

    return combats


def addPCs(combats,testing):
    if testing:
        numPlayers = 3
        hp = 10
        playerName = 'Testing!'
    else:
        numPlayers = int(input('How many PCs are there? '))

    for idx in range(numPlayers):
        if not testing:
            hp = int(input('What is the current hp of %s? ' % (playerName)))
            playerName = input('What is the name of PC %d? ' % (idx+1))
        PC = combatant(playerName, 0, 2, hp)
        combats.append(PC)

    return combats


def printFighters(roster): #need to add formatting, want to make it a table
    print('%-5s%-12s' % ('Init|','Fighter Name|'))
    for fighter in roster:
        print('%-5d%-12s' % (fighter.initiative, fighter.name))
    print('\nAll Done!\n')


def goDownList(roster):
    roster.append(roster[0])
    roster.pop(0)
    return rosters


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
    def __init__(self, name, enemOrFriend, dexMod, currentHP):
        self.name = name
        self.enemOrFriend = enemOrFriend
        self.initiative = rollD20() + dexMod
        self.hp = currentHP
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

    standardBool = areYouTesting()
    combats = createNPCfighters(combats,standardBool)
    combats = addPCs(combats,standardBool)
    combats = sortByIntiative(combats)
    print('\n\n')

    mainGameLoop(combats)


if __name__ == '__main__':
    main()
