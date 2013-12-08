from utils import within_boundaries

# Yeah I know, I'm committing one of the unholy sins of programming.


class Pawn:
    @staticmethod
    def leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos):
        opposite_queen = "q" if white_turn else "Q"
        if pieceindex[0] - king_pos[0] == pieceindex[1] - king_pos[1] \
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


if __name__ == "__main__":
    board = [list("0000"),
             list("0Pq0"),
             list("0000"),
             list("K000"),
             list("0000")]
    movement = (-1, 0)
    pieceindex = (2, 1)
    pos = (1, 1)
    white_turn = True
    king_pos = (3, 0)

    assert Pawn.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 1

    board = [list("0000"),
             list("0pQ0"),
             list("0000"),
             list("k000"),
             list("0000")]
    movement = (-1, 0)
    pieceindex = (2, 1)
    pos = (1, 1)
    white_turn = False
    king_pos = (3, 0)

    assert Pawn.leaves_king_in_check(board, movement, pieceindex, pos, white_turn, king_pos)  # 1
