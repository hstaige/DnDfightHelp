import random
import math
import keyboard
import time
from listHandling import *


def areYouTesting():
    timer = 0
    while timer < 100000:
        if keyboard.is_pressed('s'):#standard
            return True
        timer += 1
    else:
        return False


def rollD20():
    return random.randint(1, 20)


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
            hp = int(input('What is the hp of enemy %d? ' % (idx)))
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


class combatant():
    def __init__(self, name, enemOrFriend, dexMod, currentHP):
        self.name = name
        self.enemOrFriend = enemOrFriend
        self.initiative = rollD20() + dexMod
        self.hp = currentHP
        self.status = set()


    def makeAttack(self, roster):
        while True:
            try:
                dmg = int(input('How much damage does this attack deal? '))
                targetName = input('who is being attacked?')
                break
            except ValueError:
                print('\nPlease enter the right type of data.\n')

        for fighter in roster:
            if fighter.name == targetName:
                fighter.hp -= dmg

        roster = removeTheDead(roster)

        return roster


    def applyStatus(self,roster,status,targetName):
        while True:
            try:
                statusEff = input('What status effect has been applyed?')
                targetName = input('And who has it been applied to?')
                break
            except ValueError:
                print('\nPlease enter the right type of data.\n')

        for fighter in roster:
                if fighter.name == targetName:
                    fighter.status.add(status)
