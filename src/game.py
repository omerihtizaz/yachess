import tkinter as tk
from random import choice

import board
import computer
import gui


class Game:
    def __init__(self):
        self.board = board.Board()
        self.player_turns = [choice([True, False])]

        self.root = tk.Tk()
        self.root.title('Yachess')

        self.display = gui.Gui(self.root, self, self.board, self.player_turns)
        self.display.pack(
            side='top', fill='both', expand='true', padx=4, pady=4)

    def start(self):
        if self.player_turns[-1]:
            print("\nYou play as white.\n")

            self.root.after(100, self.player_play)
        else:
            print("\nYou play as black.\n")

            self.root.after(100, self.computer_play)

        self.board.print()

        self.root.mainloop()

    def player_play(self):
        print("\nPlayer's turn\n")

        # wait as long as possible for player's input
        self.root.after(100000000, self.computer_play)

    def computer_play(self):
        print("Computer's turn\n")

        computer.Computer(self.board, self.player_turns).computer_move()

        self.player_turns.append(True)

        self.display.refresh()
        self.display.draw_pieces()

        self.root.after(100, self.player_play)


Game().start()
