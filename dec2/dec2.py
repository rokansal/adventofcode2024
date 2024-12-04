import math
count = 0
i = 0
lines = []
with open("dec2/input.txt") as file:
    for line in file:
        lines.append([])
        for thing in line.split():
            lines[-1].append(int(thing))

for line in lines:
    inc = True
    ok = True
    idk = True
    count += 1
    if line[0] > line[1]:
        inc = False
    for i in range(len(line) - 1):
        if abs(line[i] - line[i+1]) < 1 or abs(line[i] - line[i+1]) > 3:
            if not ok:
                count -= 1
                idk = False
                break
            ok = False
        elif inc:  
            if (line[i] >= line[i+1]):
                if not ok:
                    count -= 1
                    idk = False
                    break
                ok = False
        else:
            if (line[i] <= line[i+1]):
                if not ok:
                    count -= 1
                    idk = False
                    break
                ok = False
    inc = True
    ok = True
    if not idk:
        if line[1] > line[2]:
            inc = False
        for i in range(1, len(line) - 1):
            if abs(line[i] - line[i+1]) < 1 or abs(line[i] - line[i+1]) > 3:
                ok = False
                break
            elif inc:  
                if (line[i] >= line[i+1]):
                    ok = False
                    break
            else:
                if (line[i] <= line[i+1]):
                    ok = False
                    break
        if ok:
            count += 1
print(count)