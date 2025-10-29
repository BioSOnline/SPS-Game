#!/usr/bin/env python3
"""Simple interactive Rock Paper Scissors game.

Player types 'rock', 'paper', 'scissors' (or r/p/s). Type 'quit' to stop.
The computer randomly selects its move. The script shows round winners and
maintains a running score.
"""
import random
import sys

VALID = {
    'rock': 'rock', 'r': 'rock',
    'paper': 'paper', 'p': 'paper',
    'scissors': 'scissors', 's': 'scissors',
}

def determine_winner(player: str, comp: str) -> str:
    """Return 'player', 'computer', or 'tie'."""
    if player == comp:
        return 'tie'
    wins = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if wins[player] == comp:
        return 'player'
    return 'computer'


def main() -> None:
    player_score = 0
    comp_score = 0

    print("Rock Paper Scissors — type 'rock', 'paper', 'scissors' (or r/p/s). Type 'quit' to exit.")

    try:
        while True:
            choice = input("Your move (r/p/s): ").strip().lower()
            if not choice:
                # empty input, prompt again
                continue
            if choice in ('quit', 'q'):
                break
            if choice not in VALID:
                print("Invalid input. Please type 'rock', 'paper', or 'scissors' (or r/p/s), or 'quit' to exit.")
                continue

            player_move = VALID[choice]
            comp_move = random.choice(['rock', 'paper', 'scissors'])
            result = determine_winner(player_move, comp_move)

            if result == 'tie':
                print(f"Both chose {player_move}. It's a tie.")
            elif result == 'player':
                player_score += 1
                print(f"You chose {player_move}, computer chose {comp_move}. You win this round!")
            else:
                comp_score += 1
                print(f"You chose {player_move}, computer chose {comp_move}. Computer wins this round.")

            print(f"Score — You: {player_score}  Computer: {comp_score}\n")

    except (KeyboardInterrupt, EOFError):
        # Graceful exit on Ctrl-C / EOF
        print("\nExiting game...")

    # Final summary
    print(f"Final score — You: {player_score}  Computer: {comp_score}")
    if player_score > comp_score:
        print("You won the game!")
    elif comp_score > player_score:
        print("Computer won the game!")
    else:
        print("The game is a tie.")


if __name__ == '__main__':
    main()
