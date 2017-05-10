class Computer:
    def __init__(self, board, is_player_white):
        self.board = board
        self.is_white = not is_player_white

    def move(self):
        print("\nComputer is thinking...\n")

        global_score = -1e8 if self.is_white else 1e8
        chosen_move = None

        for move in self.board.legal_moves():
            self.board.push(move)

            local_score = self.minimax(3, self.is_white, -1e8, 1e8)

            if self.is_white and local_score > global_score:
                global_score = local_score
                chosen_move = move

            if not self.is_white and local_score < global_score:
                global_score = local_score
                chosen_move = move

            print(local_score, move)
            self.board.pop()

        print()
        print(global_score, chosen_move)
        print()

        self.board.push(chosen_move)
        self.board.print()

    def minimax(self, depth, is_maximising_white, alpha, beta):
        if depth == 0:
            return self.board.evaluate_board()

        if not self.board.legal_moves():
            return 1e8 if is_maximising_white else -1e8

        best_score = -1e8 if is_maximising_white else 1e8

        for move in self.board.legal_moves():
            self.board.push(move)

            if is_maximising_white:
                best_score = max(best_score, self.minimax(depth - 1, False,
                                                          alpha, beta))
                alpha = max(alpha, best_score)
            else:
                best_score = min(best_score, self.minimax(depth - 1, True,
                                                          alpha, beta))
                beta = min(beta, best_score)

            self.board.pop()

            if beta <= alpha:
                break

        return best_score
