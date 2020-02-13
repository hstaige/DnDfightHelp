from initializer import *
from listHandling import *


def printFighters(roster): #need to add formatting, want to make it a table
    print('%-5s%-13s%-12s%-15s' % ('Init|','Fighter Name|','current HP|',\
    'Status Effects|'))
    for fighter in roster:
        print('%-5d%-13s%-12d%-15s' % (fighter.initiative, \
        fighter.name, fighter.hp, fighter.status))
    print('\nAll Done!\n')


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
            attacker.makeAttack(roster)
            timer = 0
        if keyboard.is_pressed('s') and timer>10000: #Adds status effect
            attacker = roster[0]
            attacker.applyStatus(roster)
            timer = 0

        timer += 1 #prevents multiple inputs


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
