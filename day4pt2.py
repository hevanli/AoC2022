file = open("day4input.txt", "r")
lines = file.read().splitlines()
data = [[list(map(int, pair.split("-"))) for pair in line.split(",")] for line in lines]

count = 0
for pair in data:
    a = pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]
    b = pair[0][1] >= pair[1][0] and pair[0][1] <= pair[1][1]
    c = pair[1][0] >= pair[0][0] and pair[1][0] <= pair[0][1]
    d = pair[1][1] >= pair[0][0] and pair[1][1] <= pair[0][1]
    if a or b or c or d:
        count += 1
print(count)

file.close()
