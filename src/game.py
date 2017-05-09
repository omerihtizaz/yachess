from random import choice

import board
import computer
import player


class Game:
    def __init__(self):
        self.board = board.Board()
        self.player_is_white = choice([True, False])

    def start(self):
        if self.player_is_white:
            print("\nYou play as white.\n")
        else:
            print("\nYou play as black.\n")

        self.board.print()

        if not self.player_is_white:
            computer.Computer(self.board).move()

        while True:
            player.Player(self.board).move()
            computer.Computer(self.board).move()

Game().start()
