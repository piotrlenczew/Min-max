import numpy as np


Tile = {0: " ", 1: "O", 2: "X"}


class State:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = np.full((self.board_size, self.board_size), 0)
        self.heuristic_map = self.make_heuristic_map()

    def print_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(f"|{Tile[self.board[i][j]]}", end="")
            print("|")
        print()

    def is_full(self):
        return not any(0 in row for row in self.board)

    def is_winner(self, player_number):
        for i in range(self.board_size):
            if all(
                self.board[i][j] == player_number for j in range(self.board_size)
            ) or all(self.board[j][i] == player_number for j in range(self.board_size)):
                return True

        if all(
            self.board[i][i] == player_number for i in range(self.board_size)
        ) or all(self.board[i][2 - i] == player_number for i in range(self.board_size)):
            return True

        return False

    def is_valid_move(self, move):
        row, column = move
        return (
            0 <= column < self.board_size
            and self.board_size > row >= 0 == self.board[row][column]
        )

    def make_move(self, move, player_number):
        row, column = move
        self.board[row][column] = player_number

    def make_heuristic_map(self):
        heuristic_map = np.full((self.board_size, self.board_size), 2)
        for i in range(self.board_size):
            heuristic_map[i][i] = 3
            heuristic_map[i][self.board_size - 1 - i] = 3
        if self.board_size % 2 == 1:
            heuristic_map[self.board_size // 2][self.board_size // 2] = 4
        return heuristic_map
