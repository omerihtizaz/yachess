import pickle


class Computer:
    depth = 3
    board_caches = {}

    cached = 0
    not_cached = 0
    test = 0

    def __init__(self, board, is_player_white):
        self.board = board
        self.is_computer_white = not is_player_white

        try:
            cache = open('data/cache.p', 'rb')
        except IOError:
            cache = open('data/cache.p', 'wb')
            pickle.dump(self.board_caches, cache)
        else:
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

        print('\n' + str(global_score) + str(chosen_move))

        print('\ncached: ' + str(self.cached))
        print('not cached: ' + str(self.not_cached))
        print('test: ' + str(self.test))
        print((self.cached / (self.cached + self.not_cached)) * 100, '%\n')

        self.board.push(chosen_move)

        with open('data/cache.p', 'wb') as cache:
            pickle.dump(self.board_caches, cache)

            print("dumped\n")

    def minimax(self, depth, is_maximising_white, alpha, beta):
        if depth == 0:
            return self.board.evaluate_board()

        # if won or lost or drew
        if not self.board.legal_moves():
            return 1e8 if is_maximising_white else -1e8

        # if board in cache, hashing board condition
        if self.hash_board(is_maximising_white) in self.board_caches:
            self.cached += 1

            return self.board_caches[self.hash_board(is_maximising_white)]

        # else
        self.not_cached += 1

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
            self.test += 1

            self.board.pop()

            if beta <= alpha:
                break

        return best_score

    def hash_board(self, is_maximising_white):
        return self.board.to_string() + ' ' + str(is_maximising_white)
