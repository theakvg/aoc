f = open("input3.txt", "r")
inputList = []
for l in f: 
    l = l.strip()
    inputList.append(l)

dataset = []
for line in range(0, len(inputList)): 
    dataset.append([])
    for letter in inputList[line]: 
        dataset[line].append(letter)

startIndex = 0
endIndex = None
currentNumberList = []
starDict = {}
sum = 0

for y in range(0, len(dataset)): 
    for x in range(0, len(dataset[y])): 
        if endIndex != None and x < endIndex: 
            continue
        elif endIndex != None and x == endIndex:
            endIndex = None
            continue
        if dataset[y][x].isdigit():
            startIndex = x
            isSymbol = False
            currentNumberList = []
            for i in range(0, 4):  
                if (x+i) > len(dataset[y])-1 or not dataset[y][x+i].isdigit(): 
                    endIndex = x + i -1
                    break
                else: 
                    currentNumberList.append(dataset[y][x+i])
            
            currentNumber = ''.join(currentNumberList)
            for a in range(-1, 2): 
                index = y+a
                if index >= 0 and index <= len(dataset)-1:
                    for n in range(startIndex - 1, endIndex + 2): 
                        if n >= 0 and n <= len(dataset[index])-1: 
                            if dataset[index][n] == "*":
                                key = str(index)+":"+str(n)
                                if key in starDict: 
                                    starDict[key].append(currentNumber)
                                else: 
                                    starDict[key] = [currentNumber]


for key in starDict: 
    if len(starDict[key]) == 2: 
        gears = int(starDict[key][0]) * int(starDict[key][1])
        sum += gears

print(sum)

