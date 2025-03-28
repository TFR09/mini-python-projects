from random import choice
from time import sleep


def get_random_word():
    with open("words.txt", 'r') as file:
        words = file.readlines()
    return choice(words).strip("\n")

def print_hangman(chance):
    return chance

def get_input(message):
    while True:
        guess = input(message)

        if guess.isalpha and len(guess) == 1:
            return guess.lower()
        
        print("Enter one letter as your guess")

def show_guess(guess, word , previous_guess):
    answer = previous_guess
    for i, letter in enumerate(word):
        if guess == letter:
            answer[i] = letter
    print(' '.join(answer), "\n")
    return answer
        

def play_game():
    secret_word = get_random_word()

    name = input("What is your name?\n")
    print(f"Hi {name} welcome to Hangman.")
    sleep(2)
    print("In this game you'll have to guess a word by slecting letters you think belong to the word")
    sleep(2)
    print("But beware you only have 10 chances... So make a smart guess")
    sleep(2)
    input("Press enter to begin\n")

    incorrect = 0
    MAX_INCORRECT = 10
    guesses = ['_' for _ in secret_word]

    while True:
        guess = get_input("Make your guess for word > ")
        sleep(1)
        guesses = show_guess(guess, secret_word, guesses)
        
        if ''.join(guesses) == secret_word:
            sleep(1)
            print("Well done! You guessed the correct word!")
            break


        if guess not in secret_word:
            incorrect += 1
            # print_hangman
            # print the hangman
            if incorrect == MAX_INCORRECT:
                sleep(1)
                print("Unfortunately you ran out of chances. The correct word was", secret_word)
                break

    input()

if __name__ == "__main__":
    play_game()