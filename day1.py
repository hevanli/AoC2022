with open("day1input.txt", "r") as f:
    elves = [0]
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            elves.append(0)
        else:
            elves[len(elves)-1] += int(line)

    total = 0
    for i in range(3):
        total += max(elves)
        elves.remove(max(elves))

    print(total)
