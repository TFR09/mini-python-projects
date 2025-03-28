class Game:
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.board = [["   ", "   ", "   "],
                      ["   ", "   ", "   "],
                      ["   ", "   ", "   "]]
        
    def get_char(self, row, col):
        return self.board[row][col]
    
    def set_char_at(self, row, col, char):
        if self.board[row][col] == "   ":
            self.board[row][col] = char
            return True
        print("Space full. Try another space!")
        return False

    def board_full(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.get_char(row, col) == "   ":
                    return False      
        return True  

    def show_board(self):
        print(f"{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}")
        print("---|---|---")
        print(f"{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}")
        print("---|---|---")
        print(f"{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}")

    def check_diagonals(self, char):
        d1, d2 = True, True
        for row in range(self.rows):
            if self.board[row][row] != char:
                d1 = False
            if self.board[self.rows - row - 1][row] != char:
                d2 = False
        diagonal = d1 or d2
        return diagonal

    def won(self, char):
        # check horizontal rows
        for row in range(self.rows):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == char:
                return True
            
        # check vertical rows
        for col in range(self.cols):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == char:
                return True

        # check diagonals
        return self.check_diagonals(char)


class Players:
    p1 = " X "
    p2 = " O "

def play_game():
    print("Welcome to my TicTacToe game")
    print("Player 1 is X and Player 2 is O. Press enter to play!")
    input()

    player1 = Players.p1
    player2 = Players.p2
    

    turn = player1

    game = Game()

    while True:
        #get input from players
        print(f"{turn.strip()}'s turn")
        row = int(input("Enter Row > "))
        col = int(input("Enter Column > "))

        # add to board
        successful_move = game.set_char_at(row, col, turn)

        game.show_board()

        if successful_move:
            if turn == player1:
                turn = player2
            else: 
                turn = player1

        # check if game ended
        if game.won(player1):
            print("Player 1 wins!")
            break
        elif game.won(player2):
            print("Player 2 wins!")
            break
        elif game.board_full():
            print("It's a tie!")
            break
    
    print("Thank you for playing!")

if __name__ == "__main__":
    play_game()