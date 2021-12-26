from piece import Piece, Rook, Bishop, Knight, Pawn, King, Queen
import config
import copy


class Board():

    def __init__(self) -> None:
        self.square = [
            [Rook((0, 0), 'black'), Knight((0, 1), 'black'), Bishop((0, 2), 'black'), Queen((0, 3), 'black'),
             King((0, 4), 'black'), Bishop((0, 5), 'black'), Knight((0, 6), 'black'), Rook((0, 7), 'black')],

            [Pawn((1, 0), 'black'), Pawn((1, 1), 'black'), Pawn((1, 2), 'black'), Pawn((1, 3), 'black'),
             Pawn((1, 4), 'black'), Pawn((1, 5), 'black'), Pawn((1, 6), 'black'), Pawn((1, 7), 'black')],


            [Piece()] * 8,
            [Piece()] * 8,
            [Piece()] * 8,
            [Piece()] * 8,

            [Pawn((6, 0), 'white'), Pawn((6, 1), 'white'), Pawn((6, 2), 'white'), Pawn((6, 3), 'white'),
             Pawn((6, 4), 'white'), Pawn((6, 5), 'white'), Pawn((6, 6), 'white'), Pawn((6, 7), 'white')],

            [Rook((7, 0), 'white'), Knight((7, 1), 'white'), Bishop((7, 2), 'white'), Queen((7, 3), 'white'),
             King((7, 4), 'white'), Bishop((7, 5), 'white'), Knight((7, 6), 'white'), Rook((7, 7), 'white')],
        ]

        self.coord = [
            ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
            ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
            ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
            ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
            ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
            ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
            ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
            ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
        ]
        self.color_play = "white"
        self.nb_hit = 0
        self.white_castling = True
        self.black_castling = True

    def add_hit(self) -> int:
        self.nb_hit += 1
        return self.nb_hit

    def castling_off(self, color) -> None:
        if color == 'white':
            self.white_castling = False
        else:
            self.black_castling = False

    def get_castling(self, color) -> bool:
        if color == "white":
            return self.white_castling
        else:
            return self.black_castling

    def change_color_play(self) -> str:
        if self.color_play == 'white':
            self.color_play = "black"
        else:
            self.color_play = "white"

    def is_empty_square(self, position) -> bool:
        if self.square[position[0]][position[1]].name != 'EMPTY':
            return False
        return True

    def get_color_pawn(self, position):
        return self.square[position[0]][position[1]].color

    def all_move_possibility(self, color, check_move=False):
        print(f'couleur move possibility : {color}')
        lst_position = []
        for i, row in enumerate(self.square):
            for j, piece in enumerate(row):
                if piece.name == 'KING' and piece.color == color:
                    lst_position += piece.move_possibility(
                        (i, j), self, piece.color, check_move, True)
                elif piece.color == color:
                    lst_position += piece.move_possibility(
                        (i, j), self, piece.color, check_move)
        return lst_position

    def is_attacked(self, lst_all_possibility, position):
        for pos in lst_all_possibility:
            if position in lst_all_possibility:
                return True
        return False

    def all_deselect_piece(self):
        for row in self.square:
            for piece in row:
                piece.selected = False

    def piece_selected(self):
        for row in self.square:
            for piece in row:
                if piece.selected:
                    return piece

    def color_adv(self):
        if self.color_play == "white":
            return 'black'
        return 'white'

    def is_check(self):
        lst_move_adv = self.all_move_possibility(self.color_adv(), True)
        for row in self.square:
            for piece in row:
                if piece.name == "KING" and piece.color == self.color_play:
                    if piece.position in lst_move_adv:
                        return True
        return False

    def move_is_check(self, lst_move_possibility, board, piece):
        squares_copy = copy.deepcopy(self.square)
        n_lst = []
        for move in lst_move_possibility:
            piece.move(board, move, lst_move_possibility)
            if not self.is_check():
                n_lst.append(move)

        self.square = squares_copy
        return n_lst