import random

def play():
    words = ["butterfly", "blue", "flowers", "black", "pizza"]
    word = random.choice(words)
    guesses = []
    lives = 6

    print("Hi, Welcome to Hangman!")
    print("_ " * len(word))

    while lives > 0:
        guess = input("Give me a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guesses:
            print("You already gave me that letter.")
            continue

        guesses.append(guess)

        if guess not in word:
            lives -= 1
            print(f"Oops! {lives} lives left.")
        else:
            print("Correct!")

        display = [letter if letter in guesses else "_" for letter in word]
        print(" ".join(display))

        if "_" not in display:
            print("🎉 You got the word!")
            break
    else:
        print(f"Game Over! The word was '{word}'.")

if __name__ == "__main__":
    play()