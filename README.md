Rock Paper Scissors
===================

Two versions of an arcade-style Rock Paper Scissors game: command-line and GUI.

The game now includes first-to-1/3/5 matches, Easy/Medium/Hard computer difficulty,
win streaks, win rate, and local statistics saved in `rps_stats.json`.

Version 1: Command-Line (rps_game.py)
--------------------------------------

Interactive terminal-based game with match and difficulty selection.

**How to run (Windows PowerShell):**

1. Open PowerShell and change to the project directory:
   ```
   cd "C:\Users\ADNAN\Desktop\SPS Game"
   ```

2. Run the game with Python 3:
   ```
   python .\rps_game.py
   ```

**Usage:**
- Choose a difficulty and match target when prompted.
- Type `rock`, `paper`, or `scissors` (or `r`, `p`, `s`) to play.
- Type `new` to restart the current match, or `quit`/`q` to exit.
- Statistics are saved automatically between runs.


Version 2: GUI (rps_game_gui.py)
---------------------------------

Visual arcade game using Tkinter.

**How to run (Windows PowerShell):**

1. Open PowerShell and change to the project directory:
   ```
   cd "C:\Users\ADNAN\Desktop\SPS Game"
   ```

2. Run the GUI version:
   ```
   python .\rps_game_gui.py
   ```

**Usage:**
- Select difficulty and a first-to target, then click a move button.
- Use `NEW MATCH` to change settings and start a match.
- Use `RESET STATS` to clear saved aggregate statistics.
- Move buttons disable automatically when a match is complete.

Product requirements
--------------------

See [PRD.md](PRD.md) for the feature requirements and acceptance criteria used for this upgrade.

Notes
-----
- Requires Python 3.6+ and Tkinter for the GUI.
- If `python` isn't in PATH, run using the full path to your Python executable.
