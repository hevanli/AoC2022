f = open("day3input.txt", "r")
sum = 0
lines = f.readlines()
lines = [line[:-1] for line in lines]

sum = 0
for i in range(len(lines)//3):
    set1, set2 = set(), set()
    for char in lines[i*3]:
        set1.add(char)
    for char in lines[i*3+1]:
        set2.add(char)
    for char in lines[i*3+2]:
        if char in set1 and char in set2:
            if ord(char) >= 97 and ord(char) <= 122:
                sum += ord(char) - 96
            elif ord(char) >= 65 and ord(char) <= 90:
                sum += ord(char) - 38
            break
print(sum)
f.close()
