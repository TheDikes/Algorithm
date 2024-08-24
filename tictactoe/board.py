from player import Player
from move import Move

class Board:
    
    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[0, 0, 0], 
                           [0, 0, 0], 
                           [0, 0, 0]]
        
    def print_board(self):
        print("\nPositions: ")
        self.print_board_with_positions()

        print("Board: ")
        for row in self.game_board:
            print("|", end="")

            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f"  {column} |", end="")
            print()
        print()

    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]

        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print("This position is already taken!. Enter another one.")


    def check_is_game_over(self, player, last_move):
        return ((self.check_row(player, last_move))
               or (self.check_column(player, last_move))
               or (self.check_diagonal(player))
               or (self.check_antidiagonal(player)))
    
    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]

        return board_row.count(player.marker) == 3
    
    def check_column(self, player, last_move):
        col_index = last_move.get_column()
        board_col = [self.game_board[i][col_index] for i in range(len(self.game_board))]

        return board_col.count(player.marker) == 3
    
    def check_diagonal(self, player):
        return all (self.game_board[i][i] == player.marker for i in range(len(self.game_board))) #for diagonal [0][0], [1][1], [2][2]

    def check_antidiagonal(self, player):
        n = len(self.game_board)
        return all(self.game_board[i][n-i-1] == player.marker for i in range(len(n)))   #for anti-diagonal [0][2], [1][1], [2][0]
    


    # Instantiate the Board and Player objects here
board = Board()
player = Player()

# Use the Board and Player objects
board.print_board()

# Assume get_move() is a method that returns a Move object
move1 = player.get_move()
move2 = player.get_move()
move3 = player.get_move()

board.submit_move(player, move1)
board.submit_move(player, move2)
board.submit_move(player, move3)

print(board.check_is_game_over(player, move3))