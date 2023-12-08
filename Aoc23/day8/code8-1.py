f = open("input8.txt", "r")
inputList = []

for l in f: 
    l = l.strip()
    if len(l) != 0:
        inputList.append(l)

instuctions = inputList[0]


del inputList[0]
elements = {}
for input in inputList: 
    tempEl = input.split(" = ")
    values = tempEl[1].strip("()").split(", ")
    elements[tempEl[0]] = values

currentEl = "AAA"
goal = "ZZZ"
num = 0


for i in range(0, 150): 
    for inst in instuctions: 
        num += 1
        if currentEl == goal: 
            break
        if inst == "L": 
            nextEl = elements[currentEl][0]
        elif inst == "R": 
            nextEl = elements[currentEl][1]
        currentEl = nextEl
    if currentEl == goal: 
        break


print(num, currentEl)

# kanskje: 16897
