from random import randint
from time import sleep

class Computer:
    def __init__(self, board):
        self.board = board

    def move(self):
        print("\nComputer is thinking...\n")
        sleep(2)

        moves = []

        for move in self.board.legal_moves():
            moves.append(move);

        chosen_move = moves[randint(0, len(moves) - 1)]
        self.board.push(chosen_move)

        self.board.print()
