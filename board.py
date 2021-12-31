from piece import Piece, Rook, Bishop, Knight, Pawn, King, Queen
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
        self.color_play = "white"
        self.nb_hit = 0
        self.nb_hit_since_last_eat = 0
        self.last_move_piece = None
        self.last_move_old_position = None
        self.last_move_new_position = None

    def change_color_play(self) -> None:
        """
        Change the color of the current player
        """
        if self.color_play == 'white':
            self.color_play = "black"
        else:
            self.color_play = "white"

    def is_empty_square(self, position: tuple) -> bool:
        """
        Checks if the square concerned by the position is empty
        """
        if self.square[position[0]][position[1]].name != 'EMPTY':
            return False
        return True

    def get_color_pawn(self, position: tuple) -> str:
        """
        Returns the color of the Piece associated with the position

        keyword arguments:
        position -- pawn position to check
        """
        return self.square[position[0]][position[1]].color

    def all_move_possibility(self, color: str, check_move: bool = False) -> list:
        """
        Retrieves all square that can be controlled by a color

        keyword arguments:
        color -- color of the parts
        check_move -- option to also check for forbidden moves for the opponent king
        """
        lst_position = []
        for i, row in enumerate(self.square):
            for j, piece in enumerate(row):
                if piece.name == 'KING' and piece.color == color:
                    lst_position += piece.move_possibility(
                        board=self, color=piece.color, check_move=check_move, recursive_call=True)
                elif piece.color == color:
                    lst_position += piece.move_possibility(
                        board=self, color=piece.color, check_move=check_move)
        return lst_position

    def is_attacked(self, position: tuple) -> bool:
        """
        Checks if a position is under attack

        keyword arguments:
        position -- position to be checked for the attack
        """
        lst_all_possibility = self.all_move_possibility(self.color_adv(), True)
        if position in lst_all_possibility:
            return True
        return False

    def all_deselect_piece(self) -> None:
        """
        Deselects all pieces on the board
        """
        for row in self.square:
            for piece in row:
                piece.selected = False

    def piece_selected(self):
        """
        Checks if a part is selected.
        If yes, returns the part
        If no, returns None
        """
        for row in self.square:
            for piece in row:
                if piece.selected:
                    return piece
        return None

    def color_adv(self) -> str:
        """
        Return the opponent's color
        """
        if self.color_play == "white":
            return 'black'
        return 'white'

    def is_check(self) -> bool:
        """
        Check if the king is in check
        """
        lst_move_adv = self.all_move_possibility(self.color_adv(), True)
        for row in self.square:
            for piece in row:
                if piece.name == "KING" and piece.color == self.color_play:
                    if piece.position in lst_move_adv:
                        return True
        return False

    def move_authorized(self, piece: Piece) -> list:
        """
        Checks the allowed moves for a piece according to the king's check

        keyword arguments:
        piece -- selectionned piece
        """
        lst_move_possibility = piece.move_possibility(self)
        squares_copy = copy.deepcopy(self.square)
        n_lst = []
        for move in lst_move_possibility:
            piece.move(self, move, lst_move_possibility)
            if not self.is_check():
                n_lst.append(move)
            self.cancel_last_move()
        self.square = squares_copy
        return n_lst

    def cancel_last_move(self) -> None:
        """
        cancel the last move playing
        """
        if self.last_move_piece != None:
            self.square[self.last_move_old_position[0]][self.last_move_old_position[1]
                                                        ] = self.square[self.last_move_new_position[0]][self.last_move_new_position[1]]
            self.square[self.last_move_new_position[0]
                        ][self.last_move_new_position[1]].position = self.last_move_old_position
            self.square[self.last_move_new_position[0]
                        ][self.last_move_new_position[1]] = self.last_move_piece
