f = open("input5.txt", "r")
inputList = []
for l in f: 
    l = l.strip()
    if len(l) != 0:
        inputList.append(l)

seeds = []
ranges = []
seeds = inputList[0].split(":")[1].split(" ")
seeds.remove("")

for index in range(1, len(inputList)-1): 
    if ":" in inputList[index]: 
        ranges.append([])
        index +=1
        while index < len(inputList) and ":" not in inputList[index]: 
            ranges[-1].append(inputList[index].split(" "))
            index += 1

locations = []

for seed in seeds:
    nextRange = int(seed) 
    for range in ranges: 
        for line in range: 
            if nextRange >= int(line[1]) and nextRange < int(line[1])+int(line[2]): 
                nextRange = int(line[0]) + (nextRange - int(line[1]))
                break
                
    locations.append(nextRange)
locations.sort()
print(locations[0])


# riktig: 535088217