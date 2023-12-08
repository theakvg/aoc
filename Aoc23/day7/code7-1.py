from functools import cmp_to_key

f = open("input7.txt", "r")
inputList = []
for l in f: 
    l = l.strip()
    if len(l) != 0:
        temp = l.split(' ')
        inputList.append(temp)

listChar = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
total = 0

def compare(card1, card2): 
    rank1 = findRank(card1)
    rank2 = findRank(card2)
    if rank1 != rank2: 
        if rank1 > rank2: 
            return 1
        else:
            return -1
    for x in range(0, len(card1[0])): 
        if listChar.index(card1[0][x]) != listChar.index(card2[0][x]): 
            if listChar.index(card1[0][x]) > listChar.index(card2[0][x]): 
                return 1
            else:
                return -1

def findRank(card): 
    rank = 0
    numCard = 0
    for char in listChar: 
        if card[0].count(char) == 5: 
            rank = 7
            break
        elif card[0].count(char) == 4: 
            rank = 6
            break
        if card[0].count(char) > 1: 
            numCard += card[0].count(char)
    if rank == 0: 
        match numCard: 
            case 5: 
                rank = 5
            case 3: 
                rank = 4
            case 4: 
                rank = 3
            case 2:
                rank = 2
            case 0: 
                rank = 1
    return rank

sortedList = sorted(inputList, key=cmp_to_key(compare))

for sl in range(0, len(sortedList)):
    total += int(sortedList[sl][1])*(sl+1)

print(total)

# riktig: 246795406
