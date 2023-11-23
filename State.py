import numpy as np


Tile = {0: " ", 1: "O", 2: "X"}


class State:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(f"|{Tile[self.board[i][j]]}", end="")
            print("|")
        print()

    def is_full(self):
        return not any(0 in row for row in self.board)

    def is_winner(self, player):
        for i in range(3):
            if all(self.board[i, j] == player.symbol for j in range(3)) or all(
                self.board[j, i] == player.symbol for j in range(3)
            ):
                return True

        if all(self.board[i, i] == player.symbol for i in range(3)) or all(
            self.board[i, 2 - i] == player.symbol for i in range(3)
        ):
            return True

        return False

    def is_valid_move(self, move):
        row, col = move
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row, col] == 0

    def make_move(self, move, player):
        row, col = move
        self.board[row, col] = player.symbol
