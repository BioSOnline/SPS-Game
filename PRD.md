# Rock Paper Scissors Upgrade PRD

## 1. Product Summary

Turn the existing single-round Rock Paper Scissors game into a replayable arcade match with selectable difficulty, a clear first-to-target win condition, and lightweight local statistics. The command-line and Tkinter versions should share the same rules so they behave consistently.

## 2. Goals

- Let a player choose a match target: first to 1, 3, or 5 round wins.
- Offer Easy, Medium, and Hard computer behavior.
- Show the current round score and announce the match winner when the target is reached.
- Track total rounds, wins, losses, ties, win rate, and best streak during the session.
- Persist aggregate statistics locally in `rps_stats.json` without requiring a database or network access.
- Preserve the existing classic Rock, Paper, Scissors rules and CLI entry point.

## 3. Non-goals

- Online multiplayer, accounts, networking, or matchmaking.
- Sound files or external assets.
- Changing the game to Rock Paper Scissors Lizard Spock.

## 4. User Stories

- As a player, I can select a difficulty before starting so the computer challenge matches my preference.
- As a player, I can select a match target so I know when the game ends.
- As a player, I can see both the round result and the match score after every move.
- As a player, I can reset the current match without losing my all-time session statistics.
- As a player, I can see my performance statistics and resume playing later.

## 5. Functional Requirements

### Match flow

1. A new match starts at 0-0 with the selected difficulty and target.
2. Each valid move produces exactly one computer move and one round result.
3. Ties do not increase either match score and do not end a match.
4. The first player to reach the target wins the match.
5. After match completion, move controls are disabled until a new match is started.
6. Starting a new match resets match score and streak but keeps aggregate statistics.

### Difficulty

- **Easy:** random computer move.
- **Medium:** 60% random move, 40% counter to the player's previous move.
- **Hard:** 70% counter to the player's most frequent move in the current match, otherwise random.
- On the first round, Medium and Hard fall back to random behavior.

### Statistics

Track and display total rounds, player wins, computer wins, ties, win rate, and best win streak. Save these aggregate values to `rps_stats.json` after each completed round. If the file is missing or invalid, start with zeroed statistics.

## 6. GUI Requirements

- Add compact controls for difficulty and match target.
- Display match score separately from all-time statistics.
- Display the current match status and final winner.
- Provide New Match, Reset Stats, and Quit actions.
- Keep the existing retro visual language and avoid external dependencies.

## 7. CLI Requirements

- Prompt for difficulty and match target at startup.
- Show match score, round result, and statistics after each round.
- Accept `new` to start a new match and `quit`/`q` to exit.
- Continue accepting `r`, `p`, and `s` aliases.

## 8. Acceptance Criteria

- The same move combinations return the same winner in both interfaces.
- All three difficulties return valid moves and do not crash when no history exists.
- A target of 1 ends after one non-tied round; ties do not end the match.
- Statistics survive a new process through `rps_stats.json`.
- GUI module can be imported without starting a window.
- CLI and engine compile successfully with Python 3.
