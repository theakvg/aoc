f = open("input4.txt", "r")
inputList = []
for l in f: 
    l = l.strip()
    inputList.append(l)

sum = 0

for line in inputList: 
    tempSum = 0
    tables = line.split(":")[1].split("|")
    winningNum = tables[0].strip().split(" ")
    ownNum = tables[1].strip().split(" ")
    for i in ownNum: 
        if i == "": 
            continue
        if i in winningNum: 
            if tempSum == 0: 
                tempSum = 1
            else: 
                tempSum = tempSum*2
    sum += tempSum

print(sum)


# riktig: 26346