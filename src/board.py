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

    def pop(self):
        self.board.pop()

    def san(self, move):
        self.board.san(move)

    def print(self):
        print(self.board)

    def evaluate_board(self):
        score = 0

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)

            if piece is not None:
                score += self.piece_value(piece)

        return score

    def piece_value(self, piece):
        symbol = piece.symbol()
        score = 1

        if symbol.lower() == 'n' or symbol.lower() == 'b':
            score = 3
        elif symbol.lower() == 'r':
            score = 5
        elif symbol.lower() == 'q':
            score = 9
        elif symbol.lower() == 'k':
            score = 100

        if symbol.islower():
            score *= -1

        return score
