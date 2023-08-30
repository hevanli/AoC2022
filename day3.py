with open("day3input.txt", "r") as f:
    sum = 0
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    for line in lines:
        part1 = line[0:len(line)//2]
        part2 = line[len(line)//2:]
        charSet = set()
        for char in part1:
            charSet.add(char)
        for char in part2:
            if char in charSet:
                if ord(char) >= 97 and ord(char) <= 122:
                    sum += ord(char) - 96
                elif ord(char) >= 65 and ord(char) <= 90:
                    sum += ord(char) - 38
                break
    print(sum)
                    



