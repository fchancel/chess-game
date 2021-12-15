import config


class Piece():
    def __init__(self, color="") -> None:
        self.color = color
        self.img = ''

    def __str__(self) -> str:
        return f"Empty square"


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
        possibility = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]
        lst_position = []
        for elt in possibility:
            if (position[0] + elt[0] >= 0 and position[0] + elt[0] <= 7) and (position[1] + elt[1] >= 0 and position[1] + elt[1] <= 7):
                lst_position.append((position[0] + elt[0], position[1] + elt[1]))
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


class Pawn(Piece):
    value = 1

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        if color == 'white':
            self.img = config.WHITE_PAWN
        else:
            self.img = config.BLACK_PAWN

    def __str__(self) -> str:
        return f"{self.color} Pawn"


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
