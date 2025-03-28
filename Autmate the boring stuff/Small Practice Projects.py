#Exercise 1

x = ['juice','bacon','water','eggs','apple']
spam = ['dogs','cats','banana','tofu']
def listgrp(x):
    for i in x:
        if i == x[-1]:
            print('and', i)
        else:
            print(i,end=', ')
        

#Exercise 2

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

def heart(lst):
    for i in range(len(lst[0])):
        for x in range(len(lst)):
            print(grid[x][i],end='')
        print()

#Exercise 3
    
            
