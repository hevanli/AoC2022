with open("day2input.txt", "r") as f:
    score = 0
    lines = f.readlines()
    for line in lines:
        opp = line[0]
        own = line[2]
        if own == 'X':
            if opp == 'A':
                score += 3
            elif opp == 'B':
                score += 1
            elif opp == 'C':
                score += 2
        elif own == 'Y':
            score += 3
            if opp == 'A':
                score += 1
            elif opp == 'B':
                score += 2
            elif opp == 'C':
                score += 3
        elif own == 'Z':
            score += 6
            if opp == 'A':
                score += 2
            elif opp == 'B':
                score += 3
            elif opp == 'C':
                score += 1
    print(score)

