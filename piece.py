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
        if color == 'white':
            self.img = config.WHITE_ROOK
        else:
            self.img = config.BLACK_ROOK
        print(self.name)

    def __str__(self) -> str:
        return f"{self.color} Rook"

    def move_possibility(self, position, board):
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
                    if board.get_color_pawn((i, position[1])) != self.color and not board.is_adv_king((i, position[1]), self.color):
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
                    if board.get_color_pawn((position[0], i)) != self.color and not board.is_adv_king((position[0], i), self.color):
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

    def move_possibility(self, position):
        possibility = [(-2, -1), (-2, 1), (-1, -2), (1, -2),
                       (2, -1), (2, 1), (-1, 2), (1, 2)]
        lst_position = []
        for elt in possibility:
            if (position[0] + elt[0] >= 0 and position[0] + elt[0] <= 7) and (position[1] + elt[1] >= 0 and position[1] + elt[1] <= 7):
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

    def move_possibility(self, position):
        lst_position = []
        for i in range(1, 8):
            if position[0] - i >= 0 and position[1] - i >= 0:
                lst_position.append((position[0] - i, position[1] - i))
            if position[0] + i <= 7 and position[1] + i <= 7:
                lst_position.append((position[0] + i, position[1] + i))
            if position[0] - i >= 0 and position[1] + i <= 7:
                lst_position.append((position[0] - i, position[1] + i))
            if position[0] + i <= 7 and position[1] - i >= 0:
                lst_position.append((position[0] + i, position[1] - i))
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

    def move_possibility(self, position):
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

    def move_possibility(self, position):
        lst_position_rook = Rook.move_possibility(None, position)
        lst_position_bishop = (Bishop.move_possibility(None, position))
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

    def move_possibility(self, position):
        lst_position = []
        lst_posibility = [(-1, -1), (-1, 0), (-1, 1), (1, 0),
                          (1, 1), (0, 1), (1, -1), (0, -1)]
        for pos in lst_posibility:
            if (position[0] + pos[0] >= 0 and position[0] + pos[0] <= 7) and (position[1] + pos[1] >= 0 and position[1] + pos[1] <= 7):
                lst_position.append(
                    (position[0] + pos[0], position[1] + pos[1]))
        return lst_position
