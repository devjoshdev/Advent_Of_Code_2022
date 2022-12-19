# A = Rock
# B = Paper
# C = Scissors
# X = Rock
# Y = Paper
# Z = Scissors
def play_round(opponent, player):
    print(f"Received {opponent} and {player}")
    score = 0
    player_win = False
    draw = False

    if opponent == "A":
        if player == "X": # Rock vs Rock (Draw)
            draw = True
            score += 1
        elif player == "Y": # Paper vs Rock (Win)
            score += 2
            player_win = True
        else: # Z - Scissors vs Rock (Loss)
            score += 3

    elif opponent == "B":
        if player == "X": # Rock vs Paper (Loss)
            score += 1
        elif player == "Y": # Paper vs Paper (Draw)
            score += 2
            draw = True
        else: # Z - Scissors vs Paper (Win)
            player_win = True
            score += 3
        
    else: ## opponent = C
        if player == "X": # Rock vs Scissors (Win)
            score += 1
            player_win = True
        elif player == "Y": # Paper vs Scissors (Loss)
            score += 2
        else: # Z - Scissors vs Scissors (Draw)
            draw = True
            score += 3
    if draw:
        print(f"Player played {player}, Opponent played {opponent}, current score is {score}")
        return score + 3
    if player_win:
        print(f"Player played {player}, Opponent played {opponent}, current score is {score}")
        return score + 6
    print(f"Player played {player}, Opponent played {opponent}, current score is {score}")
    return score


total_score = 0
with open("input.txt", 'r') as f:
    for line in f:
        inputs = line.split(" ")
        opp, player = inputs[0].strip(), inputs[1].strip()
        total_score += play_round(opp, player)
        print(f"Total Score Is: {total_score}")
