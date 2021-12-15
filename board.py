from piece import Piece, Rook, Bishop, Knight, Pawn, King, Queen
import config

class Board():
    board_img = config.BOARD

    def __init__(self) -> None:
        self.square = [
            [Rook('black'), Knight('black'), Bishop('black'), Queen('black'),
             King('black'), Bishop('black'), Knight('black'), Rook('black')],
            [Pawn('black')] * 8,

            [Piece()] * 8,
            [Piece()] * 8,
            [Piece()] * 8,
            [Piece()] * 8,

            [Pawn('white')] * 8,
            [Rook('white'), Knight('white'), Bishop('white'), Queen('white'),
             King('white'), Bishop('white'), Knight('white'), Rook('white')],
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

    def get_color_play(self) -> str:
        return self.color_play

    def change_color_play(self) -> str:
        if self.color_play == 'white':
            self.color_play = "black"
        else:
            self.color_play = "white"
