"""Shared rules, match state, and local statistics for the RPS game."""
from __future__ import annotations

import json
import random
from collections import Counter
from pathlib import Path
from typing import Dict, Optional

CHOICES = ("Rock", "Paper", "Scissors")
DIFFICULTIES = ("Easy", "Medium", "Hard")
TARGETS = (1, 3, 5)
COUNTERS = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
WINS = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
DEFAULT_STATS = {
    "rounds": 0,
    "wins": 0,
    "losses": 0,
    "ties": 0,
    "best_streak": 0,
}


class StatsStore:
    """Read and write aggregate statistics without failing the game."""

    def __init__(self, path: Optional[Path] = None):
        self.path = path or Path(__file__).with_name("rps_stats.json")

    def load(self) -> Dict[str, int]:
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            return {key: int(data.get(key, 0)) for key in DEFAULT_STATS}
        except (OSError, ValueError, TypeError):
            return DEFAULT_STATS.copy()

    def save(self, stats: Dict[str, int]) -> None:
        try:
            self.path.write_text(json.dumps(stats, indent=2), encoding="utf-8")
        except OSError:
            pass

    def reset(self) -> Dict[str, int]:
        stats = DEFAULT_STATS.copy()
        self.save(stats)
        return stats


class RPSGame:
    """Manage one match and update aggregate statistics after each round."""

    def __init__(self, difficulty: str = "Easy", target: int = 3, store: Optional[StatsStore] = None):
        self.store = store or StatsStore()
        self.stats = self.store.load()
        self.start_match(difficulty, target)

    def start_match(self, difficulty: str = "Easy", target: int = 3) -> None:
        self.difficulty = difficulty if difficulty in DIFFICULTIES else "Easy"
        self.target = target if target in TARGETS else 3
        self.player_score = 0
        self.computer_score = 0
        self.current_streak = 0
        self.history = []
        self.finished = False
        self.match_winner = None

    def computer_move(self) -> str:
        if self.difficulty == "Easy" or not self.history:
            return random.choice(CHOICES)

        if self.difficulty == "Medium":
            if random.random() < 0.4:
                return COUNTERS[self.history[-1]]
            return random.choice(CHOICES)

        most_common_move = Counter(self.history).most_common(1)[0][0]
        if random.random() < 0.7:
            return COUNTERS[most_common_move]
        return random.choice(CHOICES)

    @staticmethod
    def determine_winner(player: str, computer: str) -> str:
        if player == computer:
            return "tie"
        return "player" if WINS[player] == computer else "computer"

    def play_round(self, player: str) -> Dict[str, Optional[str]]:
        if player not in CHOICES:
            raise ValueError("Invalid move")
        if self.finished:
            raise RuntimeError("The match is finished")

        computer = self.computer_move()
        result = self.determine_winner(player, computer)
        self.history.append(player)

        if result == "player":
            self.player_score += 1
            self.current_streak += 1
            self.stats["wins"] += 1
            self.stats["best_streak"] = max(self.stats["best_streak"], self.current_streak)
        elif result == "computer":
            self.computer_score += 1
            self.current_streak = 0
            self.stats["losses"] += 1
        else:
            self.stats["ties"] += 1

        self.stats["rounds"] += 1
        self.store.save(self.stats)

        if self.player_score >= self.target:
            self.finished = True
            self.match_winner = "player"
        elif self.computer_score >= self.target:
            self.finished = True
            self.match_winner = "computer"

        return {
            "player": player,
            "computer": computer,
            "result": result,
            "match_winner": self.match_winner,
        }

    @property
    def win_rate(self) -> float:
        decided_rounds = self.stats["wins"] + self.stats["losses"]
        return (self.stats["wins"] / decided_rounds * 100) if decided_rounds else 0.0
