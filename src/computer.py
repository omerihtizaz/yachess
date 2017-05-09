from random import randint
from time import sleep

class Computer:
    def __init__(self, board, is_player_white):
        self.board = board
        self.is_white = not is_player_white

    def move(self):
        print("\nComputer is thinking...\n")

        global_score = -1000 if self.is_white else 1000
        chosen_move = None

        for move in self.board.legal_moves():
            self.board.push(move)

            local_score = self.minimax(2, self.is_white)

            if self.is_white and local_score > global_score:
                global_score = local_score
                chosen_move = move

            if not self.is_white and local_score < global_score:
                global_score = local_score
                chosen_move = move

            self.board.pop()

        self.board.push(chosen_move)
        self.board.print()

    def minimax(self, depth, is_maximising_white):
        if depth == 0:
            return self.board.evaluate_board()

        best_score = -1000 if is_maximising_white else 1000

        for move in self.board.legal_moves():
            self.board.push(move)

            if is_maximising_white:
                best_score = max(best_score, self.minimax(depth - 1, False))
            else:
                best_score = min(best_score, self.minimax(depth - 1, True))

            self.board.pop()

        return best_score
