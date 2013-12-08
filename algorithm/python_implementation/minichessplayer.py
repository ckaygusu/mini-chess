import sys
from board import Board

BOARD_CHARS = "KQRPkqrp0"

def main(argv):
    assert len(argv) == 5, "Invalid number of argv {}".format(len(argv))
    assert argv[1] == "-b" and argv[3] == "-wt", "Invalid structure of argv values. {}".format(argv)
    assert len(argv[2]) == 20, "Board representation length is incorrect. {}".format(len(argv[2]))
    for elem in argv[2]:
        assert elem in BOARD_CHARS, "Invalid character in board representation: {}".format(elem)
    assert argv[4] in "01", "Invalid indicator of turn: {}".format(argv[3])

    b = Board(argv[2], int(argv[4]))
    nb = b.generate_boards()

    for b in nb:
        print b
        print
    print len(nb)

    return 0


if __name__ == "__main__":
    retval = main(sys.argv)
    exit(retval)