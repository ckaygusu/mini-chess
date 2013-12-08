import Rook
import Bishop


Queen = Rook.Rook


rays = Rook.rays + Bishop.rays

if __name__ == "__main__":
    # test time, bitches
    board = [list("0000"),
             list("0000"),
             list("00K0"),
             list("0000"),
             list("0Qq0")]
    movement = (1, 1)
    pieceindex = (3, 2)
    pos = (4, 3)
    white_turn = True
    king_pos = (2, 2)

    assert Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 1

    board = [list("0000"),
             list("0000"),
             list("0K0q"),
             list("00Q0"),
             list("0000")]
    movement = (1, 0)
    pieceindex = (2, 2)
    pos = (3, 2)
    white_turn = True
    king_pos = (2, 1)
    assert Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 2

    board = [list("00K0"),
             list("0000"),
             list("00Q0"),
             list("0000"),
             list("00q0")]
    movement = (1, 0)
    pieceindex = (1, 2)
    pos = (2, 2)
    white_turn = True
    king_pos = (0, 2)
    assert not Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 3

    board = [list("00K0"),
             list("0000"),
             list("0000"),
             list("Q000"),
             list("00q0")]
    movement = (2, -1)
    pieceindex = (1, 2)
    pos = (3, 0)
    white_turn = True
    king_pos = (0, 2)
    assert Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 4

    board = [list("00K0"),
             list("0000"),
             list("0000"),
             list("Q0r0"),
             list("00q0")]
    movement = (2, -1)
    pieceindex = (1, 2)
    pos = (3, 0)
    white_turn = True
    king_pos = (0, 2)
    assert Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 5

    board = [list("00K0"),
             list("0000"),
             list("00p0"),
             list("Q0r0"),
             list("00q0")]
    movement = (2, -1)
    pieceindex = (1, 2)
    pos = (3, 0)
    white_turn = True
    king_pos = (0, 2)
    assert not Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 6

    board = [list("00K0"),
             list("0000"),
             list("00R0"),
             list("Q0r0"),
             list("00q0")]
    movement = (2, -1)
    pieceindex = (1, 2)
    pos = (3, 0)
    white_turn = True
    king_pos = (0, 2)
    assert not Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 7

    board = [list("00K0"),
             list("0000"),
             list("0000"),
             list("Q0r0"),
             list("00q0")]
    movement = (2, -1)
    pieceindex = (1, 2)
    pos = (3, 0)
    white_turn = True
    king_pos = (0, 2)
    assert Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 8

    board = [list("0000"),
             list("0000"),
             list("00K0"),
             list("0000"),
             list("qQ00")]
    movement = (1, 0)
    pieceindex = (3, 1)
    pos = (4, 1)
    white_turn = True
    king_pos = (2, 2)
    assert Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 9

    board = [list("0000"),
             list("000q"),
             list("0Q00"),
             list("0000"),
             list("K000")]
    movement = (-1, 0)
    pieceindex = (3, 1)
    pos = (2, 1)
    white_turn = True
    king_pos = (4, 0)
    assert Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 10

    board = [list("rqkr"),
             list("p0pp"),
             list("qPQ0"),
             list("P0PP"),
             list("R0KR")]
    movement = (-1, 1)
    pieceindex = (3, 1)
    pos = (2, 2)
    white_turn = True
    king_pos = (4, 2)
    assert Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 11

    board = [list("00k0"),
             list("0000"),
             list("0000"),
             list("q000"),
             list("00Q0")]
    movement = (2, -1)
    pieceindex = (1, 2)
    pos = (3, 0)
    white_turn = False
    king_pos = (0, 2)
    assert Queen.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 12
