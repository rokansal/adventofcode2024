import math

#part 1
first = []
second = []
with open("dec1/input.txt") as file:
    for line in file:
        x, y = line.split()
        first.append(int(x))
        second.append(int(y))

first.sort()
second.sort()
sum = 0
for i in range(len(first)):
    sum += abs(first[i] - second[i])
    
print(sum)

#part 2
sum = 0
left = 0
right = 0
while (left < len(first) and right < len(second)):
    if first[left] == second[right]:
        num = first[left]
        subsum = 0
        while (right < len(second) and second[right] == num):
            right += 1
            subsum += num
        while (left < len(first) and first[left] == num):
            left += 1
            sum += subsum
    elif first[left] < second[right]:
        left += 1
    else:
        right += 1
print(sum)