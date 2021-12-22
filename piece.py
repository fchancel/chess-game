import config


class Piece():
    def __init__(self, color="") -> None:
        self.color = color
        self.img = ''
        self.name = 'EMPTY'

    def __str__(self) -> str:
        return self.name


class Rook(Piece):
    value = 5

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        self.name = "ROOK"
        first_move = True
        if color == 'white':
            self.img = config.WHITE_ROOK
        else:
            self.img = config.BLACK_ROOK
        print(self.name)

    def __str__(self) -> str:
        return f"{self.color} Rook"

    def move_possibility(self, position, board, color=None, checkmate_move=False):
        if color == None:
            color = self.color
        lst_position_vertical = []
        lst_position_horizontal = []
        bool_vertical = True
        bool_horizontal = True

        for i in range(0, 8):
            # VERTICAL MOVE POSSIBILITY
            if bool_vertical and i != position[0]:
                if not board.is_empty_square((i, position[1])):
                    if i < position[0]:
                        lst_position_vertical = []
                    else:
                        bool_vertical = False
                    if board.get_color_pawn((i, position[1])) != color or checkmate_move:
                        lst_position_vertical.append((i, position[1]))
                else:
                    lst_position_vertical.append((i, position[1]))

            # HORIZONTAL MOVE POSSIBILITY
            if bool_horizontal and i != position[1]:
                if not board.is_empty_square((position[0], i)):
                    if i < position[1]:
                        lst_position_horizontal = []
                    else:
                        bool_horizontal = False
                    if board.get_color_pawn((position[0], i)) != color or checkmate_move:
                        lst_position_horizontal.append((position[0], i))
                else:
                    lst_position_horizontal.append((position[0], i))

        return lst_position_horizontal + lst_position_vertical


class Knight(Piece):
    value = 3

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        self.name = "KNIGHT"
        if color == 'white':
            self.img = config.WHITE_KNIGHT
        else:
            self.img = config.BLACK_KNIGHT

    def __str__(self) -> str:
        return f"{self.color} Knight"

    def move_possibility(self, position, board, color=None, checkmate_move=False):
        if color == None:
            color = self.color
        possibility = [(-2, -1), (-2, 1), (-1, -2), (1, -2),
                       (2, -1), (2, 1), (-1, 2), (1, 2)]
        lst_position = []
        for elt in possibility:
            if (position[0] + elt[0] >= 0 and position[0] + elt[0] <= 7) and (position[1] + elt[1] >= 0 and position[1] + elt[1] <= 7):
                if checkmate_move:
                    lst_position.append(
                        (position[0] + elt[0], position[1] + elt[1]))
                elif board.get_color_pawn((position[0] + elt[0], position[1] + elt[1])) != color:
                    lst_position.append(
                        (position[0] + elt[0], position[1] + elt[1]))

        return lst_position


