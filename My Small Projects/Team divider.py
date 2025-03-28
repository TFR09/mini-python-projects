from random import choice
import sys

names = []

def main():
    print('Hello there! This is a group divider app.To continue press enter else type no')
    cont = input()
    if cont == '':
        print('How many people are there to make groups?')
        num = int(input())
        for i in range(int(num)):
            print('Please enter name',i+1
                  )
            name = input()
            names.append(name)

        grp1 = []
        grp2 = []

        if num%2 == 0:
            hnum = int(num/2)
        else:
            hnum = int((num/2)+
                       0.5)

        for e in range(0,hnum):
            player = choice(names)
            grp1.append(player)
            names.remove(player)

            if len(names) == 0:
                break

            player = choice(names)
            grp2.append(player)
            names.remove(player)
            

        print('1st team =', grp1)
        print('2nd team =', grp2)

    
    elif cont == 'no':
        exit()
    
    

if __name__=='__main__':
    main()
    
