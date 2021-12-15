import config

class Piece():
    def __init__(self, color="") -> None:
        self.color = color
        self.img = ''

    def __str__(self) -> str:
        return f"Empty square"


class Rook(Piece):
    value = 5
    size = (100, 100)

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        if color == 'white':
            self.img = config.WHITE_ROOK
        else:
            self.img = config.BLACK_ROOK

    def __str__(self) -> str:
        return f"{self.color} Rook"


class Knight(Piece):
    value = 3
    size = (100,100)

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        if color == 'white':
            self.img = config.WHITE_KNIGHT
        else:
            self.img = config.BLACK_KNIGHT

    def __str__(self) -> str:
        return f"{self.color} Knight"


class Bishop(Piece):
    value = 3
    size = (100,100)

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
    size = (100, 100)

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
    size = (100, 100)

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
    size = (100, 90)

    def __init__(self, color) -> None:
        super().__init__(color)
        self.color = color
        if color == 'white':
            self.img = config.WHITE_KING
        else:
            self.img = config.BLACK_KING

    def __str__(self) -> str:
        return f"{self.color} King"
