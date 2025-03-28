from random import randint

def main():
    print("Welcome to the Cows and Bulls game!")
    q = input("Press enter to play or enter q to quit").lower()
    if q == "q":
        print("Thanks for playing!")
        quit()
    how_to_play()
    play()
    input()
   

def how_to_play():
   print("How to play: ")
   print("The correct number in the correct place will be the number of cows.")
   print("The correct number in the wrong place will be the number of bulls.")

def play():
    guesses = 0
    answer = str(randint(1000, 9999))
    player = 0
    cows, bulls = 0, 0
    while answer != player:
        player = input("Guess a random number between 1000 and 9999: ")
        for i in range(len(answer)):
            if player[i] == answer[i]:
                cows += 1
            elif player[i] in answer:
                bulls += 1
        print(f"{cows} cows and {bulls} bulls")
        guesses += 1

    print(f"You guessed the correct number in the correct place in {guesses} guesses!")

if __name__ == '__main__':
   main()