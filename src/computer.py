import pickle


class Computer:
    depth = 3

    cached = 0
    not_cached = 0

    board_caches = {}

    try:
        cache = open('data/cache.p', 'rb')
    except IOError:
        cache = open('data/cache.p', 'wb')
        pickle.dump(board_caches, cache)
    else:
        board_caches = pickle.load(cache)

    def __init__(self, board, is_player_white):
        self.board = board
        self.is_computer_white = not is_player_white

    def computer_move(self):
        global_score = -1e8 if self.is_computer_white else 1e8
        chosen_move = None

        for move in self.board.legal_moves():
            self.board.push(move)

            local_score = self.minimax(self.depth, self.is_computer_white, -1e8,
                                       1e8)

            if (self.is_computer_white and local_score > global_score) or (
                    not self.is_computer_white and local_score < global_score):
                global_score = local_score
                chosen_move = move

            self.board.pop()

            print(local_score, move)

        print('\n' + str(global_score) + ' ' + str(chosen_move))

        print('\ncached: ' + str(self.cached))
        print('not cached: ' + str(self.not_cached))
        print((self.cached / (self.cached + self.not_cached)) * 100, '%\n')

        self.board.push(chosen_move)

        with open('data/cache.p', 'wb') as cache:
            pickle.dump(self.board_caches, cache)

    def minimax(self, depth, is_maximising_white, alpha, beta):
        if depth == 0:
            self.board_caches[self.hash_board(
                depth, is_maximising_white)] = self.board.evaluate_board()

            return self.board_caches[self.hash_board(depth,
                                                     is_maximising_white)]

        # if won or lost or drew
        if not self.board.legal_moves():
            self.board_caches[self.hash_board(
                depth,
                is_maximising_white)] = 1e8 if is_maximising_white else -1e8

            return self.board_caches[self.hash_board(depth,
                                                     is_maximising_white)]

        # if board in cache
        if self.hash_board(depth, is_maximising_white) in self.board_caches:
            self.cached += 1

            return self.board_caches[self.hash_board(depth,
                                                     is_maximising_white)]

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

            self.board_caches[self.hash_board(depth,
                                              is_maximising_white)] = best_score

            self.board.pop()

            if beta <= alpha:
                break

        self.board_caches[self.hash_board(depth,
                                          is_maximising_white)] = best_score

        return self.board_caches[self.hash_board(depth, is_maximising_white)]

    def hash_board(self, depth, is_maximising_white):
        return self.board.to_string() + ' ' + str(depth) + ' ' + str(
            is_maximising_white)
