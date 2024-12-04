answer = 0
read = True
text = ""
with open("dec3/input.txt") as file:
    for line in file:
        for char in line:
            text += char
i = 0
while (i < len(text)):
    if (text[i:i+4] == "do()"):
        read = True
        i += 3
    elif (text[i:i+7] == "don't()"):
        read = False
        i += 6
    elif (read and text[i] == 'm'):
        i += 1
        if (i < len(text) and text[i] == 'u'):
            i += 1
            if (i < len(text) and text[i] == 'l'):
                i += 1
                if (i < len(text) and text[i] == '('):
                    i += 1
                    n = ""
                    if (ord(text[i]) >= 48 and ord(text[i]) <= 57):
                        n += text[i]
                        i += 1
                        valid = False
                        if (text[i] == ","):
                            valid = True
                        elif (ord(text[i]) >= 48 and ord(text[i]) <= 57):
                            n += text[i]
                            i += 1
                            if (text[i] == ","):
                                valid = True
                            elif (ord(text[i]) >= 48 and ord(text[i]) <= 57):
                                n += text[i]
                                i += 1
                                if (text[i] == ","):
                                    valid = True
                        if valid:
                            i += 1
                            valid = False
                            num1 = int(n)
                            n = ""
                            if (ord(text[i]) >= 48 and ord(text[i]) <= 57):
                                n += text[i]
                                i += 1
                                valid = False
                                if (text[i] == ")"):
                                    valid = True
                                elif (ord(text[i]) >= 48 and ord(text[i]) <= 57):
                                    n += text[i]
                                    i += 1
                                    if (text[i] == ")"):
                                        valid = True
                                    elif (ord(text[i]) >= 48 and ord(text[i]) <= 57):
                                        n += text[i]
                                        i += 1
                                        if (text[i] == ")"):
                                            valid = True
                                if valid:
                                    num2 = int(n)
                                    p = num1*num2
                                    print(num1, num2)
                                    answer += p
    i += 1
print(answer)