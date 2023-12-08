f = open("input8.txt", "r")
inputList = []

for l in f: 
    l = l.strip()
    if len(l) != 0:
        inputList.append(l)

instuctions = inputList[0]



del inputList[0]
elements = {}
currentEls = []
for input in inputList: 
    tempEl = input.split(" = ")
    values = tempEl[1].strip("()").split(", ")
    elements[tempEl[0]] = values
    if tempEl[0][2] == 'A': 
        currentEls.append(tempEl[0])

goal = "Z"
num = 0
sum = 1
for current in range(0, len(currentEls)):
    for i in range(0, 1000): 
        for inst in instuctions: 
            check = True
            num += 1
            if currentEls[current][2] == goal: 
                break
            if inst == "L": 
                nextEl = elements[currentEls[current]][0]
            elif inst == "R": 
                nextEl = elements[currentEls[current]][1]
            currentEls[current] = nextEl
        if currentEls[current][2] == goal: 
            break
    currentEls[current] = num
    num = 0
currentEls.sort()

def lcm(nums):
    res = 1
    for i in nums:
        res = (res * i) // gcd(res, i)
    return res
    
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
    
print(lcm(currentEls))

# riktig: 16563603485021

