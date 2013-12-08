from utils import within_boundaries

def rook_ray1():
    for i in range(1, 6):
        yield i, 0

def rook_ray2():
    for i in range(1, 6):
        yield -i, 0

def rook_ray3():
    for i in range(1, 6):
        yield 0, i

def rook_ray4():
    for i in range(1, 6):
        yield 0, -i

BLACK_PIECES = "kqrp"
WHITE_PIECES = "KQRP"


class Rook:
    @staticmethod
    def is_valid_movement(board, movement, pieceindex, pos, white_turn):
        opposite_pieces = BLACK_PIECES if white_turn else WHITE_PIECES
        own_pieces = WHITE_PIECES if white_turn else BLACK_PIECES

        if not 0 <= pos[0] < 5 or not 0 <= pos[1] < 4:  # out of bounds
            return False
        elif board[pos[0]][pos[1]] in own_pieces:  # can't attack own pieces
            return False
        return True

    @staticmethod
    def is_capturing_movement(board, movement, pieceindex, pos, white_turn):
        opposite_pieces = BLACK_PIECES if white_turn else WHITE_PIECES
        if board[pos[0]][pos[1]] in opposite_pieces:
            return True
        else:
            return False

    @staticmethod
    def leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos):
        opposite_rook = "r" if white_turn else "R"
        opposite_queen = "q" if white_turn else "Q"
        fearsome_pieces = opposite_rook + opposite_queen
        if king_pos[0] - pieceindex[0] == 0 and king_pos[0] - pos[0] != 0:  # first in the same row, then moves away
            for i in range(1, 5):
                posy = king_pos[0]
                posx = king_pos[1] + i
                if not within_boundaries(posy, posx):
                    break
                else:
                    if board[posy][posx] in opposite_queen+opposite_rook:
                        return True
                    elif board[posy][posx] == "0":
                        continue
                    else:
                        break
            for i in range(1, 5):
                posy = king_pos[0]
                posx = king_pos[1] - i
                if not within_boundaries(posy, posx):
                    break
                else:
                    if board[king_pos[0]][king_pos[1]-i] in fearsome_pieces:
                        return True
                    elif board[king_pos[0]][king_pos[1]-i] == "0":
                        continue
                    else:  # implicit rejection means found a non-attacking piece
                        break
        elif king_pos[1] - pieceindex[1] == 0 and king_pos[1] - pos[1] != 0:  # in the same column, then moves away
            for i in range(1, 6):
                posy = king_pos[0] + i
                posx = king_pos[1]
                if not within_boundaries(posy, posx):
                    break
                else:
                    if board[posy][posx] in fearsome_pieces:
                        return True
                    elif board[posy][posx] == "0":
                        continue
                    else:
                        break
            for i in range(1, 6):
                posy = king_pos[0] - i
                posx = king_pos[1]
                if not within_boundaries(posy, posx):
                    break
                else:
                    if board[king_pos[0]-i][king_pos[1]] in fearsome_pieces:
                        return True
                    elif board[king_pos[0]-i][king_pos[1]] == "0":
                        continue
                    else:
                        break
        elif pieceindex[0] - king_pos[0] == pieceindex[1] - king_pos[1] \
        and pos[0] - king_pos[0] != pos[1] - king_pos[1]:  # first and third quadrant
            for i in range(1, 5):
                posy = king_pos[0] + i
                posx = king_pos[1] + i
                if not within_boundaries(posy, posx):
                    break
                else:
                    if board[posy][posx] == opposite_queen:
                        return True
                    elif board[posy][posx] == "0":
                        continue
                    else:
                        break
            for i in range(1, 5):
                posy = king_pos[0] - i
                posx = king_pos[1] - i
                if not within_boundaries(posy, posx):
                    break
                try:
                    if board[posy][posx] == opposite_queen:
                        return True
                    elif board[posy][posx] == "0":
                        continue
                    else:
                        break
                except IndexError:
                    break
        elif pieceindex[0] - king_pos[0] == -(pieceindex[1] - king_pos[1]) \
        and pos[0] - king_pos[0] != -(pos[1] - king_pos[1]):  # second and fourth quadrant
            for i in range(1, 5):
                posy = king_pos[0] + i
                posx = king_pos[1] - i
                if not within_boundaries(posy, posx):
                    break
                else:
                    if board[posy][posx] == opposite_queen:
                        return True
                    elif board[posy][posx] == "0":
                        continue
                    else:
                        break
            for i in range(1, 5):
                posy = king_pos[0] - i
                posx = king_pos[1] + i
                if not within_boundaries(posy, posx):
                    break
                try:
                    if board[posy][posx] == opposite_queen:
                        return True
                    elif board[posy][posx] == "0":
                        continue
                    else:
                        break
                except IndexError:
                    break

        return False

rays = [rook_ray1, rook_ray2, rook_ray3, rook_ray4]

if __name__ == "__main__":
    board = [list("0000"),
             list("0000"),
             list("00K0"),
             list("0R00"),
             list("00q0")]
    movement = (0, -1)
    pieceindex = (3, 2)
    pos = (3, 1)
    white_turn = True
    king_pos = (2, 2)

    assert Rook.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 1
