class Player:
    def __init__(self, board):
        self.board = board

    def move(self):
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
