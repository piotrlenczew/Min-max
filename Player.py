class Player:
    def __init__(self, number=None):
        self.number = number

    def get_move(self, state):
        raise NotImplementedError("Subclasses must implement the get_move method.")


class HumanPlayer(Player):
    def get_move(self, state):
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                move = (row, col)

                if state.is_valid_move(move):
                    return move
                else:
                    print("Invalid move. Try again.")

            except ValueError:
                print("Invalid input. Please enter integers for row and column.")
