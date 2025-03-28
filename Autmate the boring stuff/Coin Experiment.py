from random import *
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin = []
    for i in range(100):
        num = randint(0,1)
        if num == 0:
            coin.append('H')
        else:
            coin.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    end = False
    a,b = 0,6
    while not end:
        flip = coin[a]
        for i in coin[a:b]:
            if flip == i:
                streak = 'yes'
            else:
                streak = 'no'
                break
        if streak == 'yes':
            numberOfStreaks += 1
            break
        if b == len(coin):
            end = True
        a += 1
        b += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
