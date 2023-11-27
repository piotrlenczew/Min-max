class Player:
    def __init__(self, number=None):
        self.number = number

    def get_move(self, state):
        raise NotImplementedError(
            "Get_move is implemented by subclasses. Use one of them."
        )


class HumanPlayer(Player):
    def get_move(self, state):
        while True:
            try:
                row, col = [
                    int(x) for x in input("Enter move (row, column): ").split(", ")
                ]
                move = (row, col)

                if state.is_valid_move(move):
                    return move
                else:
                    print("Invalid move. Try again.")

            except ValueError:
                print("Invalid input. Please enter integers for row and column.")


class ComputerPlayer(Player):
    def __init__(self, max_depth):
        super().__init__()
        self.max_depth = max_depth

    def get_move(self, state):
        _, move = self.minimax(state, self.number, self.max_depth)
        return move

    def minimax(self, state, player_number, depth):
        if state.is_winner(self.number):
            return 10, None
        elif state.is_winner(self.opponent_number(self.number)):
            return -10, None
        elif state.is_full():
            return 0, None
        elif depth == 0:
            return self.heuristic(state), None

        scores = []
        moves = []

        for i in range(state.board_size):
            for j in range(state.board_size):
                if state.is_valid_move((i, j)):
                    state.make_move((i, j), player_number)
                    score, _ = self.minimax(
                        state, self.opponent_number(player_number), depth - 1
                    )
                    state.board[i][j] = 0

                    scores.append(score)
                    moves.append((i, j))

        if player_number == self.number:
            max_index = scores.index(max(scores))
            return scores[max_index], moves[max_index]
        else:
            min_index = scores.index(min(scores))
            return scores[min_index], moves[min_index]

    def heuristic(self, state):
        result = 0
        for i in range(state.board_size):
            for j in range(state.board_size):
                if state.board[i][j] == self.number:
                    result += state.heuristic_map[i][j]
                elif state.board[i][j] == self.opponent_number(self.number):
                    result -= state.heuristic_map[i][j]
        return result

    def opponent_number(self, player_number):
        return 1 if player_number == 2 else 2
