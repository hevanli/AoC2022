# read input
file = open("day6input.txt", "r")
datastream = file.readline().strip()

buffer = []
for i, char in enumerate(datastream):
    if len(buffer) == 14:
        buffer.pop(0)
    unique = (char not in buffer) and (len(set(buffer)) == len(buffer))
    bufferFull = len(buffer) == 13
    if unique and bufferFull:
        print(i + 1)
        break
    buffer.append(char)

file.close()

