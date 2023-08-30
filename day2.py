with open("day2input.txt", "r") as f:
    score = 0
    lines = f.readlines()
    for line in lines:
        opp = line[0]
        own = line[2]
        if own == 'X': # rock
            score += 1
            if opp == 'A':
                score += 3
            elif opp == 'C':
                score += 6
        elif own == 'Y': # paper
            score += 2
            if opp == 'A':
                score += 6
            elif opp == 'B':
                score += 3
        elif own == 'Z': # scissors
            score += 3
            if opp == 'B':
                score += 6
            elif opp == 'C':
                score += 3
    print(score)
