from random import randint
from time import sleep

import chess


class Board:
    def __init__(self):
        self.board = chess.Board()

    def computer_move(self):
        print("\nComputer is thinking...\n")
        sleep(2)

        moves = []

        for move in self.board.legal_moves:
            moves.append(move);

        chosen_move = moves[randint(0, len(moves) - 1)]
        self.board.push(chosen_move)

        self.print()

    def push_san(self, move):
        self.board.push_san(move)

    def print(self):
        print(self.board)
