import random

def shuffle_word(word):
    """Shuffles the letters of a word."""
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def play_game():
    """Main function to play the game."""
    print("Welcome to the Word Shuffle Game!")
    print("You will be given a word, and you have to guess the original word by shuffling its letters.")
    print("Enter 'quit' to exit the game.")
    words = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
    while True:
        word = random.choice(words)
        shuffled_word = shuffle_word(word)
        print(f"Shuffled Word: {shuffled_word}")
        guess = input("Guess the original word: ")
        if guess.lower() == 'quit':
            break
        elif guess.lower() == word:
            print("Congratulations! You guessed it right!")
        else:
            print(f"Sorry, the correct answer is {word}. Better luck next time!")
    print("Thanks for playing!")
