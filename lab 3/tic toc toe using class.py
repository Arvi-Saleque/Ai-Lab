import math

class TicTacToe:
    WIN_LINES = [
        ((0,0),(0,1),(0,2)),
        ((1,0),(1,1),(1,2)),
        ((2,0),(2,1),(2,2)),
        ((0,0),(1,0),(2,0)),
        ((0,1),(1,1),(2,1)),
        ((0,2),(1,2),(2,2)),
        ((0,0),(1,1),(2,2)),
        ((0,2),(1,1),(2,0)),
    ]

    def __init__(self, state=None):
        # state is a 3x3 list of lists containing 'X', 'O', or ' '
        self.state = state if state is not None else [[' ' for _ in range(3)] for _ in range(3)]

    def copy_state(self):
        return [row[:] for row in self.state]

    def display(self):
        print("\n".join(" | ".join(row) for row in self.state))
        print("-" * 5)

    def winner(self):
        for a, b, c in self.WIN_LINES:
            r1, c1 = a
            r2, c2 = b
            r3, c3 = c
            ch = self.state[r1][c1]
            if ch != ' ' and ch == self.state[r2][c2] == self.state[r3][c3]:
                return ch
        return None

    def current_player(self):
        cntx = sum(cell == 'X' for row in self.state for cell in row)
        cnto = sum(cell == 'O' for row in self.state for cell in row)
        return 'X' if cntx == cnto else 'O'

    def actions(self):
        moves = []
        for r in range(3):
            for c in range(3):
                if self.state[r][c] == ' ':
                    moves.append((r, c))
        return moves

    def result(self, action):
        r, c = action
        if self.state[r][c] != ' ':
            raise ValueError("Invalid move: cell already occupied")

        new_state = self.copy_state()
        new_state[r][c] = self.current_player()
        return TicTacToe(new_state)

    def terminal(self):
        return self.winner() is not None or all(cell != ' ' for row in self.state for cell in row)

    def utility(self):
        w = self.winner()
        if w == 'X':
            return 1
        if w == 'O':
            return -1
        return 0


class MinimaxAgent:
    """
    AI Agent using Minimax.
    Designed so later you can swap this with MCTSAgent that also has choose_move(game).
    """

    def choose_move(self, game: TicTacToe):
        # In your original code, AI is X, so we compute best move for the current player.
        player = game.current_player()
        if player == 'X':
            return self._max_value(game)[1]
        else:
            return self._min_value(game)[1]

    def _max_value(self, game: TicTacToe):
        if game.terminal():
            return game.utility(), None

        best_val = -math.inf
        best_move = None

        for move in game.actions():
            val, _ = self._min_value(game.result(move))
            if val > best_val:
                best_val = val
                best_move = move

        return best_val, best_move

    def _min_value(self, game: TicTacToe):
        if game.terminal():
            return game.utility(), None

        best_val = math.inf
        best_move = None

        for move in game.actions():
            val, _ = self._max_value(game.result(move))
            if val < best_val:
                best_val = val
                best_move = move

        return best_val, best_move


def play():
    game = TicTacToe()
    ai = MinimaxAgent()

    print("Welcome to Tic-Tac-Toe")
    print("You are O, AI is X\n")

    game.display()

    while not game.terminal():
        if game.current_player() == 'O':
            row, col = map(int, input("Enter row and column (0-2): ").split())
            if (row, col) not in game.actions():
                print("Invalid move. Try again.")
                continue
            game = game.result((row, col))
        else:
            move = ai.choose_move(game)
            print(f"AI plays: {move}")
            game = game.result(move)

        game.display()

    score = game.utility()
    if score == 1:
        print("X wins!")
    elif score == -1:
        print("O wins!")
    else:
        print("Draw!")


if __name__ == "__main__":
    play()
