f = open("input2.txt", "r")
inputList = []
for l in f: 
    inputList.append(l)

red = 12
green = 13
blue = 14
sumGames = 0

for line in inputList:
    goodGame = True
    colonSplit = line.split(": ")
    currentGame = colonSplit[0].split(" ")[1]
    rounds = colonSplit[1].split("; ")
    currentRed = 0
    currentGreen = 0
    currentBlue = 0
    for r in rounds: 
        sets = r.split(", ")
        for s in sets: 
            cubes = s.split(" ")
            match cubes[1].strip(): 
                case "red": 
                    if int(cubes[0]) > currentRed: 
                        currentRed = int(cubes[0])
                case "blue": 
                    if int(cubes[0]) > currentBlue: 
                        currentBlue = int(cubes[0])
                case "green": 
                    if int(cubes[0]) > currentGreen: 
                        currentGreen = int(cubes[0])
    
    sumGames += (currentRed*currentGreen*currentBlue)

print(sumGames)

# answere: 63700
