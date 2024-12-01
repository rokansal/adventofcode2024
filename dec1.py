import math
first = []
second = []
while (True):
    line = input()
    if line == "exit":
        break
    else:
        x, y = line.split()
        first.append(int(x))
        second.append(int(y))
first.sort()
second.sort()
sum = 0
for i in range(len(first)):
    sum += abs(first[i] - second[i])
    
print(sum)