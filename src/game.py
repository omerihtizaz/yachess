from random import choice
from time import sleep

import board


class Game:
    def __init__(self):
        self.board = board.Board()
        self.player_white = choice([True, False])

    def __player_move__(self):
        while True:
            move = input("\nIt's your move. ")

            try:
                self.board.push_san(move)
            except ValueError:
                print("Wrong move, try again.")
            else:
                break

        print()
        self.board.print()

    def start(self):
        if self.player_white:
            print("You play as white.\n")
        else:
            print("You play as black.\n")

        self.board.print()

        if not self.player_white:
            self.board.computer_move()

        while True:
            self.__player_move__()
            self.board.computer_move()
