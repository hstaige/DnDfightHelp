import random

def rollD20():
    return(random.randint(1,20))

# def sortByIntiative(roster):
#     for idx in range(len(roster)):
#         for fighter2 in range(roster:
#             if fighter1.initiative < fighter2.initiative:
#                 placeholder = fighter1
#                 fighter1 = fighter2
#                 fighter2 = placeholder
#     return(roster)

def sortByIntiative(arr):
    num = len(arr)
    for i in range(num):
        for j in range(0, num-i-1):
            if arr[j].initiative > arr[j+1].initiative :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    temp = arr
    for i in range(num):
        arr[i] = temp[num-i-1]
        print(arr.name)

    return(arr)

class combatant():
    def __init__(self, name,enemOrFriend, dexMod):
        self.name = name
        self.enemOrFriend = enemOrFriend
        self.initiative = rollD20() + dexMod


def main():
    combats = []

    numCombats = input('How many combatants are there? ')
    for idx in range(int(numCombats)): #creates all combatants
        idx = str(idx+1)
        name = 'combatant' + idx
        name = combatant(name,1,2)
        combats.append(name)

    combats = sortByIntiative(combats)



    for fighter in combats:
        print('%-2d %s' % (fighter.initiative, fighter.name))

main()
