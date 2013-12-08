from pieces import Bishop
from pieces import King
from pieces import Pawn
from pieces import Queen
from pieces import Rook

WHITE_PIECES = "KRPQ"
BLACK_PIECES = "kprq"


class Board:
    def __init__(self, brd, trn):
        self.boardstring = brd
        self.turn = trn

    def _get_piece_index(self, board, piece):
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if piece == elem:
                    return i, j

    def _leaves_king_in_check(self, board, move, pieceindex, pos):
        return False
        k = "Q" if self.turn else "q"
        coords = self._get_piece_index(k)

        #  on the same file and goese to other file
        if pieceindex[1] == coords[1] and pos[1] != coords[1]:
            pass  # TODO

    def _move_is_valid(self, board, move, pieceindex):
        pos = pieceindex[0] + move[0], pieceindex[1] + move[1]
        if not 0 <= pos[0] < 5 or not 0 <= pos[1] < 4:  # out of bounds
            return False
        elif board[pos[0]][pos[1]] != "0":  # place is occupied
            return False
        elif self._leaves_king_in_check(board, move, pieceindex, pos):
            return False
        else:
            return True

    def _add_new_board(self, board, move, pieceindex):
        nbs = list(self.boardstring)
        nbt = 0 if self.turn else 1

        src = pieceindex[0]*4 + pieceindex[1]
        dst = src + move[0]*4 + move[1]

        p = nbs[src]
        nbs[src] = "0"
        nbs[dst] = p

        board.append(Board("".join(nbs), nbt))

    def _move_is_capturing(self, board, mv, pieceindex):
        pass


    def generate_boards(self):
        if self.turn:
            own_pieces = WHITE_PIECES
            pawn_move = (-1, 0)
        else:
            own_pieces = BLACK_PIECES
            pawn_move = (1, 0)

        board = [list(self.boardstring[:4]),
                 list(self.boardstring[4:8]),
                 list(self.boardstring[8:12]),
                 list(self.boardstring[12:16]),
                 list(self.boardstring[16:20])]

        new_boards = []

        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem not in own_pieces:
                    continue
                else:
                    e = elem.lower()
                    if e == "k":  # handle king movements
                        for mv in King.moves:
                            if
                    elif e == "q":  # handle queen movements
                        for ray in Queen.rays:
                            for mv in ray():
                                if self._move_is_valid(board, mv, (i, j)):
                                    self._add_new_board(new_boards, mv, (i, j))
                                    if self._move_is_capturing(board, mv, (i, j)):
                                        break
                                else:
                                    break
                    elif e == "r":  # handle rook movements
                        for ray in Rook.rays:
                            for mv in ray():
                                if self._move_is_valid(board, mv, (i, j)):
                                    self._add_new_board(new_boards, mv, (i, j))
                                    if self._move_is_capturing(board, mv, (i, j)):
                                        break
                                else:
                                    break
                    elif e == "p":  # handle pawn movements
                        if self._move_is_valid(board, pawn_move, (i, j)):
                            self._add_new_board(new_boards, pawn_move, (i, j))
                        if self._move_is_valid(board, (pawn_move[0], 1), (i, j)):
                            self._add_new_board(new_boards, (pawn_move[0], 1), (i, j))
                        if self._move_is_valid(new_boards, (pawn_move[0], -1), (i, j)):
                            self._add_new_board(new_boards, (pawn_move[0], -1), (i, j))
                    else:
                        raise Exception("Invalid piece in the board {}".format(e))

        return new_boards

    def __str__(self):
        return "%s\n%s\n%s\n%s\n%s" % (self.boardstring[:4], self.boardstring[4:8], self.boardstring[8:12],
                                       self.boardstring[12:16], self.boardstring[16:20])