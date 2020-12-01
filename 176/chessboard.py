WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""

    board = """"""

    for row in range(size):
        for column in range(size):
            if row % 2 == 0:
                board += WHITE if column % 2 == 0 else BLACK
            else:
                board += WHITE if column % 2 == 1 else BLACK
        board += '\n'
    print(board)
