f = open("input1.txt", "r")
inputList = []
for l in f: 
    inputList.append(l)
sum = 0
for line in inputList: 
    currentNumber = []
    for x in line: 
        if x.isdigit():
            currentNumber.append(x) 
            
    number = ''.join([currentNumber[0], currentNumber[-1]])
    sum += int(number)

print(sum)


# answer: 57346