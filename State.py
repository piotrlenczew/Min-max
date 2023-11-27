import numpy as np


Tile = {0: " ", 1: "O", 2: "X"}


class State:
    def __init__(self, board_size):
        self.board_size = board_size
        self.rows, self.columns = board_size
        self.board = np.full((self.rows, self.columns), 0)

    def print_board(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(f"|{Tile[self.board[i][j]]}", end="")
            print("|")
        print()

    def is_full(self):
        return not any(0 in row for row in self.board)

    def is_winner(self, player_number):
        for i in range(self.rows):
            if all(self.board[i, j] == player_number for j in range(self.columns)) or all(
                self.board[j, i] == player_number for j in range(self.columns)
            ):
                return True

        if all(self.board[i, i] == player_number for i in range(self.rows)) or all(
            self.board[i, 2 - i] == player_number for i in range(self.rows)
        ):
            return True

        return False

    def is_valid_move(self, move):
        row, column = move
        return  0 <= column < self.columns and self.rows > row >= 0 == self.board[row, column]

    def make_move(self, move, player_number):
        row, column = move
        self.board[row, column] = player_number
