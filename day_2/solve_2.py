# A = Rock
# B = Paper
# C = Scissors
# X = Loss
# Y = Draw
# Z = Win
def play_round(opponent, player):
    print(f"Received {opponent} and {player}")
    score = 0
    player_win = False
    draw = False

    if opponent == "A":
        if player == "X": # Loss (Scissors)
            score += 3
        elif player == "Y": # Draw (Rock)
            draw = True
            score += 1
        else: # Z - Win (Paper)
            player_win = True
            score += 2

    elif opponent == "B":
        if player == "X": # Loss (Rock)
            score += 1
        elif player == "Y": # Draw (Paper)
            score += 2
            draw = True
        else: # Z - Win (Scissors)
            player_win = True
            score += 3
        
    else: ## opponent = C
        if player == "X": # Loss (Paper)
            score += 2
        elif player == "Y": # Draw (Scissors)
            draw = True
            score += 3
        else: # Z - Win (Rock)
            player_win = True
            score += 1
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