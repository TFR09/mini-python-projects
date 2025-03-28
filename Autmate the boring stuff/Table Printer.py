tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    longest = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if len(list[i][j]) > longest:
                longest = len(list[i][j])
    colWidths = longest

    for l in range(len(list[0])):
        for k in range(len(list)):
            value = list[k][l]
            print(value.rjust(colWidths),end = ' ')
        print(end = '\n')
    
printTable(tableData)
