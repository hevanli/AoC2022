# read in input
file = open("day5input.txt", "r")
lines = file.read().splitlines()

# determine how many stacks there are
numStacks = (len(lines[0]) + 1) // 4

# create stacks
stacks = [[] for i in range(numStacks)]
for line in lines:
    if line[1].isnumeric():
        break
    for i in range(numStacks):
        if line[i * 4 + 1] != ' ':
            stacks[i].append(line[i * 4 + 1])

# instructions -> list
instructions = []
for line in lines:
    if not line.startswith("move"):
        continue

    listToAdd = []
    for i in line.split():
        if i.isnumeric():
            listToAdd.append(int(i))
    instructions.append(listToAdd)

# simulate instructions
for i in instructions:
    howMany = i[0]
    stack1 = i[1] - 1
    stack2 = i[2] - 1
    toMove = stacks[stack1][:howMany]
    toMove.reverse()
    stacks[stack1] = stacks[stack1][howMany:]
    stacks[stack2] = toMove + stacks[stack2]

# accumulate top boxes
output = ""
for stack in stacks:
    output += str(stack[0])
print(output)

file.close()
