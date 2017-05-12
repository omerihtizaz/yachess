import pickle

class Computer:
    depth = 3
    board_caches = None

    def __init__(self, board, is_player_white):
        self.board = board
        self.is_computer_white = not is_player_white

        with open('data/cache.txt', 'rb') as cache:
            self.board_caches = pickle.load(cache)

    def computer_move(self):
        global_score = -1e8 if self.is_computer_white else 1e8
        chosen_move = None

        for move in self.board.legal_moves():
            self.board.push(move)

            local_score = self.minimax(self.depth, self.is_computer_white, -1e8,
                                       1e8)

            if self.is_computer_white and local_score > global_score:
                global_score = local_score
                chosen_move = move

            if not self.is_computer_white and local_score < global_score:
                global_score = local_score
                chosen_move = move

            self.board.pop()

            print(local_score, move)

        print()
        print(global_score, chosen_move)

        self.board.push(chosen_move)

        with open('data/cache.txt', 'wb') as cache:
            pickle.dump(self.board_caches, cache)

    def minimax(self, depth, is_maximising_white, alpha, beta):
        if depth == 0:
            return self.board.evaluate_board()

        # if won or lost or drew
        if not self.board.legal_moves():
            return 1e8 if is_maximising_white else -1e8

        # if board in cache, hashing board condition
        if self.hash_board(is_maximising_white) in self.board_caches:
            return self.board_caches[self.hash_board(is_maximising_white)]

        # else
        best_score = -1e8 if is_maximising_white else 1e8

        for move in self.board.legal_moves():
            self.board.push(move)

            if is_maximising_white:
                best_score = max(best_score,
                                 self.minimax(depth - 1, False, alpha, beta))
                alpha = max(alpha, best_score)
            else:
                best_score = min(best_score,
                                 self.minimax(depth - 1, True, alpha, beta))
                beta = min(beta, best_score)

            self.board_caches[self.hash_board(is_maximising_white)] = best_score

            self.board.pop()

            if beta <= alpha:
                break

        return best_score

    def hash_board(self, is_maximising_white):
        return self.board.to_string() + str(is_maximising_white)
