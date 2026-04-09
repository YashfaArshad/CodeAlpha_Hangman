# task# 01 : hangman_.py

import random


def get_word():
    words = {
        "python": "A programming language",
        "hangman": "This game!",
        "developer": "A person who writes code",
        "keyboard": "You type on it",
        "internet": "Global network"
    }
    word = random.choice(list(words.keys()))
    return word, words[word]


def display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])


def play_game():
    word, hint = get_word()
    guessed_letters = set()
    wrong_letters = set()
    attempts = 6

    print("\n🎮 Welcome TO Hangman Game")
    print(f"💡 Hint: {hint}")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("❌ Wrong letters:", " ".join(wrong_letters))
        print("❤️ Attempts left:", attempts)

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You WON!")
            return

        guess = input("👉 Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter ONE valid letter!")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("⚠️ Already guessed!")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("✅ Correct!")
        else:
            wrong_letters.add(guess)
            attempts -= 1
            print("❌ Wrong!")

    print(f"\n💀 OOPS! You LOST! Word was: {word}")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("👋 Goodbye!")
            break


if __name__ == "__main__":
    main()