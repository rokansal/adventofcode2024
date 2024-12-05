rules = set()
counter = 0
counter2 = 0
with open("dec5/input.txt") as file:
    con = True
    for line in file:
        if con:
            if len(line) < 3:
                con = False
                continue
            rules.add(line[:2] + line[3:5])
        else:
            correct = True
            nums = line.split(',')
            nums[-1] = nums[-1][:2]
            for i in range(len(nums) - 1):
                for j in range(i+1, len(nums)):
                    if nums[j]+nums[i] in rules:
                        correct = False
            if correct:
                counter += int(nums[int(len(nums)/2)])
            else:
                for i in range(len(nums)):
                    swapped = False
                    for j in range(0, len(nums)-i-1):
                        if nums[j+1] + nums[j] in rules:
                            nums[j], nums[j+1] = nums[j+1], nums[j]
                            swapped = True
                    if (swapped == False):
                        break
                counter2 += int(nums[int(len(nums)/2)])

print(counter)
print(counter2)