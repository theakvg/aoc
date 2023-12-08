f = open("input6.txt", "r")
inputList = []
for l in f: 
    l = l.strip()
    if len(l) != 0:
        inputList.append(l)

timeList = inputList[0].split(":")[1].split(" ")
timeList = list(filter(lambda a: a!= '', timeList))
currentTime = int(''.join(timeList))

distanceList = inputList[1].split(":")[1].split(" ")
distanceList = list(filter(lambda a: a!= '', distanceList))
currentDistance = int(''.join(distanceList))

currentSum = 0
for sec in range(0, currentTime): 
    if sec*(currentTime-sec) > currentDistance: 
        currentSum = currentTime - (sec*2) +1
        break


print(currentSum)


# result: 20048741