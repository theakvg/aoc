f = open("input2.txt", "r")
inputList = []
for l in f: 
    inputList.append(l)

red = 12
green = 13
blue = 14
sumGames = 0
count = 0
for line in inputList:
    goodGame = True
    colonSplit = line.split(": ")
    currentGame = colonSplit[0].split(" ")[1]
    rounds = colonSplit[1].split("; ")
    for r in rounds: 
        sets = r.split(", ")
        for s in sets: 
            cubes = s.split(" ")
            match cubes[1].strip(): 
                case "red": 
                    if int(cubes[0]) > red: 
                        goodGame = False
                case "blue": 
                    if int(cubes[0]) > blue: 
                        goodGame = False
                case "green": 
                    if int(cubes[0]) > green: 
                        goodGame = False
    if goodGame: 
        count += 1
        sumGames += int(currentGame)
print(count)
print(sumGames)

# answere: 2176
