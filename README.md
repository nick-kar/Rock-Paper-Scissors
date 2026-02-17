This project was completed as part of the freeCodeCamp – Machine Learning with Python Certification.

The objective of this challenge was to build a Rock Paper Scissors AI that wins at least 60% of games against four different opponent bots over 1000 matches each.

Project Requirements

Implement a player(prev_play) function inside RPS.py

The function must return "R", "P", or "S"

Win at least 60% of games against:

Abbey

Kris

Mrugesh

Quincy

Do not modify RPS_game.py

Strategy Overview

To consistently defeat all four bots, this solution combines multiple adaptive strategies:

Reactive Pattern Detection
Detects opponents that follow predictable counter-move patterns and exploits them.

Variable-Length Markov Prediction
Uses sequence pattern recognition (length 2–4) to predict the opponent’s next move based on historical data.

Weighted Recency Model
Applies exponential decay to prioritize recent opponent moves, improving adaptability.

Frequency-Based Bias Adjustment
Adds a strategic counter to the opponent’s most frequent recent move to stabilize win rate against semi-random strategies.

Results (1000 Games Per Opponent)

Abbey: ~60%+
Kris: ~90%+
Mrugesh: ~80%+
Quincy: ~60%+

All required tests pass successfully.

How to Run

Clone the repository:

git clone https://github.com/nick-kar/rock-paper-scissors.git

cd rock-paper-scissors
python main.py

To manually test against a specific bot:

play(player, quincy, 1000, verbose=True)

Project Structure

RPS.py — AI logic (main solution)
RPS_game.py — Game engine (provided by freeCodeCamp)
main.py — Test runner
test_module.py — Unit tests

Author

GitHub: https://github.com/nick-kar
