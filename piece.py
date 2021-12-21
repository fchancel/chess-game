import config


class Piece():
    def __init__(self, color="") -> None:
        self.color = color
        self.img = ''

    def __str__(self) -> str:
        return f"Empty"

    def is_empty_square(self):
        if self.__str__() == 'Empty':
            return True
        else:
            return False


class Rook(Piece):
    value = 5

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        if color == 'white':
            self.img = config.WHITE_ROOK
        else:
            self.img = config.BLACK_ROOK

    def __str__(self) -> str:
        return f"{self.color} Rook"

    def move_possibility(self, position):
        lst_position = []
        for i in range(0, 8):
            if i != position[0]:
                lst_position.append((i, position[1]))
            if i != position[1]:
                lst_position.append((position[0], i))
        return lst_position


class Knight(Piece):
    value = 3

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
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
        lst_position = [(position[0] + value, position[1]), (position[0] + value , position[1] - 1), (position[0] + value , position[1] + 1)]
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
