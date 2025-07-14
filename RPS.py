def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    N = 3
    if len(opponent_history) < N:
        return "R" 

    last_moves = "".join(opponent_history[-N:])
    patterns = {}
    for i in range(len(opponent_history) - N):
        pattern = "".join(opponent_history[i:i+N])
        next_move = opponent_history[i+N]
        if pattern not in patterns:
            patterns[pattern] = {"R": 0, "P": 0, "S": 0}
        patterns[pattern][next_move] += 1

    if last_moves in patterns:
        predicted = max(patterns[last_moves], key=patterns[last_moves].get)
    else:
        predicted = opponent_history[-1] 

    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted]
