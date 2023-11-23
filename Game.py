from State import State


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = player1
        self.state = State()

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

            while not self.state.is_valid_move(move):
                print("Invalid move. Try again.")
                move = self.current_player.get_move()

            self.state.make_move(move, self.current_player)

            if self.state.is_winner(self.current_player):
                self.state.print_board()
                print(f"Player {self.current_player.symbol} wins!")
                return

            self.switch_player()

        if not self.state.is_winner(self.players[0]) and not self.state.is_winner(
            self.players[1]
        ):
            self.state.print_board()
            print("It's a tie!")
