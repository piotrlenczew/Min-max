from State import State


class Game:
    def __init__(self, player1, player2, board_size):
        player1.number = 1
        player2.number = 2
        self.players = [player1, player2]
        self.current_player = player1
        self.state = State(board_size)

    def switch_player(self):
        self.current_player = (
            self.players[1]
            if self.current_player == self.players[0]
            else self.players[0]
        )

    def play(self):
        while not self.state.is_full():
            self.state.print_board()
            move = self.current_player.get_move(self.state)

            self.state.make_move(move, self.current_player.number)

            if self.state.is_winner(self.current_player.number):
                self.state.print_board()
                print(f"Player {self.current_player.number} wins!")
                return

            self.switch_player()

        self.state.print_board()
        print("It's a tie!")
