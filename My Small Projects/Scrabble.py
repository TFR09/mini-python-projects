
POINTS ={"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,"O":1,"P":3,"Q":10, "R":1,"S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}

def main():
    #Get input words from both players
    word1 = input("Player 1 Enter a word: ")
    word2 = input("Player 2 Enter a word: ")

    #Score both words
    score1 = compute_score(word1)
    score2 = compute_score(word2)

    print(f"\nPlayer 1's score is {score1}")
    print(f"Player 2's score is {score2}\n")

    #TODO: Print the winner
    if score1 > score2:
        print("Player 1 wins!")
    elif score1 < score2:
        print("Player  wins!")
    else:
        print("It's a draw!")

def compute_score(word):
    #TODO: Compute and return score for string
    total = 0
    s = word.upper()
    for i in range(len(word)):
        w = s[i]
        total += POINTS[w]
    return int(total)

main()
