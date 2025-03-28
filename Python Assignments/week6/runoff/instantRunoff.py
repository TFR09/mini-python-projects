def instantRunoff(filename):
    votesfile = open(filename)
    c = votesfile.readline().split()
    candidates = c[1:]
    
    results = voteCounter(votesfile, candidates)
    y = eliminate(results, candidates)
    print(y)
    votesfile.close()
  
def voteCounter(filename, candidates):
    results = []
    for candidate in candidates:
        filename.seek(0)
        total = 0
        counter = 0
        for line in filename: 
            voteList = line.split()
            total += 1
            if voteList[1] == candidate:
                counter += 1

        percentage = (counter / total) * 100
        results.append([candidate,percentage])
        print(candidate, "gets", percentage,"% of votes")
        print(len(results))
        
    return results
  
def eliminate(results,candidates):
    eliminated = results[0]
    for cand in results:
        if cand[1] < eliminated[1]:
            eliminated = cand
    candidates.remove(eliminated[0])
    return candidates

def winner(results):
    winner = results[0][0]
    for cand in results:
        if (cand[1] >= 50):
            winner = cand[0]
            return winner


if __name__ == "__main__":
  instantRunoff("votes.txt")
