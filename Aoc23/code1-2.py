f = open("input1-jakob.txt", "r")
inputList = []
for l in f: 
    inputList.append(l)
sum = 0
stringNumber = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
check = 0
for line in inputList:
    check += 1 
    dictcurretNumber = []
    for x in range(0, len(line)): 
        if line[x].isdigit(): 
            dictcurretNumber.append([x, line[x]])

    for num in stringNumber:
        if line.count(num) > 0:
            nextIndex = 0
            for i in range(0, line.count(num)): 
                nextIndex += line[nextIndex:].find(num)
                dictcurretNumber.append([nextIndex, stringNumber.index(num)])
                nextIndex += len(num)
    sortedDict = sorted(dictcurretNumber, key=lambda x:x[0])
    currentNumber = ''.join([str(sortedDict[0][1]), str(sortedDict[-1][1])])
    sum += int(currentNumber)

print(sum)

# answer: 57345
