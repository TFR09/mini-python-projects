
def wordsStarting(file, lower, upper):
    myfile = open(file)
    words = myfile.read().split()
    list = []
    for word in words:
        if (lower <= word[0] <= upper):
            list.append(word)
        
    myfile.close()
    return list

if __name__ == "__main__":
    caps = wordsStarting('richmond.txt','A','Z')
    print("Words in richmond.txt starting with capitals: ", caps)
