#!/usr/bin/env python3
"""Rock Paper Scissors arcade interface."""
import tkinter as tk
from tkinter import font, messagebox, ttk

from game_engine import CHOICES, DIFFICULTIES, RPSGame, StatsStore, TARGETS


class RPSGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ROCK PAPER SCISSORS")
        self.root.geometry("650x760")
        self.root.resizable(False, False)
        self.colors = {"bg": "#111827", "panel": "#1f2937", "blue": "#38bdf8", "text": "#f8fafc", "muted": "#94a3b8", "pink": "#fb7185", "green": "#4ade80", "yellow": "#facc15", "button": "#334155"}
        self.root.configure(bg=self.colors["bg"])
        self.title_font = font.Font(family="Courier New", size=22, weight="bold")
        self.heading_font = font.Font(family="Courier New", size=14, weight="bold")
        self.body_font = font.Font(family="Courier New", size=11)
        self.game = RPSGame()
        self.store = StatsStore()
        self.difficulty = tk.StringVar(value="Easy")
        self.target = tk.IntVar(value=3)
        self.setup_ui()
        self.update_display()
        self.root.bind("<KeyPress-r>", lambda event: self.play_round("Rock"))
        self.root.bind("<KeyPress-p>", lambda event: self.play_round("Paper"))
        self.root.bind("<KeyPress-s>", lambda event: self.play_round("Scissors"))

    def setup_ui(self):
        tk.Frame(self.root, bg=self.colors["pink"], height=6).pack(fill=tk.X)
        header = tk.Frame(self.root, bg=self.colors["panel"], padx=20, pady=14)
        header.pack(fill=tk.X, padx=22, pady=(18, 10))
        tk.Label(header, text="ROCK PAPER SCISSORS", bg=self.colors["panel"], fg=self.colors["pink"], font=self.title_font).pack()
        tk.Label(header, text="ARCADE MATCH", bg=self.colors["panel"], fg=self.colors["blue"], font=self.body_font).pack(pady=(4, 0))

        settings = tk.Frame(self.root, bg=self.colors["panel"], padx=14, pady=10)
        settings.pack(fill=tk.X, padx=22, pady=8)
        self._label(settings, "DIFFICULTY").grid(row=0, column=0, padx=8, sticky="w")
        ttk.Combobox(settings, textvariable=self.difficulty, values=DIFFICULTIES, state="readonly", width=10).grid(row=0, column=1, padx=8)
        self._label(settings, "FIRST TO").grid(row=0, column=2, padx=(24, 8), sticky="w")
        ttk.Combobox(settings, textvariable=self.target, values=TARGETS, state="readonly", width=5).grid(row=0, column=3, padx=8)
        tk.Button(settings, text="NEW MATCH", command=self.new_match, font=self.body_font, bg=self.colors["blue"], fg="#082f49", relief=tk.FLAT, padx=10, pady=5).grid(row=0, column=4, padx=(22, 4))

        score = tk.Frame(self.root, bg=self.colors["bg"])
        score.pack(pady=12)
        self.player_score = self._score_box(score, "PLAYER", self.colors["green"], 0)
        tk.Label(score, text="VS", bg=self.colors["bg"], fg=self.colors["pink"], font=self.heading_font).grid(row=0, column=1, padx=20)
        self.computer_score = self._score_box(score, "CPU", self.colors["pink"], 2)

        choices = tk.Frame(self.root, bg=self.colors["bg"])
        choices.pack(pady=8)
        self.player_choice = self._choice_box(choices, "YOUR MOVE", self.colors["green"], 0)
        self.computer_choice = self._choice_box(choices, "CPU MOVE", self.colors["pink"], 1)
        self.result_label = tk.Label(self.root, text="MAKE YOUR CHOICE", bg=self.colors["panel"], fg=self.colors["yellow"], font=self.heading_font, padx=30, pady=12)
        self.result_label.pack(fill=tk.X, padx=50, pady=14)
        self.status_label = tk.Label(self.root, text="", bg=self.colors["bg"], fg=self.colors["muted"], font=self.body_font)
        self.status_label.pack()

        moves = tk.Frame(self.root, bg=self.colors["bg"])
        moves.pack(pady=14)
        self.move_buttons = []
        move_colors = [self.colors["green"], self.colors["yellow"], self.colors["blue"]]
        for index, choice in enumerate(CHOICES):
            button = tk.Button(moves, text=choice.upper(), command=lambda move=choice: self.play_round(move), font=("Courier New", 11, "bold"), bg=move_colors[index], fg="#111827", activebackground=self.colors["text"], relief=tk.FLAT, width=13, pady=12)
            button.grid(row=0, column=index, padx=6)
            self.move_buttons.append(button)

        stats = tk.Frame(self.root, bg=self.colors["panel"], padx=15, pady=10)
        stats.pack(fill=tk.X, padx=22, pady=8)
        self.stats_label = tk.Label(stats, text="", bg=self.colors["panel"], fg=self.colors["muted"], font=("Courier New", 10))
        self.stats_label.pack()
        controls = tk.Frame(self.root, bg=self.colors["bg"])
        controls.pack(pady=10)
        tk.Button(controls, text="RESET STATS", command=self.reset_stats, font=self.body_font, bg=self.colors["yellow"], fg="#422006", relief=tk.FLAT, padx=12, pady=6).grid(row=0, column=0, padx=8)
        tk.Button(controls, text="QUIT", command=self.root.destroy, font=self.body_font, bg=self.colors["pink"], fg="#450a0a", relief=tk.FLAT, padx=25, pady=6).grid(row=0, column=1, padx=8)

    def _label(self, parent, text):
        return tk.Label(parent, text=text, bg=self.colors["panel"], fg=self.colors["text"], font=self.body_font)

    def _score_box(self, parent, title, color, column):
        box = tk.Frame(parent, bg=self.colors["panel"], padx=24, pady=8)
        box.grid(row=0, column=column)
        tk.Label(box, text=title, bg=self.colors["panel"], fg=color, font=self.body_font).pack()
        score = tk.Label(box, text="0", bg=self.colors["panel"], fg=self.colors["text"], font=self.title_font, width=4)
        score.pack()
        return score

    def _choice_box(self, parent, title, color, column):
        box = tk.Frame(parent, bg=self.colors["panel"], padx=16, pady=8)
        box.grid(row=0, column=column, padx=8)
        tk.Label(box, text=title, bg=self.colors["panel"], fg=color, font=self.body_font).pack()
        choice = tk.Label(box, text="???", bg=self.colors["panel"], fg=self.colors["text"], font=self.heading_font, width=13, pady=9)
        choice.pack()
        return choice

    def play_round(self, choice):
        if self.game.finished:
            return
        result = self.game.play_round(choice)
        self.player_choice.config(text=result["player"].upper())
        self.computer_choice.config(text=result["computer"].upper())
        messages = {"player": ("PLAYER WINS THE ROUND", self.colors["green"]), "computer": ("CPU WINS THE ROUND", self.colors["pink"]), "tie": ("DRAW - TRY AGAIN", self.colors["yellow"])}
        message, color = messages[result["result"]]
        self.result_label.config(text=message, fg=color)
        if result["match_winner"]:
            winner_color = self.colors["green"] if result["match_winner"] == "player" else self.colors["pink"]
            self.result_label.config(text=f"{result['match_winner'].upper()} WINS THE MATCH", fg=winner_color)
        self.update_display()

    def update_display(self):
        self.player_score.config(text=str(self.game.player_score))
        self.computer_score.config(text=str(self.game.computer_score))
        stats = self.game.stats
        self.stats_label.config(text=f"ROUNDS {stats['rounds']}   WINS {stats['wins']}   LOSSES {stats['losses']}   TIES {stats['ties']}   WIN RATE {self.game.win_rate:.1f}%   BEST STREAK {stats['best_streak']}")
        status = "Choose NEW MATCH to play again." if self.game.finished else f"First to {self.game.target}  |  {self.game.difficulty} mode  |  Match score {self.game.player_score}-{self.game.computer_score}"
        self.status_label.config(text=status)
        state = tk.DISABLED if self.game.finished else tk.NORMAL
        for button in self.move_buttons:
            button.config(state=state)

    def new_match(self):
        self.game.start_match(self.difficulty.get(), int(self.target.get()))
        self.player_choice.config(text="???")
        self.computer_choice.config(text="???")
        self.result_label.config(text="MAKE YOUR CHOICE", fg=self.colors["yellow"])
        self.update_display()

    def reset_stats(self):
        if messagebox.askyesno("Reset statistics", "Delete all saved statistics?"):
            self.game.stats = self.store.reset()
            self.update_display()


def main():
    root = tk.Tk()
    RPSGameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
