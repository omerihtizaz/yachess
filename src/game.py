from random import choice

import board
import computer
import player


class Game:
    def __init__(self):
        self.board = board.Board()
        self.is_player_white = choice([True, False])

    def start(self):
        if self.is_player_white:
            print("\nYou play as white.\n")
        else:
            print("\nYou play as black.\n")

        self.board.print()

        if not self.is_player_white:
            computer.Computer(self.board, self.is_player_white).move()

        while True:
            player.Player(self.board).move()
            computer.Computer(self.board, self.is_player_white).move()

Game().start()
