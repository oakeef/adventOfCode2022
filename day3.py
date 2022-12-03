lowerCaseOffset = 96
upperCaseOffset = 38

#part1
backpackItems = []

with open('day3input.txt') as backpacks:
    for item in backpacks:
        strippedItem = item.strip()

        middle = int(len(strippedItem)/2)

        firstItem = strippedItem[0:middle]
        secondItem = strippedItem[middle:]
        
        backpackItems.append([firstItem,secondItem])
        
sameItems = []

for items in backpackItems:
    sameItem = ""
    for i in range(len(items[0])):
        if sameItem != "": break
        for j in range(len(items[1])):
            if items[0][i] == items[1][j]:
                sameItem = items[0][i]
                sameItems.append(sameItem)
                break

sumOfItemsPriority = 0

for value in sameItems:
    if value.isupper():
        sumOfItemsPriority += ord(value) - upperCaseOffset
    else:
        sumOfItemsPriority += ord(value) - lowerCaseOffset

print(sumOfItemsPriority)

# part 2
backPackArray = []
elvesGroups = []

with open('day3input.txt') as backpacks:
    for item in backpacks:
        backPackArray.append(item.strip())
    
for index in range(0, len(backPackArray), 3):
    elvesGroups.append([backPackArray[index].strip(), backPackArray[index + 1].strip(), backPackArray[index + 2].strip()])

badges = []

for group in elvesGroups:
    pack1 = group[0]
    pack2 = group[1]
    pack3 = group[2]
    for index in range(len(pack1)):
        item = pack1[index]
        if pack2.find(item) != -1 and pack3.find(item) != -1:
            badges.append(item)
            break

sumOfBadges = 0

for value in badges:
    if value.isupper():
        sumOfBadges += ord(value) - upperCaseOffset
    else:
        sumOfBadges += ord(value) - lowerCaseOffset

print(sumOfBadges)