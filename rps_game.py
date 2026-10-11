#!/usr/bin/env python3
"""Command-line interface for the upgraded Rock Paper Scissors game."""
from game_engine import CHOICES, DIFFICULTIES, TARGETS, RPSGame

VALID = {choice.lower(): choice for choice in CHOICES}
VALID.update({choice[0].lower(): choice for choice in CHOICES})


def main() -> None:
    print("=" * 50)
    print("ROCK PAPER SCISSORS: ARCADE MATCH")
    print("=" * 50)
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    print("Type 'rock', 'paper', or 'scissors' (or r/p/s). Type 'quit' to exit.")
    print("=" * 50)

    difficulty = input("Difficulty (Easy/Medium/Hard) [Easy]: ").strip().title() or "Easy"
    if difficulty not in DIFFICULTIES:
        difficulty = "Easy"
    target_text = input("Match target (1/3/5) [3]: ").strip() or "3"
    target = int(target_text) if target_text.isdigit() and int(target_text) in TARGETS else 3
    game = RPSGame(difficulty, target)
    print(f"\nMatch: first to {target} | Difficulty: {difficulty}")

    try:
        while True:
            choice = input("Your move (r/p/s): ").strip().lower()
            if not choice:
                # empty input, prompt again
                continue
            if choice in ('quit', 'q'):
                break
            if choice == 'new':
                game.start_match(difficulty, target)
                print("New match started.")
                continue
            if choice not in VALID:
                print("Invalid input. Please type 'rock', 'paper', or 'scissors' (or r/p/s), or 'quit' to exit.")
                continue

            if game.finished:
                print(f"Match over: {game.match_winner} won. Type 'new' to play again.")
                continue

            round_result = game.play_round(VALID[choice])
            player_move = round_result['player']
            comp_move = round_result['computer']
            result = round_result['result']

            if result == 'tie':
                print(f"Both chose {player_move}. It's a tie.")
            elif result == 'player':
                print(f"You chose {player_move}, computer chose {comp_move}. You win this round!")
            else:
                print(f"You chose {player_move}, computer chose {comp_move}. Computer wins this round.")

            print(f"Match score — You: {game.player_score}  Computer: {game.computer_score}")
            print(f"Stats — Wins: {game.stats['wins']}  Losses: {game.stats['losses']}  Ties: {game.stats['ties']}  Win rate: {game.win_rate:.1f}%")
            if game.finished:
                print(f"MATCH COMPLETE: {game.match_winner.upper()} wins! Type 'new' to play again.\n")

    except (KeyboardInterrupt, EOFError):
        # Graceful exit on Ctrl-C / EOF
        print("\nExiting game...")

    # Final summary
    print(f"Session stats — Wins: {game.stats['wins']}  Losses: {game.stats['losses']}  Ties: {game.stats['ties']}")


if __name__ == '__main__':
    main()