class Bishop(Piece):
    value = 3

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        self.name = "BISHOP"
        if color == 'white':
            self.img = config.WHITE_BISHOP
        else:
            self.img = config.BLACK_BISHOP

    def __str__(self) -> str:
        return f"{self.color} Bishop"

    def move_possibility(self, position, board, color=None, checkmate_move=False):
        if color == None:
            color = self.color
        lst_pos_to_r = []
        lst_pos_to_l = []
        bool_right = True
        bool_left = True

        begin_to_r = (position[0] - position[1])
        if begin_to_r < 0:
            begin_to_r = (0, abs(begin_to_r))
        else:
            begin_to_r = (begin_to_r, 0)

        begin_to_l = ((position[0]) - (7 - position[1]))
        if begin_to_l < 0:
            begin_to_l = [0, 7 - abs(begin_to_l)]
        else:
            begin_to_l = [begin_to_l, 7]

        for i in range(0, 8):
            # TO RIGHT MOVE POSSIBILITY
            if (bool_right and sum(position) != sum(begin_to_r) + (i * 2) and begin_to_r[0] + i <= 7 and begin_to_r[1] + i <= 7):
                if not board.is_empty_square((begin_to_r[0] + i, begin_to_r[1] + i)):
                    if (sum(begin_to_r) + (i*2)) < sum(position):
                        lst_pos_to_r = []
                    else:
                        bool_right = False
                    if board.get_color_pawn((begin_to_r[0] + i, begin_to_r[1] + i)) != color or checkmate_move:
                        lst_pos_to_r.append(
                            (begin_to_r[0] + i, begin_to_r[1] + i))
                else:
                    lst_pos_to_r.append(
                        (begin_to_r[0] + i, begin_to_r[1] + i))

            # TO LEFT MOVE POSSIBILITY
            if (bool_left and (begin_to_l[0] + i != position[0] and begin_to_l[1] - i != position[1]) and begin_to_l[0] + i <= 7 and begin_to_l[1] - i >= 0):
                if not board.is_empty_square((begin_to_l[0] + i, begin_to_l[1] - i)):
                    if begin_to_l[1] - i > position[1]:
                        lst_pos_to_l = []
                    else:
                        bool_left = False
                    if board.get_color_pawn((begin_to_l[0] + i, begin_to_l[1] - i)) != color or checkmate_move:
                        lst_pos_to_l.append(
                            (begin_to_l[0] + i, begin_to_l[1] - i))
                else:
                    lst_pos_to_l.append(
                        (begin_to_l[0] + i, begin_to_l[1] - i))

        return lst_pos_to_r + lst_pos_to_l


class Queen(Piece):
    value = 9

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        self.name = "QUEEN"
        if color == 'white':
            self.img = config.WHITE_QUEEN
        else:
            self.img = config.BLACK_QUEEN

    def __str__(self) -> str:
        return f"{self.color} Queen"

    def move_possibility(self, position, board, color=None, checkmate_move=False):
        if color == None:
            color = self.color
        lst_position_rook = Rook.move_possibility(
            None, position, board, color, checkmate_move)
        lst_position_bishop = Bishop.move_possibility(
            None, position, board, color, checkmate_move)
        return lst_position_rook + lst_position_bishop


class King(Piece):
    value = 0

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        self.name = "KING"
        if color == 'white':
            self.img = config.WHITE_KING
        else:
            self.img = config.BLACK_KING

    def __str__(self) -> str:
        return f"{self.color} King"

    def move_possibility(self, position, board, color=None, checkmate_move=False):
        if color == None:
            color = self.color
        lst_position = []
        lst_posibility = [(-1, -1), (-1, 0), (-1, 1), (1, 0),
                          (1, 1), (0, 1), (1, -1), (0, -1)]
        for pos in lst_posibility:
            if (position[0] + pos[0] >= 0 and position[0] + pos[0] <= 7) and (position[1] + pos[1] >= 0 and position[1] + pos[1] <= 7):
                if checkmate_move:
                    lst_position.append(
                        (position[0] + pos[0], position[1] + pos[1]))
                elif board.get_color_pawn((position[0] + pos[0], position[1] + pos[1])) != color:
                    lst_position.append(
                        (position[0] + pos[0], position[1] + pos[1]))

        # CHECK IF MOVE IS POSSIBLE WITHOUT CHECKMATE
        if board.color_play != color:
            adv_color = 'white' if color == "black" else "black"
            all_pos_adv = board.all_move_possibility(adv_color, True)
            n_lst = []
            for pos in lst_position:
                if not pos in all_pos_adv:
                    n_lst.append(pos)
            return n_lst
        return lst_position


class Pawn(Piece):
    value = 1

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        self.first_move = False
        self.name = "PAWN"
        if color == 'white':
            self.img = config.WHITE_PAWN
        else:
            self.img = config.BLACK_PAWN

    def __str__(self) -> str:
        return f"{self.color} Pawn"

    def move_possibility(self, position, board, color=None):
        if color == None:
            color = self.color
        if self.color == 'white':
            value = -1
        else:
            value = 1
        lst_position = [(position[0] + value, position[1]), (position[0] +
                                                             value, position[1] - 1), (position[0] + value, position[1] + 1)]
        if self.first_move == False:
            lst_position.append((position[0] + value * 2, position[1]))
        return lst_position

    def change_first_move(self):
        self.first_move = True
