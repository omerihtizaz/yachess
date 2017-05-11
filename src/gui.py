import tkinter
from PIL import ImageTk

import chess


class Gui(tkinter.Frame):
    pieces = {}
    icons = {}

    white = "white"
    black = "grey"

    rows = 8
    columns = 8

    square_size = 64

    def __init__(self, parent, board):
        self.board = board
        self.parent = parent

        tkinter.Frame.__init__(self, parent)

        canvas_width = self.columns * self.square_size
        canvas_height = self.rows * self.square_size

        self.canvas = tkinter.Canvas(
            self, width=canvas_width, height=canvas_height, background="grey")
        self.canvas.pack(side="top", fill="both", anchor="c", expand=True)

    def draw_pieces(self):
        self.canvas.delete("piece")

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)

            if piece is not None:
                image_name = "img/%s.png" % (piece.symbol())
                piece_name = "%s%s" % (piece.symbol(), square)

                if image_name not in self.icons:
                    self.icons[image_name] = ImageTk.PhotoImage(
                        file=image_name, width=32, height=32)

                self.add_piece(piece_name, self.icons[image_name], square // 8,
                               square % 8)
                self.place_piece(piece_name, square // 8, square % 8)

    def add_piece(self, name, image, row=0, column=0):
        self.canvas.create_image(
            0, 0, image=image, tags=(name, "piece"), anchor="c")
        self.place_piece(name, row, column)

    def place_piece(self, name, row, column):
        self.pieces[name] = (row, column)

        true_row = (column * self.square_size) + int(self.square_size / 2)
        true_column = ((7 - row) * self.square_size) + int(self.square_size / 2)
        self.canvas.coords(name, true_row, true_column)


def display(board):
    root = tkinter.Tk()
    root.title("Yachess")

    gui = Gui(root, board)
    gui.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    gui.draw_pieces()

    root.mainloop()


BOARD = chess.Board()
display(BOARD)
