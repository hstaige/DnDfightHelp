import math

def goDownList(roster): #proceeds down list
    roster.append(roster[0])
    roster.pop(0)
    return roster

def sortByIntiative(arr): #gets list of random initiatives sorted
    num = len(arr)
    for i in range(num):
        for j in range(0, num - i - 1):
            if arr[j].initiative > arr[j + 1].initiative:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    for i in range(math.floor(num / 2)):
        arr[i], arr[num - i - 1] = arr[num - i - 1], arr[i]

    return arr

def removeTheDead(roster): #removes dead fighters from the initiative list
    for fighter in roster:
        if fighter.hp < 0:
            print('%s has died!' % (fighter.name))
            roster.pop(roster.index(fighter))
