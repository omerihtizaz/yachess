import chess


class Board:
    def __init__(self):
        self.board = chess.Board()

    def legal_moves(self):
        return self.board.legal_moves

    def push(self, move):
        self.board.push(move)

    def push_san(self, move):
        self.board.push_san(move)

    def print(self):
        print(self.board)
