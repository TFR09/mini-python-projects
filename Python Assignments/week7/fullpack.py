def fullpack():
    suit = {'\u2660','\u2665','\u2666','\u2663'}
    cards = set()
    for type in suit:
        for i in range(2,11):
            cards.add(type + str(i))
            cards.add((type + "J"))
            cards.add((type + "Q"))
            cards.add((type + "K"))
            cards.add((type + "A"))
    return cards

if __name__ == '__main__':
    cards = fullpack()
    print(cards)