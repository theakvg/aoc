f = open("input4.txt", "r")
inputList = []
for l in f: 
    l = l.strip()
    inputList.append(l)

sum = 0
cardDict = {}

for card in inputList: 
    cardNum = int(card.split(":")[0].split(" ")[-1])
    cardDict[cardNum] = 1


for line in inputList: 
    tempSum = 0
    cardNum = int(line.split(":")[0].split(" ")[-1])
    tables = line.split(":")[1].split("|")
    winningNum = tables[0].strip().split(" ")
    ownNum = tables[1].strip().split(" ")
    for i in ownNum: 
        if i == "": 
            continue
        if i in winningNum: 
            tempSum += 1
    for s in range(1, tempSum+1): 
        cardDict[cardNum+s] = cardDict[cardNum+s] + (1*cardDict[cardNum])

cards = list(cardDict.values())
for c in cards:
    sum += c


print(sum)


# riktig: 8467762