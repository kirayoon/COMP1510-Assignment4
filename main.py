def print_grid(board):
    for row in range(10):
        print(" +---+---+---+---+---+---+---+---+---+---+")
        for col in range(10):
            print(" |", board[row][col], end="")
        print(' |', end="\n")
    print(" +---+---+---+---+---+---+---+---+---+---+")


def create_board():
    return [[u"\u25A1" for _ in range(10)] for _ in range(10)]


def main():
    board = create_board()
    print_grid(board)


if __name__ == '__main__':
    main()
