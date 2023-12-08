from functools import cmp_to_key

f = open("input7.txt", "r")
inputList = []
for l in f: 
    l = l.strip()
    if len(l) != 0:
        temp = l.split(' ')
        inputList.append(temp)

listChar = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
total = 0

def compare(card1, card2): 
    rank1 = findRank(card1[0])
    rank2 = findRank(card2[0])
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
    
    rank = 1

    for c in card: 
        if (card.count(c) == 5) or (c != 'J' and card.count(c) + card.count('J') == 5):
            rank = 7
        elif rank < 6 and ((card.count(c) == 4) or (c != 'J' and card.count(c) + card.count('J') == 4)):
            rank = 6
        elif rank < 4 and ((card.count(c) == 3) or (c != 'J' and card.count(c) + card.count('J') == 3)): 
            rank = 4
        for d in card: 
            if rank < 5 and c != d and ((card.count(c) + card.count(d) == 5) or (c != 'J' and d != 'J' and card.count('J') + card.count(c) + card.count(d) == 5)): 
                print(c, d, card.count('J'), card.count(c), card.count(d))
                rank = 5
            elif rank < 3 and c != d and ((card.count(c) + card.count(d) == 4) or (c != 'J' and d != 'J' and card.count('J') + card.count(c) + card.count(d) == 4)):
                rank = 3 
            
        if rank < 2 and (card.count(c) == 2 or (c != 'J' and card.count(c) + card.count('J') == 2)): 
            rank = 2
    return rank

sortedList = sorted(inputList, key=cmp_to_key(compare))

for sl in range(0, len(sortedList)):
    total += int(sortedList[sl][1])*(sl+1)
print(sortedList)
print(total)

# right: 249356515
