import tkinter as tk
from tkinter import ttk, messagebox
import random
class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.user_score = 0
        self.comp_score = 0
        # Frame for game elements
        self.game_frame = ttk.Frame(self.root, padding="20")
        self.game_frame.grid(row=0, column=0, sticky="nsew")
        # Label and Combobox for user's choice
        self.choice_label = ttk.Label(self.game_frame, text="Choose:")
        self.choice_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("rock")  # Default choice
        choices = ['rock', 'paper', 'scissors']
        self.choice_combobox = ttk.Combobox(self.game_frame, textvariable=self.user_choice_var, values=choices, state="readonly")
        self.choice_combobox.grid(row=0, column=1, padx=5, pady=5)
        # Result Label
        self.result_label = ttk.Label(self.game_frame, text="")
        self.result_label.grid(row=1, column=0, columnspan=2, pady=10)
        # Buttons for actions
        self.play_button = ttk.Button(self.game_frame, text="Play", command=self.play_game)
        self.play_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.reset_button = ttk.Button(self.game_frame, text="Reset Score", command=self.reset_scores)
        self.reset_button.grid(row=3, column=0, columnspan=2, pady=10)
        # Frame for score display
        self.score_frame = ttk.Frame(self.root, padding="20")
        self.score_frame.grid(row=1, column=0, sticky="nsew")
        self.score_label = ttk.Label(self.score_frame, text="Score:")
        self.score_label.pack()
        self.score_display_label = ttk.Label(self.score_frame, text=f"User: {self.user_score} | Computer: {self.comp_score}")
        self.score_display_label.pack()
        # Set grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
    def play_game(self):
        user_choice = self.user_choice_var.get()
        comp_choice = random.choice(['rock', 'paper', 'scissors'])
        result = self.determine_winner(user_choice, comp_choice)
        self.result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {comp_choice}\nResult: {result}")
        self.update_score(result)
    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'paper' and comp_choice == 'rock') or \
             (user_choice == 'scissors' and comp_choice == 'paper'):
            return "You win!"
        else:
            return "Computer wins!"
    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.comp_score += 1
        self.score_display_label.config(text=f"User: {self.user_score} | Computer: {self.comp_score}")
    def reset_scores(self):
        self.user_score = 0
        self.comp_score = 0
        self.score_display_label.config(text=f"User: {self.user_score} | Computer: {self.comp_score}")
        self.result_label.config(text="")
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()