import tkinter as tk
from tkinter import font, messagebox, ttk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("900x800")
        self.root.configure(bg="#f0f8ff")  # Light blue background
        self.root.resizable(False, False)
        
        # Initialize scores and game history
        self.user_score = 0
        self.computer_score = 0
        self.tie_count = 0
        self.total_games = 0
        self.game_history = []
        
        # Create custom fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.header_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.normal_font = font.Font(family="Helvetica", size=12)
        self.emoji_font = font.Font(family="Segoe UI Emoji", size=48)
        self.score_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.small_font = font.Font(family="Helvetica", size=10)
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f0f8ff")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Title
        title_label = tk.Label(main_frame, text="Rock-Paper-Scissors Game", 
                              font=self.title_font, bg="#f0f8ff", fg="#2c3e50")
        title_label.pack(pady=10)
        
        # Game stats
        stats_frame = tk.Frame(main_frame, bg="#f0f8ff")
        stats_frame.pack(pady=5)
        
        self.games_label = tk.Label(stats_frame, text="Games Played: 0", 
                                   font=self.normal_font, bg="#f0f8ff", fg="#7f8c8d")
        self.games_label.pack()
        
        # Instructions
        instruction_label = tk.Label(main_frame, text="Choose your weapon:",
                                   font=self.header_font, bg="#f0f8ff", fg="#34495e")
        instruction_label.pack(pady=10)
        
        # Choice buttons frame
        button_frame = tk.Frame(main_frame, bg="#f0f8ff")
        button_frame.pack(pady=15)
        
        # Choice buttons
        choices = [("Rock", "✊", "rock"), ("Paper", "✋", "paper"), ("Scissors", "✌️", "scissors")]
        self.choice_buttons = []
        
        for i, (text, emoji, choice) in enumerate(choices):
            btn_frame = tk.Frame(button_frame, bg="#f0f8ff", highlightbackground="#bdc3c7", 
                                highlightthickness=1, relief=tk.RAISED, bd=2)
            btn_frame.grid(row=0, column=i, padx=10)
            
            emoji_label = tk.Label(btn_frame, text=emoji, font=self.emoji_font, 
                                  bg="#f0f8ff", cursor="hand2")
            emoji_label.pack(pady=5)
            emoji_label.bind("<Button-1>", lambda e, c=choice: self.play(c))
            
            btn = tk.Button(btn_frame, text=text, font=self.normal_font,
                           width=10, height=1, bg="#3498db", fg="white", cursor="hand2",
                           command=lambda c=choice: self.play(c))
            btn.pack(pady=5)
            self.choice_buttons.append(btn)
        
        # Result display frame
        result_frame = tk.LabelFrame(main_frame, text="Current Game", 
                                    font=self.header_font, bg="#f0f8ff", fg="#2c3e50",
                                    relief=tk.GROOVE, bd=2)
        result_frame.pack(pady=15, padx=10, fill=tk.BOTH, expand=True)
        
        # Choices display
        choices_frame = tk.Frame(result_frame, bg="#f0f8ff")
        choices_frame.pack(pady=15)
        
        # User choice
        user_frame = tk.Frame(choices_frame, bg="#f0f8ff")
        user_frame.grid(row=0, column=0, padx=20)
        
        tk.Label(user_frame, text="Your Choice", font=self.normal_font, 
                bg="#f0f8ff", fg="#2980b9").pack()
        
        self.user_display = tk.Label(user_frame, text="?", font=self.emoji_font, 
                                    bg="#f0f8ff", fg="#2980b9", width=4, height=2)
        self.user_display.pack(pady=10)
        
        # VS label
        vs_label = tk.Label(choices_frame, text="VS", font=self.header_font, 
                           bg="#f0f8ff", fg="#e74c3c")
        vs_label.grid(row=0, column=1, padx=15)
        
        # Computer choice
        computer_frame = tk.Frame(choices_frame, bg="#f0f8ff")
        computer_frame.grid(row=0, column=2, padx=20)
        
        tk.Label(computer_frame, text="Computer's Choice", font=self.normal_font, 
                bg="#f0f8ff", fg="#c0392b").pack()
        
        self.computer_display = tk.Label(computer_frame, text="?", font=self.emoji_font, 
                                        bg="#f0f8ff", fg="#c0392b", width=4, height=2)
        self.computer_display.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(result_frame, text="Make your choice to start the game!", 
                                    font=self.header_font, bg="#f0f8ff", fg="#2c3e50")
        self.result_label.pack(pady=15)
        
        # Score display
        score_frame = tk.Frame(result_frame, bg="#f0f8ff")
        score_frame.pack(pady=10)
        
        # User score
        user_score_frame = tk.Frame(score_frame, bg="#f0f8ff")
        user_score_frame.grid(row=0, column=0, padx=15)
        
        tk.Label(user_score_frame, text="Your Score", font=self.normal_font, 
                bg="#f0f8ff", fg="#2980b9").pack()
        
        self.user_score_label = tk.Label(user_score_frame, text="0", font=self.score_font, 
                                        bg="#f0f8ff", fg="#2980b9")
        self.user_score_label.pack()
        
        # Tie count
        tie_frame = tk.Frame(score_frame, bg="#f0f8ff")
        tie_frame.grid(row=0, column=1, padx=15)
        
        tk.Label(tie_frame, text="Ties", font=self.normal_font, 
                bg="#f0f8ff", fg="#7f8c8d").pack()
        
        self.tie_label = tk.Label(tie_frame, text="0", font=self.score_font, 
                                 bg="#f0f8ff", fg="#7f8c8d")
        self.tie_label.pack()
        
        # Computer score
        computer_score_frame = tk.Frame(score_frame, bg="#f0f8ff")
        computer_score_frame.grid(row=0, column=2, padx=15)
        
        tk.Label(computer_score_frame, text="Computer Score", font=self.normal_font, 
                bg="#f0f8ff", fg="#c0392b").pack()
        
        self.computer_score_label = tk.Label(computer_score_frame, text="0", font=self.score_font, 
                                            bg="#f0f8ff", fg="#c0392b")
        self.computer_score_label.pack()
        
        # Score card frame
        score_card_frame = tk.LabelFrame(main_frame, text="Score Card - Game History", 
                                       font=self.header_font, bg="#f0f8ff", fg="#2c3e50",
                                       relief=tk.GROOVE, bd=2)
        score_card_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Create treeview for score card
        columns = ("game", "user_choice", "computer_choice", "result")
        self.score_tree = ttk.Treeview(score_card_frame, columns=columns, show="headings", height=6)
        
        # Define headings
        self.score_tree.heading("game", text="Game")
        self.score_tree.heading("user_choice", text="Your Choice")
        self.score_tree.heading("computer_choice", text="Computer's Choice")
        self.score_tree.heading("result", text="Result")
        
        # Define columns
        self.score_tree.column("game", width=60, anchor=tk.CENTER)
        self.score_tree.column("user_choice", width=100, anchor=tk.CENTER)
        self.score_tree.column("computer_choice", width=120, anchor=tk.CENTER)
        self.score_tree.column("result", width=100, anchor=tk.CENTER)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(score_card_frame, orient=tk.VERTICAL, command=self.score_tree.yview)
        self.score_tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack treeview and scrollbar
        self.score_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=5)
        
        # Button frame
        action_frame = tk.Frame(main_frame, bg="#f0f8ff")
        action_frame.pack(pady=15)
        
        # Play again button
        self.play_again_btn = tk.Button(action_frame, text="Next Round", font=self.normal_font,
                                       width=15, height=1, bg="#2ecc71", fg="white", cursor="hand2",
                                       command=self.next_round, state=tk.DISABLED)
        self.play_again_btn.pack(side=tk.LEFT, padx=10)
        
        # End game button
        self.end_game_btn = tk.Button(action_frame, text="End Game", font=self.normal_font,
                                     width=15, height=1, bg="#e74c3c", fg="white", cursor="hand2",
                                     command=self.end_game)
        self.end_game_btn.pack(side=tk.LEFT, padx=10)
        
        # Clear history button
        self.clear_btn = tk.Button(action_frame, text="Clear History", font=self.normal_font,
                                  width=15, height=1, bg="#f39c12", fg="white", cursor="hand2",
                                  command=self.clear_history)
        self.clear_btn.pack(side=tk.LEFT, padx=10)
        
        # Add some style
        self.style_buttons()
        
    def style_buttons(self):
        # Style the buttons
        for btn in self.choice_buttons:
            btn.configure(relief=tk.FLAT, bd=0, highlightthickness=0,
                         activebackground="#2980b9")
        
        self.play_again_btn.configure(relief=tk.FLAT, bd=0, highlightthickness=0,
                                    activebackground="#27ae60")
        
        self.end_game_btn.configure(relief=tk.FLAT, bd=0, highlightthickness=0,
                                   activebackground="#c0392b")
        
        self.clear_btn.configure(relief=tk.FLAT, bd=0, highlightthickness=0,
                                activebackground="#e67e22")
        
    def play(self, user_choice):
        # Disable choice buttons during result display
        for btn in self.choice_buttons:
            btn.config(state=tk.DISABLED)
        
        # Get computer's choice
        choices = {"rock": "✊ Rock", "paper": "✋ Paper", "scissors": "✌️ Scissors"}
        computer_choice = random.choice(list(choices.keys()))
        
        # Update choice displays
        self.user_display.config(text=choices[user_choice].split()[0])
        self.computer_display.config(text=choices[computer_choice].split()[0])
        
        # Determine winner
        if user_choice == computer_choice:
            result = "Tie"
            result_text = "It's a tie!"
            color = "#f39c12"
            self.tie_count += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You Win"
            result_text = "You win! 🎉"
            color = "#27ae60"
            self.user_score += 1
        else:
            result = "Computer Wins"
            result_text = "Computer wins! 🤖"
            color = "#e74c3c"
            self.computer_score += 1
        
        # Update game count
        self.total_games += 1
        self.games_label.config(text=f"Games Played: {self.total_games}")
        
        # Update result label
        self.result_label.config(text=result_text, fg=color)
        
        # Update scores
        self.user_score_label.config(text=str(self.user_score))
        self.tie_label.config(text=str(self.tie_count))
        self.computer_score_label.config(text=str(self.computer_score))
        
        # Add to game history
        game_data = (self.total_games, choices[user_choice], choices[computer_choice], result)
        self.game_history.append(game_data)
        
        # Update score card
        self.update_score_card()
        
        # Enable next round button
        self.play_again_btn.config(state=tk.NORMAL)
    
    def update_score_card(self):
        # Clear existing items
        for item in self.score_tree.get_children():
            self.score_tree.delete(item)
        
        # Add items from game history
        for game in self.game_history:
            # Color code based on result
            tags = ()
            if game[3] == "You Win":
                tags = ("win",)
            elif game[3] == "Computer Wins":
                tags = ("lose",)
            else:
                tags = ("tie",)
                
            self.score_tree.insert("", "end", values=game, tags=tags)
        
        # Configure tag colors
        self.score_tree.tag_configure("win", background="#d4f1d4")  # Light green
        self.score_tree.tag_configure("lose", background="#f8d7da")  # Light red
        self.score_tree.tag_configure("tie", background="#fff3cd")  # Light yellow
        
        # Scroll to the bottom
        self.score_tree.yview_moveto(1)
    
    def next_round(self):
        # Reset choice displays
        self.user_display.config(text="?")
        self.computer_display.config(text="?")
        
        # Reset result label
        self.result_label.config(text="Make your choice to start the next round!", fg="#2c3e50")
        
        # Enable choice buttons
        for btn in self.choice_buttons:
            btn.config(state=tk.NORMAL)
        
        # Disable next round button
        self.play_again_btn.config(state=tk.DISABLED)
    
    def end_game(self):
        # Calculate win percentages
        if self.total_games > 0:
            user_percentage = (self.user_score / self.total_games) * 100
            computer_percentage = (self.computer_score / self.total_games) * 100
            tie_percentage = (self.tie_count / self.total_games) * 100
            
            # Show final results
            result_message = (
                f"Game Over!\n\n"
                f"Total Games: {self.total_games}\n"
                f"Your Wins: {self.user_score} ({user_percentage:.1f}%)\n"
                f"Computer Wins: {self.computer_score} ({computer_percentage:.1f}%)\n"
                f"Ties: {self.tie_count} ({tie_percentage:.1f}%)\n\n"
            )
            
            # Determine overall winner
            if self.user_score > self.computer_score:
                result_message += "🎉 Congratulations! You won the game! 🎉"
            elif self.computer_score > self.user_score:
                result_message += "🤖 Computer wins the game! Better luck next time!"
            else:
                result_message += "⚖️ It's a tie game! Well played!"
            
            # Ask if user wants to play again
            play_again = messagebox.askyesno("Game Over", result_message + "\n\nWould you like to play again?")
            
            if play_again:
                self.reset_game()
            else:
                self.root.quit()
        else:
            messagebox.showinfo("Game Over", "You ended the game without playing any rounds.")
            self.root.quit()
    
    def clear_history(self):
        # Clear game history
        self.game_history = []
        
        # Clear score card
        for item in self.score_tree.get_children():
            self.score_tree.delete(item)
        
        messagebox.showinfo("History Cleared", "Game history has been cleared!")
    
    def reset_game(self):
        # Reset all scores and counters
        self.user_score = 0
        self.computer_score = 0
        self.tie_count = 0
        self.total_games = 0
        self.game_history = []
        
        # Update displays
        self.user_display.config(text="?")
        self.computer_display.config(text="?")
        self.result_label.config(text="Make your choice to start a new game!", fg="#2c3e50")
        self.user_score_label.config(text="0")
        self.tie_label.config(text="0")
        self.computer_score_label.config(text="0")
        self.games_label.config(text="Games Played: 0")
        
        # Clear score card
        for item in self.score_tree.get_children():
            self.score_tree.delete(item)
        
        # Enable choice buttons
        for btn in self.choice_buttons:
            btn.config(state=tk.NORMAL)
        
        # Disable next round button
        self.play_again_btn.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()