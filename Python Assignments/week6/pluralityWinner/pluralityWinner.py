def countVotes(filename,candidate):
    file = open(filename)
    votes = 0
    for line in file:
        vote = line.split()
        if vote[1] == candidate:
            votes += 1
    file.close()
    return votes

  
def pluralityWinner(filename,candidates):
    file = open(filename)
    results = []
    for candidate in  candidates:
        votes = countVotes(filename,candidate)
        results.append([candidate,votes])
    winner = results[0]
    for result in results:
        if (result[1] > winner[1]):
            winner = result
    file.close()
    return winner
  

if __name__ == "__main__":
    candidates = ['Memphis','Nashville','Chattanooga','Knoxville']
    win = pluralityWinner('votes.txt',candidates)
    print("Plurality winner from votes.txt")
    print(win)