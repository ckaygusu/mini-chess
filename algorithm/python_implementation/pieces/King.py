import Rook
import Bishop

BLACK_PIECES = "kqrp"
WHITE_PIECES = "KQRP"


class King:
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
    def is_checked(board, king_pos):
        white_turn = True if board[king_pos[0]][king_pos[1]] == "K" else False
        opposite_rook = "R" if white_turn else "r"
        opposite_queen = "Q" if white_turn else "q"
        opposite_pawn = "P" if white_turn else "p"
        pawn_direction = -1 if white_turn else 1

        try: # Determine if checked by opposite pawns
            if board[king_pos[0] + pawn_direction][king_pos[1] + 1] == opposite_pawn:
                return True
        except IndexError:
            pass
        try:
            if board[king_pos[0] + pawn_direction][king_pos[1] - 1] == opposite_pawn:
                return True
        except IndexError:
            pass

        for ray in Rook.rays:
            for movement in ray():
                posy = king_pos[0] + movement[0]
                posx = king_pos[1] + movement[1]
                try:
                    elem = board[posy][posx]
                except IndexError:
                    break
                if elem == opposite_rook or elem == opposite_queen:
                    return True
                elif elem == "0":
                    continue
                else:
                    break

        for ray in Bishop.rays:
            for movement in ray():
                posy = king_pos[0] + movement[0]
                posx = king_pos[1] + movement[1]
                try:
                    elem = board[posy][posx]
                except IndexError:
                    break
                if elem == opposite_queen:
                    return True
                elif elem == "0":
                    continue
                else:
                    break

        return True


moves = [(0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1,),
    (-1, 1),
    (1, -1),
    (-1, -1)]