
elfPairs = []

with open('day4input.txt') as pairs:
    for elf in pairs:
        elfPair = elf.strip().split(',')
        elfPairNums = []
        for elf in elfPair:
            splitElf = elf.split('-')
            for index, num in enumerate(splitElf):
                splitElf[index] = int(num)
            elfPairNums.append(splitElf)
        elfPairs.append(elfPairNums)

sameRange = 0

for pair in elfPairs:
    startElf1 = pair[0][0]
    endElf1 = pair[0][1]
    startElf2 = pair[1][0]
    endElf2 = pair[1][1]

    if startElf1 <= endElf2 and startElf1 >= startElf2 and endElf1 <= endElf2 and endElf1 >= startElf2 or startElf2 <= endElf1 and startElf2 >= startElf1 and endElf2 <= endElf1 and endElf2 >= startElf1:
        sameRange +=1
              
print(sameRange)