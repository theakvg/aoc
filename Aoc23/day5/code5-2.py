f = open("input5.txt", "r")
inputList = []
for l in f: 
    l = l.strip()
    if len(l) != 0:
        inputList.append(l)
tempseeds = []
seeds = []
ranges = []
tempseeds = inputList[0].split(":")[1].split(" ")
tempseeds.remove("")
for s in range(0, len(tempseeds), 2):
    seeds.append([int(tempseeds[s]), int(tempseeds[s])+int(tempseeds[s+1])-1])
for index in range(1, len(inputList)-1): 
    if ":" in inputList[index]: 
        ranges.append([])
        index +=1
        while index < len(inputList) and ":" not in inputList[index]: 
            temp = inputList[index].split(" ")
            ranges[-1].append([int(temp[0]) - int(temp[1]), int(temp[1]), int(temp[1])+int(temp[2])-1])
            index += 1



locations = []


for seed in seeds:
    currentRanges = [seed]
    for range in ranges: 
        changedSeeds = []
        unchangedSeeds = currentRanges
        for line in range:
            test = unchangedSeeds.copy()
            for uc in test: 
                changedSeed = []
                oldSeed = []
                oldSeed2 = []
                splittedRange = False
                if uc[0] >= line[1] and uc[1] <= line[2]:
                    changedSeed = [uc[0]+line[0], uc[1]+line[0]]
                elif uc[1] < line[1] or uc[0] > line[2]:
                    oldSeed = uc
                elif uc[0] < line[1] and uc[1] < line[2]: 
                    oldSeed = [uc[0], line[1]-1]
                    changedSeed = [line[1]+line[0], uc[1]+line[0]]
                    splittedRange = True
                elif uc[0] > line[1] and uc[1] > line[2]: 
                    oldSeed = [line[2]+1, uc[1]]
                    changedSeed = [uc[0]+line[0], line[2]+line[0]]
                    splittedRange = True
                elif uc[0] < line[1] and uc[1] > line[2]: 
                    oldSeed = [uc[0], line[1]-1] 
                    oldSeed2 = [line[2]+1, uc[1]]
                    changedSeed = [line[1]+line[0], line[2]+line[0]]
                    splittedRange = True
                if splittedRange: 
                    changedSeeds.append(changedSeed)
                    unchangedSeeds.append(oldSeed)
                    test.append(oldSeed)
                    unchangedSeeds.remove(uc)
                    if oldSeed2 != []:
                        unchangedSeeds.append(oldSeed2)
                        test.append(oldSeed2)
                elif changedSeed != []:
                    changedSeeds.append(changedSeed)
                    unchangedSeeds.remove(uc)
            currentRanges = []
            for us in unchangedSeeds: 
                currentRanges.append(us)
            for cs in changedSeeds: 
                currentRanges.append(cs) 
    for cr in currentRanges: 
        locations.append(cr[0])   


locations.sort()

print(locations[0])



# right: 51399228


