#!/usr/bin/env python3
"""Rock Paper Scissors game with Tkinter GUI.

GUI version with buttons for Rock, Paper, Scissors choices.
Shows scores, round results, and allows resetting the game.
"""
import random
import tkinter as tk
from tkinter import font


class RPSGame:
    """Rock Paper Scissors game with GUI."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ ROCK PAPER SCISSORS ⚡")
        self.root.geometry("600x750")
        self.root.resizable(False, False)
        
        # Game state
        self.player_score = 0
        self.computer_score = 0
        self.choices = ['Rock', 'Paper', 'Scissors']
        
        # Retro CodeDex-inspired color scheme
        self.bg_color = "#1a1a2e"  # Deep dark blue
        self.secondary_bg = "#16213e"  # Slightly lighter blue
        self.accent_color = "#0f3460"  # Mid blue
        self.fg_color = "#e94560"  # Hot pink/red
        self.text_color = "#eee"  # Off-white
        self.button_color = "#533483"  # Purple
        self.button_hover = "#7c3aed"  # Bright purple
        self.win_color = "#00d9ff"  # Cyan
        self.lose_color = "#ff006e"  # Hot pink
        self.tie_color = "#ffd000"  # Yellow
        self.border_color = "#e94560"  # Hot pink border
        
        self.root.configure(bg=self.bg_color)
        
        # Retro fonts - using system monospace for pixel feel
        self.title_font = font.Font(family="Courier New", size=22, weight="bold")
        self.score_font = font.Font(family="Courier New", size=18, weight="bold")
        self.result_font = font.Font(family="Courier New", size=13, weight="bold")
        self.button_font = font.Font(family="Courier New", size=13, weight="bold")
        self.small_font = font.Font(family="Courier New", size=10)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Create all UI elements."""
        # Decorative top border
        top_border = tk.Frame(self.root, bg=self.border_color, height=5)
        top_border.pack(fill=tk.X)
        
        # Title with retro ASCII style
        title_frame = tk.Frame(self.root, bg=self.secondary_bg, relief=tk.RIDGE, bd=3)
        title_frame.pack(pady=15, padx=20, fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="⚡ ROCK PAPER SCISSORS ⚡",
            font=self.title_font,
            bg=self.secondary_bg,
            fg=self.fg_color,
            pady=10
        )
        title_label.pack()
        
        subtitle = tk.Label(
            title_frame,
            text="[ ARCADE MODE ]",
            font=self.small_font,
            bg=self.secondary_bg,
            fg=self.win_color,
            pady=5
        )
        subtitle.pack()
        
        # Score display with retro boxes
        score_container = tk.Frame(self.root, bg=self.bg_color)
        score_container.pack(pady=15)
        
        # Player score box
        player_box = tk.Frame(score_container, bg=self.accent_color, relief=tk.RIDGE, bd=4)
        player_box.grid(row=0, column=0, padx=15)
        
        tk.Label(
            player_box,
            text="[ PLAYER ]",
            font=self.small_font,
            bg=self.accent_color,
            fg=self.win_color,
            pady=5
        ).pack()
        
        self.player_score_label = tk.Label(
            player_box,
            text=f"{self.player_score:03d}",
            font=self.score_font,
            bg=self.accent_color,
            fg=self.text_color,
            width=8,
            pady=5
        )
        self.player_score_label.pack()
        
        # VS label
        tk.Label(
            score_container,
            text="VS",
            font=self.score_font,
            bg=self.bg_color,
            fg=self.fg_color
        ).grid(row=0, column=1, padx=10)
        
        # Computer score box
        comp_box = tk.Frame(score_container, bg=self.accent_color, relief=tk.RIDGE, bd=4)
        comp_box.grid(row=0, column=2, padx=15)
        
        tk.Label(
            comp_box,
            text="[ CPU ]",
            font=self.small_font,
            bg=self.accent_color,
            fg=self.lose_color,
            pady=5
        ).pack()
        
        self.computer_score_label = tk.Label(
            comp_box,
            text=f"{self.computer_score:03d}",
            font=self.score_font,
            bg=self.accent_color,
            fg=self.text_color,
            width=8,
            pady=5
        )
        self.computer_score_label.pack()
        
        # Choice display area with retro boxes
        choice_container = tk.Frame(self.root, bg=self.bg_color)
        choice_container.pack(pady=20)
        
        # Player choice display
        player_choice_box = tk.Frame(choice_container, bg=self.secondary_bg, relief=tk.GROOVE, bd=3)
        player_choice_box.grid(row=0, column=0, padx=15)
        
        tk.Label(
            player_choice_box,
            text="[ YOUR MOVE ]",
            font=self.small_font,
            bg=self.secondary_bg,
            fg=self.win_color
        ).pack(pady=5)
        
        self.player_choice_label = tk.Label(
            player_choice_box,
            text="???",
            font=self.result_font,
            bg=self.secondary_bg,
            fg=self.text_color,
            width=12,
            height=2
        )
        self.player_choice_label.pack(pady=10, padx=20)
        
        # Computer choice display
        comp_choice_box = tk.Frame(choice_container, bg=self.secondary_bg, relief=tk.GROOVE, bd=3)
        comp_choice_box.grid(row=0, column=1, padx=15)
        
        tk.Label(
            comp_choice_box,
            text="[ CPU MOVE ]",
            font=self.small_font,
            bg=self.secondary_bg,
            fg=self.lose_color
        ).pack(pady=5)
        
        self.computer_choice_label = tk.Label(
            comp_choice_box,
            text="???",
            font=self.result_font,
            bg=self.secondary_bg,
            fg=self.text_color,
            width=12,
            height=2
        )
        self.computer_choice_label.pack(pady=10, padx=20)
        
        # Result message with border
        result_box = tk.Frame(self.root, bg=self.accent_color, relief=tk.RIDGE, bd=4)
        result_box.pack(pady=15, padx=40, fill=tk.X)
        
        self.result_label = tk.Label(
            result_box,
            text=">>> MAKE YOUR CHOICE <<<",
            font=self.result_font,
            bg=self.accent_color,
            fg=self.tie_color,
            height=2
        )
        self.result_label.pack(pady=5)
        
        # Buttons for choices with retro styling
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        # Rock button
        rock_btn = tk.Button(
            button_frame,
            text="[ ROCK ]\n🪨",
            font=self.button_font,
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.button_hover,
            activeforeground=self.text_color,
            width=10,
            height=3,
            command=lambda: self.play_round('Rock'),
            cursor="hand2",
            relief=tk.RAISED,
            bd=5
        )
        rock_btn.grid(row=0, column=0, padx=10)
        
        # Paper button
        paper_btn = tk.Button(
            button_frame,
            text="[ PAPER ]\n📄",
            font=self.button_font,
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.button_hover,
            activeforeground=self.text_color,
            width=10,
            height=3,
            command=lambda: self.play_round('Paper'),
            cursor="hand2",
            relief=tk.RAISED,
            bd=5
        )
        paper_btn.grid(row=0, column=1, padx=10)
        
        # Scissors button
        scissors_btn = tk.Button(
            button_frame,
            text="[ SCISSORS ]\n✂️",
            font=self.button_font,
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.button_hover,
            activeforeground=self.text_color,
            width=10,
            height=3,
            command=lambda: self.play_round('Scissors'),
            cursor="hand2",
            relief=tk.RAISED,
            bd=5
        )
        scissors_btn.grid(row=0, column=2, padx=10)
        
        # Separator line
        separator = tk.Frame(self.root, bg=self.border_color, height=3)
        separator.pack(pady=20, padx=40, fill=tk.X)
        
        # Control buttons with more visible styling
        control_frame = tk.Frame(self.root, bg=self.bg_color)
        control_frame.pack(pady=10)
        
        reset_btn = tk.Button(
            control_frame,
            text="[ RESET ]\n🔄",
            font=self.button_font,
            bg="#ffd000",
            fg="#1a1a2e",
            activebackground="#ffed4e",
            activeforeground="#1a1a2e",
            width=14,
            height=3,
            command=self.reset_game,
            cursor="hand2",
            relief=tk.RAISED,
            bd=5
        )
        reset_btn.grid(row=0, column=0, padx=15)
        
        quit_btn = tk.Button(
            control_frame,
            text="[ QUIT ]\n❌",
            font=self.button_font,
            bg="#ff006e",
            fg=self.text_color,
            activebackground="#cc0058",
            activeforeground=self.text_color,
            width=14,
            height=3,
            command=self.root.quit,
            cursor="hand2",
            relief=tk.RAISED,
            bd=5
        )
        quit_btn.grid(row=0, column=1, padx=15)
        
        # Bottom decorative border
        bottom_border = tk.Frame(self.root, bg=self.border_color, height=5)
        bottom_border.pack(side=tk.BOTTOM, fill=tk.X)
    
    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner of the round."""
        if player_choice == computer_choice:
            return 'tie'
        
        wins = {
            'Rock': 'Scissors',
            'Scissors': 'Paper',
            'Paper': 'Rock'
        }
        
        if wins[player_choice] == computer_choice:
            return 'player'
        return 'computer'
    
    def play_round(self, player_choice):
        """Play a round with the given player choice."""
        computer_choice = random.choice(self.choices)
        
        # Update choice displays with retro formatting
        self.player_choice_label.config(text=f"{player_choice.upper()}")
        self.computer_choice_label.config(text=f"{computer_choice.upper()}")
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        if result == 'tie':
            self.result_label.config(
                text=">>> DRAW! TRY AGAIN <<<",
                fg=self.tie_color,
                bg=self.accent_color
            )
        elif result == 'player':
            self.player_score += 1
            self.result_label.config(
                text="*** PLAYER WINS! ***",
                fg=self.win_color,
                bg=self.accent_color
            )
        else:
            self.computer_score += 1
            self.result_label.config(
                text="*** CPU WINS! ***",
                fg=self.lose_color,
                bg=self.accent_color
            )
        
        # Update scores with zero-padding
        self.player_score_label.config(text=f"{self.player_score:03d}")
        self.computer_score_label.config(text=f"{self.computer_score:03d}")
    
    def reset_game(self):
        """Reset the game to initial state."""
        self.player_score = 0
        self.computer_score = 0
        
        self.player_score_label.config(text=f"{self.player_score:03d}")
        self.computer_score_label.config(text=f"{self.computer_score:03d}")
        
        self.player_choice_label.config(text="???")
        self.computer_choice_label.config(text="???")
        
        self.result_label.config(
            text=">>> MAKE YOUR CHOICE <<<",
            fg=self.tie_color,
            bg=self.accent_color
        )


def main():
    """Create and run the GUI application."""
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
