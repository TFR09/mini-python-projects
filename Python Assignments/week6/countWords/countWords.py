def countWords(filename):
    myfile = open(filename)
    nbrWords = len(myfile.read().split()) 
    myfile.close()
    
    return nbrWords

if __name__ == "__main__":
    nbrWords = countWords('_input.txt')
    print("Number of words = ", nbrWords)