validSquares = ['a1','a2','a3','a4','a5','a6','a7','a8',
                'b1','b2','b3','b4','b5','b6','b7','b8',
                'c1','c2','c3','c4','c5','c6','c7','c8',
                'd1','d2','d3','d4','d5','d6','d7','d8',
                'e1','e2','e3','e4','e5','e6','e7','e8',
                'f1','f2','f3','f4','f5','f6','f7','f8',
                'g1','g2','g3','g4','g5','g6','g7','g8',
                'h1','h2','h3','h4','h5','h6','h7','h8']

validPieces = ['wking','bking','wqueen','bqueen','wrook','brook','wknight','bknight','wbishop','bbishop','wpawn','bpawn']

board = {'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen', 'e3': 'wking','a8':''}

def count(x,dictionary):
    counter = 0
    for value in dictionary.values():
        if value == x:
            counter += 1

    return counter
    
def isValidChessBoard(board):
        for key in board.keys():
            if key not in validSquares:
                return False
        for value in board.values():
            if value not in validPieces:
                return False
        if count('bking',board) > 1 or count('wking',board) > 1 or count('bqueen',board) > 1 or count('wqueen',board) > 1:
            return False
        if count('brook',board) > 2 or count('wrook',board) > 2 or count('bbishop',board) > 2 or count('wbishop',board) > 2:
            return False
        if count('bknight',board) > 2 or count('wknight',board) > 2 or count('bpawn',board) > 8 or count('wpawn',board) > 8:
            return False
        return True
    
valid = isValidChessBoard(board)
print(valid)
