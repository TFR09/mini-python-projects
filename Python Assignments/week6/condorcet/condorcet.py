def headToHead(candidateA, candidateB, filename):
    score = 0
    votesFile = open(filename)
    for vote in votesFile: 
        voteList = vote.split()
        indexA = voteList.index(candidateA)
        indexB = voteList.index(candidateB)
        if indexA < indexB:
            score += 1
        elif indexA > indexB:
            score -= 1
    votesFile.close()
    return score

def nbrWins(candidate, opponents, filename):
    wins = 0
    for opponent in opponents:
        if headToHead(candidate,opponent,filename) > 0:
            wins += 1
    return wins

def getCandidates(filename):
    myfile = open(filename)
    c = (myfile.readline()).split()
    cands = c[1:]
    myfile.close()
    return cands

def condorcet(filename):
    cand = getCandidates(filename)
    for candidate in cand:
        wins = nbrWins(candidate,cand,filename)
        print(candidate,"wins",wins,"times")
        if wins == (len(cand) - 1):
            winner = candidate
    print("The Condorcet Winner is", winner)
  
if __name__ == "__main__":
  print("CONDORCET ANALYSIS OF votes.txt")
  condorcet('votes.txt')
  print("======================================")
  print("CONDORCET ANALYSIS OF votes2.txt")
  condorcet('votes2.txt')