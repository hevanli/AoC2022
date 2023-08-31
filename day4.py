f = open("day4input.txt", "r")
fileread = f.read()
lines = fileread.splitlines()

data = [[list(map(int, pair.split('-'))) for pair in line.split(',')] for line in lines]

count = 0
for pairs in data:
    firstInSecond = pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]
    secondInFirst = pairs[1][0] >= pairs[0][0] and pairs[1][1] <= pairs[0][1]
    if firstInSecond or secondInFirst:
        count += 1
print(count)
f.close()
