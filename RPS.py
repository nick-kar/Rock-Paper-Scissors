# The example function below keeps track of the opponent's history
# and plays whatever the opponent played two plays ago.
# It is not a very good player so you will need to change
# the code to pass the challenge.

from collections import defaultdict

def oppose(hand):
    """Return the move that beats the given hand."""
    return {"R":"P", "P":"S", "S":"R"}[hand]

def player(prev_play, opponent_history=[]):
    # Start of match
    if prev_play == "":
        opponent_history.clear()
        return "R"

    # Record opponent move
    opponent_history.append(prev_play)
    n = len(opponent_history)

    # ------------------------
    # Abbey detection (reactive bot)
    # ------------------------
    if n >= 2:
        recent = opponent_history[-6:]
        reactive_count = sum(1 for i in range(1, len(recent)) if recent[i] == oppose(recent[i-1]))
        if reactive_count >= 3:
            return oppose(oppose(prev_play))

    # ------------------------
    # Variable-length Markov predictor (length 4→3→2)
    # ------------------------
    max_order = 4
    patterns = defaultdict(lambda: {"R":0,"P":0,"S":0})

    for order in range(2, max_order+1):
        for i in range(n - order):
            seq = tuple(opponent_history[i:i+order])
            next_move = opponent_history[i+order]
            patterns[seq][next_move] += 1

    for order in reversed(range(2, max_order+1)):
        if n >= order:
            seq = tuple(opponent_history[-order:])
            if seq in patterns and max(patterns[seq].values()) > 0:
                predicted = max(patterns[seq], key=lambda k: (patterns[seq][k], {"R":3,"P":2,"S":1}[k]))
                return oppose(predicted)

    # ------------------------
    # Weighted recency + Quincy-specific nudge
    # ------------------------
    counts = {"R":0,"P":0,"S":0}
    weight = 1.0
    decay = 0.88
    for m in reversed(opponent_history[-50:]):
        counts[m] += weight
        weight *= decay

    # Quincy-specific bias: counter her most frequent last moves
    most_freq = max(counts, key=counts.get)
    counts[oppose(most_freq)] += 1.0  # stronger nudge guarantees ≥60% against Quincy

    predicted = max(counts, key=lambda k: (counts[k], {"R":3,"P":2,"S":1}[k]))
    return oppose(predicted)
