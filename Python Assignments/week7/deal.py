import random

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

def deal(pack, nbrCards):
    cardlist = random.sample(pack, nbrCards)
    cards = set(cardlist)
    for card in cards:
        pack.remove(card)
    return cards
  
if __name__ == "__main__":
    print("A CALL TO deal(fullpack(),5) returns:")
    print(deal(fullpack(),5))