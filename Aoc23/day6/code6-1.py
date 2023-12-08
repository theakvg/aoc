f = open("input6.txt", "r")
inputList = []
for l in f: 
    l = l.strip()
    if len(l) != 0:
        inputList.append(l)

timeList = inputList[0].split(":")[1].split(" ")
timeList = list(filter(lambda a: a!= '', timeList))

distanceList = inputList[1].split(":")[1].split(" ")
distanceList = list(filter(lambda a: a!= '', distanceList))

total = 1

for race in range(0, len(timeList)): 
    currentTime = int(timeList[race])
    currentDistance = int(distanceList[race])
    currentSum = 0
    for sec in range(0, currentTime): 
        if sec*(currentTime-sec) > currentDistance: 
            currentSum += 1

    total = total*currentSum

print(total)


# result: 633080