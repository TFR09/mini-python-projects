def initialiseState(col,row,orientation,agility,strength):
    state = {}
    player = {'type':'player','orientation':orientation,'agility':agility,'strength':strength}
    state['playerSquare'] = (col,row)
    state['player'] = player
    state['others'] = {}

    return state


def addHerb(state,col,row,agility):
    herb = {'type':'herb','agility':agility}
    others ={}
    others[(col,row)] = herb
    state['others'].update(others)
    
    return state


def addBread(state,col,row,strength):
    bread = {'type':'bread','strength':strength}
    others ={}
    others[(col,row)] = bread
    state['others'].update(others)
    
    return state


def addBlock(state,col,row,height):
    block = {'type':'block','height':height}
    others ={}
    others[(col,row)] = block
    state['others'].update(others)
    
    return state


def getEntityAt(state,col,row):
    if state['playerSquare'] == (col,row):
        entity = state['player']
    elif (col,row) in state['others']:
        entity = state['others'][(col,row)]
    else:
        entity = {}
    return entity

def checkOccupied(state):
    #checks if entity occupies space in front of player
    global col, row, direction
    direction = state['player']['orientation']
    col = state['playerSquare'][0]
    row = state['playerSquare'][1]
    if direction == 'right':
        col += 1
    elif direction == 'left':
        col -= 1
    elif direction == 'up':
        row -= 1
    else:
        row += 1
    return getEntityAt(state, col, row)


def showBoard(state,cols,rows):
    pPosition = state['playerSquare']
    object = state['others']
    direction = state['player']['orientation']
    
    #coordinates to centre the player on the board
    startRow = pPosition[1] - rows
    endRow = pPosition[1] + rows +1
    startCol = pPosition[0] - cols
    endCol = pPosition[0] + cols +1
    
    for row in range(startRow,endRow):
        for col in range(startCol,endCol):
            if (col,row) in object or (col,row) == pPosition:
                if (col,row) == pPosition:
                #print player with correct orientation
                    if direction == 'up':
                        print('\u2191',end=' ')
                    elif direction == 'down':
                        print('\u2193',end=' ')
                    elif direction == 'left':
                        print('\u2190',end=' ')
                    elif direction == 'right':
                        print('\u2192',end=' ')

                #check if one of the objects and print corresponding on board
                elif object[(col,row)]['type'] == 'herb':
                    print('#',end=' ')
                elif object[(col,row)]['type'] == 'bread':
                    print('@',end=' ')
                elif object[(col,row)]['type'] == 'block':
                    print(object[(col,row)]['height'],end=' ')
            else:
                print('. ',end='')
        print(' ',end ='\n')
    

def getPlayer(state):
    return state['player']


def getPlayerSquare(state):
    return state['playerSquare']


def turn(state, direction):
    legal = ('up', 'down', 'left', 'right')
    if direction in legal:
        state['player']['orientation'] = direction
        return 1
    else:
        return -1


def step(state):
    position = state['playerSquare']
    if checkOccupied(state) == {}:
        if direction == 'right':
            state['playerSquare'] = (position[0] +1,position[1])
        elif direction == 'left':
            state['playerSquare'] = (position[0] -1,position[1])
        elif direction == 'up':
            state['playerSquare'] = (position[0],position[1] -1)
        else:
            state['playerSquare'] = (position[0],position[1] +1)
        return 1
    else:
        return -1


def showPlayer(state):
    position = getPlayerSquare(state)
    player = getPlayer(state)
    print('row:',position[1],
            '\ncolumn:',position[0],
            '\norientation:',player['orientation'],
            '\nagility:',player['agility'],
            '\nstrength:',player['strength'])


def showFacing(state):
    entity = checkOccupied(state)
    if entity == {}:
        print('No entity')
    elif entity['type'] == 'herb':
        print('row:',row,
            '\ncolumn:',col,
            '\ntype:',entity['type'],
            '\nagility:',entity['agility'])
    elif entity['type'] == 'bread':
        print('row:',row,
            '\ncolumn:',col,
            '\ntype:',entity['type'],
            '\nstrength:',entity['strength'])
    else:
        print('row:',row,
            '\ncolumn:',col,
            '\ntype:',entity['type'],
            '\nheight:',entity['height'])


def eat(state):
    entity = checkOccupied(state)
    player = state['player']
    
    if entity == {} or entity['type'] == 'block':
        return -1
    elif entity['type'] == 'herb':
        player['agility'] += entity['agility']
        state['others'].pop((col,row))
    else:
        player['strength'] += entity['strength']
        state['others'].pop((col,row))
    return 1


def batter(state):
    entity = checkOccupied(state)
    player = state['player']
    
    if entity == {}:
        return -1
    elif entity['type'] == 'block' and state['player']['strength'] > 0:
        if entity['height'] <= 2:
            state['others'].pop((col,row))
        else:
            entity['height'] -= 2
            player['strength'] -= 1
        return 1
    else:
        return -2
    

def jump(state):
    entity = checkOccupied(state)
    col = state['playerSquare'][0]
    row = state['playerSquare'][1]
    if direction == 'right':
        col += 2
    elif direction == 'left':
        col -= 2
    elif direction == 'up':
        row -= 2
    else:
        row += 2
    occupied = getEntityAt(state,col,row)

    if entity == {}:
        return -1
    elif occupied == {}:
        if entity['type'] == 'block' and state['player']['agility'] > 0:
            state['player']['agility'] -= 1
            state['playerSquare'] = (col,row)
        elif entity['type'] == 'herb' or entity['type'] == 'bread':
            state['playerSquare'] = (col,row)
        return 1
    else:
        return -2


def readState(file):
    initFile = open(file)
    for line in initFile:
        entity = line.split()
        col = int(entity[1])
        row = int(entity[2])
        if entity[0] == 'player':
            state = initialiseState(col,row,entity[5],int(entity[3]),int(entity[4]))
        elif entity[0] == 'herb':
            addHerb(state,col,row,int(entity[3]))
        elif entity[0] == 'bread':
            addBread(state,col,row,int(entity[3]))
        else:
            addBlock(state,col,row,int(entity[3]))

    initFile.close()
    return state
      

def playConsole(file):
    state = readState(file)
    request = ''
    while request != 'quit':
        request = input('Next Request> ')
        if request == 'step':
            step(state)
        elif request == 'show player':
            showPlayer(state)
        elif request == 'show facing':
            showFacing(state)
        elif request == 'show board':
            showBoard(state,6,6)
        elif request == 'jump':
            jump(state)
        elif request == 'eat':
            eat(state)
        elif request == 'batter':
            batter(state)
        elif request == 'quit':
            print('Goodbye')
        elif request.split()[0] == 'turn':
            turn(state,request.split()[1])

if __name__ == "__main__":
    playConsole('example.txt')
  