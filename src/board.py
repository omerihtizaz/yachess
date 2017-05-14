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

    def is_checkmate(self):
        return self.board.is_checkmate()

    def is_stalemate(self):
        return self.board.is_stalemate()

    def to_string(self):
        return str(self.board)

    def piece_at(self, square):
        return self.board.piece_at(square)

    def evaluate_board(self):
        score = 0

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)

            if piece is not None:
                score += piece_value(piece, square)

        return score


def piece_value(piece, square):
    symbol = piece.symbol()
    is_white = not symbol.islower()

    row = convert_square(square, is_white)[0]
    column = convert_square(square, is_white)[1]

    score = 0

    if symbol.lower() == 'p':
        score = 1000 + pawn_table[row][column]
    elif symbol.lower() == 'n':
        score = 3000 + knight_table[row][column]
    elif symbol.lower() == 'b':
        score = 3000 + bishop_table[row][column]
    elif symbol.lower() == 'r':
        score = 5000 + rook_table[row][column]
    elif symbol.lower() == 'q':
        score = 9000 + queen_table[row][column]
    elif symbol.lower() == 'k':
        score = 1000000 + king_table[row][column]

    if not is_white:
        score *= -1

    return score

def convert_square(square, is_white):
    row = square // 8
    column = square % 8

    if is_white:
        row = 7 - row

    return (row, column)

pawn_table = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [5, 10, 10, -20, -20, 10, 10, 5],
    [5, -5, -10, 0, 0, -10, -5, 5],
    [0, 0, 0, 20, 20, 0, 0, 0],
    [5, 5, 10, 25, 25, 10, 5, 5],
    [10, 10, 20, 30, 30, 20, 10, 10],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

knight_table = [
    [-50, -40, -30, -30, -30, -30, -40, -50],
    [-40, -20, 0, 0, 0, 0, -20, -40],
    [-30, 0, 10, 15, 15, 10, 0, -30],
    [-30, 5, 15, 20, 20, 15, 5, -30],
    [-30, 0, 15, 20, 20, 15, 0, -30],
    [-30, 5, 10, 15, 15, 10, 5, -30],
    [-40, -20, 0, 5, 5, 0, -20, -40],
    [-50, -40, -30, -30, -30, -30, -40, -50]
]

bishop_table = [
    [-20, -10, -10, -10, -10, -10, -10, -20],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [-10, 0, 5, 10, 10, 5, 0, -10],
    [-10, 5, 5, 10, 10, 5, 5, -10],
    [-10, 0, 10, 10, 10, 10, 0, -10],
    [-10, 10, 10, 10, 10, 10, 10, -10],
    [-10, 5, 0, 0, 0, 0, 5, -10],
    [-20, -10, -10, -10, -10, -10, -10, -20]
]

rook_table = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [5, 10, 10, 10, 10, 10, 10, 5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [0, 0, 0, 5, 5, 0, 0, 0]
]

queen_table = [
    [-20, -10, -10, -5, -5, -10, -10, -20,],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [10, 0, 5, 5, 5, 5, 0, -10],
    [-5, 0, 5, 5, 5, 5, 0, -5],
    [0, 0, 5, 5, 5, 5, 0, -5],
    [-10, 5, 5, 5, 5, 5, 0, -10],
    [-10, 0, 5, 0, 0, 0, 0, -10],
    [-20, -10, -10, -5, -5, -10, -10, -20]
]

king_table = [
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-20, -30, -30, -40, -40, -30, -30, -20],
    [-10, -20, -20, -20, -20, -20, -20, -10],
    [20, 20, 0, 0, 0, 0, 20, 20],
    [20, 30, 10, 0, 0, 10, 30, 20]
]
