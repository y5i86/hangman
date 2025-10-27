import tkinter as tk
import random

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")

        self.words = ["butterfly", "blue", "flowers", "black", "pizza"]
        self.word = random.choice(self.words)
        self.guesses = []
        self.lives = 6

        self.label_word = tk.Label(root, text=self.get_display_word(), font=("Helvetica", 20))
        self.label_word.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button_guess = tk.Button(root, text="Guess", command=self.make_guess)
        self.button_guess.pack(pady=5)

        self.label_info = tk.Label(root, text=f"Lives left: {self.lives}")
        self.label_info.pack(pady=5)

    def get_display_word(self):
        return " ".join([letter if letter in self.guesses else "_" for letter in self.word])

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.label_info.config(text="Give me a letter!")
            return

        if guess in self.guesses:
            self.label_info.config(text="You already gave me that letter.")
            return

        self.guesses.append(guess)

        if guess not in self.word:
            self.lives -= 1
            if self.lives == 0:
                self.label_info.config(text=f"Oops! Word was '{self.word}'")
                self.button_guess.config(state=tk.DISABLED)
            else:
                self.label_info.config(text=f"Wrong! Lives left: {self.lives}")
        else:
            if all(letter in self.guesses for letter in self.word):
                self.label_info.config(text="🎉 You are a Champion!")
                self.button_guess.config(state=tk.DISABLED)

        self.label_word.config(text=self.get_display_word())

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGUI(root)
    root.mainloop()