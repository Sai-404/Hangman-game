import random

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    return stages[tries]

def get_word(difficulty):
    word_list = {
        'easy': ['apple', 'ball', 'cat', 'dog', 'fish'],
        'medium': ['python', 'programming', 'hangman', 'bicycle', 'puzzle'],
        'hard': ['microscope', 'xylophone', 'juxtaposition', 'quizzical', 'rhythm']
    }
    return random.choice(word_list[difficulty])

def play_game():
    print("Welcome to Hangman!")
    print("Choose a difficulty level: Easy, Medium, or Hard")
    difficulty = input("Enter difficulty level: ").strip().lower()

    if difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty. Defaulting to Medium.")
        difficulty = 'medium'

    word = get_word(difficulty)
    word_length = len(word)
    guessed_word = ["_"] * word_length
    guessed_letters = []
    tries = 6

    print("\nLet's play Hangman!")
    print(display_hangman(tries))
    print("Word: ", " ".join(guessed_word))

    while tries > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter or guess the word: ").strip().lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try a different letter.")
            elif guess in word:
                print(f"Good guess! '{guess}' is in the word.")
                for i in range(word_length):
                    if word[i] == guess:
                        guessed_word[i] = guess
                guessed_letters.append(guess)
            else:
                print(f"Wrong guess! '{guess}' is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
        elif len(guess) == word_length:
            if guess == word:
                guessed_word = list(word)
                break
            else:
                print(f"Wrong guess! The word is not '{guess}'.")
                tries -= 1
        else:
            print("Invalid input. Please enter a single letter or a word of correct length.")

        print(display_hangman(tries))
        print("Word: ", " ".join(guessed_word))
        print("Guessed letters: ", ", ".join(guessed_letters))

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The correct word was:", word)

if __name__ == "__main__":
    play_game()
