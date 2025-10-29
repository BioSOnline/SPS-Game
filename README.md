Rock Paper Scissors
===================

Two versions of Rock Paper Scissors game: command-line and GUI.

Version 1: Command-Line (rps_game.py)
--------------------------------------

Interactive terminal-based game.

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
- Type `rock`, `paper`, or `scissors` (or `r`, `p`, `s`) when prompted.
- Type `quit` or `q` to exit the game and see the final score.
- The game prints who won each round and maintains a running score.


Version 2: GUI (rps_game_gui.py)
---------------------------------

Visual game with buttons and colorful interface using Tkinter.

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
- Click on Rock 🪨, Paper 📄, or Scissors ✂️ buttons to play.
- Scores update automatically after each round.
- Click "Reset Game" to start over.
- Click "Quit" to exit the application.

Notes
-----
- Requires Python 3.6+ (f-strings used).
- If `python` isn't in PATH, run using the full path to your Python executable.
