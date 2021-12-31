
import config


class Piece():
    def __init__(self, position: tuple = (), color: str = "", name: str = 'EMPTY', value=0) -> None:
        """
        Initializes a piece of the chess game.
        If the keyword name is EMPTY, then the square is empty

        Keyword arguments:
        position -- position where the piece is located
        color -- color of the piece
        name -- name of the piece
        """
        self.color = color
        self.img = ''
        self.name = name
        self.selected = False
        self.position = position
        self.value=value

    def __str__(self) -> str:
        return self.name
        

    def move(self, board, new_position: tuple, move_possibility: list) -> None:
        """
        Move a piece on the board

        keyword arguments:
        board -- instance of class Board
        new_position -- new position on the board for the piece
        move_possibility -- list of possible positions for the piece
        """

        if new_position in move_possibility:
            board.last_move_piece = board.square[new_position[0]
                                                 ][new_position[1]]
            board.last_move_old_position = self.position
            board.last_move_new_position = new_position

            board.square[new_position[0]][new_position[1]
                                          ] = board.square[self.position[0]][self.position[1]]
            board.square[self.position[0]][self.position[1]] = Piece()
            self.position = new_position


class Rook(Piece):

    def __init__(self, position, color) -> None:
        super().__init__(position, color, "ROOK", 5)
        self.first_move = True
        if color == 'white':
            self.img = config.WHITE_ROOK
        else:
            self.img = config.BLACK_ROOK

    def __str__(self) -> str:
        return f"{self.color} Rook"

    def move_possibility(self, board, position: tuple = (), color: str = None, check_move: bool = False) -> list:
        """
        Created a list of allowed positions for the Piece

        keyword arguments:
        position -- position of the piece
        board -- instance of the Board class
        color -- color of the piece
        check_move -- option to also check for forbidden moves for the opponent king
        """
        if len(position) == 0:
            position = self.position
        if color == None:
            color = self.color
        lst_position_vertical = []
        lst_position_horizontal = []
        bool_vertical = True
        bool_horizontal = True

        for i in range(0, 8):
            if bool_vertical and i != position[0]:
                if not board.is_empty_square((i, position[1])):
                    if i < position[0]:
                        lst_position_vertical = []
                    else:
                        bool_vertical = False
                    if board.get_color_pawn((i, position[1])) != color or check_move:
                        lst_position_vertical.append((i, position[1]))
                else:
                    lst_position_vertical.append((i, position[1]))

            if bool_horizontal and i != position[1]:
                if not board.is_empty_square((position[0], i)):
                    if i < position[1]:
                        lst_position_horizontal = []
                    else:
                        bool_horizontal = False
                    if board.get_color_pawn((position[0], i)) != color or check_move:
                        lst_position_horizontal.append((position[0], i))
                else:
                    lst_position_horizontal.append((position[0], i))

        return lst_position_horizontal + lst_position_vertical

    def move(self, board, new_position: tuple, move_possibility: list) -> None:
        """
        Move a piece on the board

        keyword arguments:
        board -- instance of class Board
        new_position -- new position on the board for the piece
        move_possibility -- list of possible positions for the piece
        """
        super().move(board, new_position, move_possibility)
        if self.first_move:
            self.first_move = False


class Knight(Piece):

    def __init__(self, position, color) -> None:
        super().__init__(position, color, 'KNIGHT', 3)
        if color == 'white':
            self.img = config.WHITE_KNIGHT
        else:
            self.img = config.BLACK_KNIGHT

    def __str__(self) -> str:
        return f"{self.color} Knight"

    def move_possibility(self,  board, position: tuple = (), color: str = None, check_move: bool = False) -> list:
        """
        Created a list of allowed positions for the Piece

        keyword arguments:
        position -- position of the piece
        board -- instance of the Board class
        color -- color of the piece
        check_move -- option to also check for forbidden moves for the opponent king
        """

        if len(position) == 0:
            position = self.position
        if color == None:
            color = self.color
        possibility = [(-2, -1), (-2, 1), (-1, -2), (1, -2),
                       (2, -1), (2, 1), (-1, 2), (1, 2)]
        lst_position = []
        for elt in possibility:
            if (position[0] + elt[0] >= 0 and position[0] + elt[0] <= 7) and (position[1] + elt[1] >= 0 and position[1] + elt[1] <= 7):
                if check_move:
                    lst_position.append(
                        (position[0] + elt[0], position[1] + elt[1]))
                elif board.get_color_pawn((position[0] + elt[0], position[1] + elt[1])) != color:
                    lst_position.append(
                        (position[0] + elt[0], position[1] + elt[1]))

        return lst_position


class Bishop(Piece):

    def __init__(self, position, color) -> None:
        super().__init__(position, color, 'BISHOP', 3)
        if color == 'white':
            self.img = config.WHITE_BISHOP
        else:
            self.img = config.BLACK_BISHOP

    def __str__(self) -> str:
        # return f"{self.color} Bishop"
        return f"{self.color} Bishop"

    def move_possibility(self, board, position: tuple = (), color: str = None, check_move: bool = False) -> list:
        """
        Created a list of allowed positions for the Piece

        keyword arguments:
        position -- position of the piece
        board -- instance of the Board class
        color -- color of the piece
        check_move -- option to also check for forbidden moves for the opponent king
        """

        if len(position) == 0:
            position = self.position
        if color == None:
            color = self.color
        lst_pos_to_r = []
        lst_pos_to_l = []
        bool_right = True
        bool_left = True

        # SEARCH FOR THE LOWER RIGHT SQUARE WHERE THE BISHOP COULD START
        begin_to_r = (position[0] - position[1])
        if begin_to_r < 0:
            begin_to_r = (0, abs(begin_to_r))
        else:
            begin_to_r = (begin_to_r, 0)

        # SEARCH FOR THE LOWER LEFT SQUARE WHERE THE BISHOP COULD START
        begin_to_l = ((position[0]) - (7 - position[1]))
        if begin_to_l < 0:
            begin_to_l = [0, 7 - abs(begin_to_l)]
        else:
            begin_to_l = [begin_to_l, 7]
        for i in range(0, 8):
            if (bool_right and sum(position) != sum(begin_to_r) + (i * 2) and begin_to_r[0] + i <= 7 and begin_to_r[1] + i <= 7):
                if not board.is_empty_square((begin_to_r[0] + i, begin_to_r[1] + i)):
                    # CHECK IF THE CHECKED SQUARE IS BEFORE THE ORIGINAL POSITION OF THE BISHOP
                    if begin_to_r[0] + i < position[0]:
                        lst_pos_to_r = []
                    else:
                        bool_right = False
                    if board.get_color_pawn((begin_to_r[0] + i, begin_to_r[1] + i)) != color or check_move:
                        lst_pos_to_r.append(
                            (begin_to_r[0] + i, begin_to_r[1] + i))
                else:
                    lst_pos_to_r.append(
                        (begin_to_r[0] + i, begin_to_r[1] + i))

            if (bool_left and (begin_to_l[0] + i != position[0] and begin_to_l[1] - i != position[1]) and begin_to_l[0] + i <= 7 and begin_to_l[1] - i >= 0):
                if not board.is_empty_square((begin_to_l[0] + i, begin_to_l[1] - i)):
                    # CHECK IF THE CHECKED SQUARE IS BEFORE THE ORIGINAL POSITION OF THE BISHOP
                    if begin_to_l[1] - i > position[1]:
                        lst_pos_to_l = []
                    else:
                        bool_left = False
                    if board.get_color_pawn((begin_to_l[0] + i, begin_to_l[1] - i)) != color or check_move:
                        lst_pos_to_l.append(
                            (begin_to_l[0] + i, begin_to_l[1] - i))
                else:
                    lst_pos_to_l.append(
                        (begin_to_l[0] + i, begin_to_l[1] - i))

        return lst_pos_to_r + lst_pos_to_l


class Queen(Piece):
    
    def __init__(self, position, color) -> None:
        super().__init__(position, color, 'QUEEN', 9)
        if color == 'white':
            self.img = config.WHITE_QUEEN
        else:
            self.img = config.BLACK_QUEEN

    def __str__(self) -> str:
        return f"{self.color} Queen"

    def move_possibility(self, board, position: tuple = (), color: str = None, check_move: bool = False) -> list:
        """
        Created a list of allowed positions for the Piece

        keyword arguments:
        position -- position of the Piece
        board -- instance of the Board class
        color -- color of the piece
        check_move -- option to also check for forbidden moves for the opponent king
        """
        if len(position) == 0:
            position = self.position

        if color == None:
            color = self.color
        lst_position_rook = Rook.move_possibility(
            None, board, self.position, color, check_move)
        lst_position_bishop = Bishop.move_possibility(
            None, board, self.position, color, check_move)
        return lst_position_rook + lst_position_bishop


class King(Piece):

    def __init__(self, position, color) -> None:
        super().__init__(position, color, "KING")
        self.first_move = True
        self.castling_possibility = False
        if color == 'white':
            self.img = config.WHITE_KING
        else:
            self.img = config.BLACK_KING

    def __str__(self) -> str:
        return f"{self.color} King"

    def move_possibility(self,  board, position: tuple = (), color: str = None, check_move: bool = False, recursive_call: bool = False) -> list:
        """
        Created a list of allowed positions for the Piece

        keyword arguments:
        position -- position of the piece
        board -- instance of the Board class
        color -- color of the piece
        check_move -- option to also check for forbidden moves for the opponent king
        recursive_call -- Option to avoid infinite recursion when this method is called from board.all_move_possibility
        """

        if len(position) == 0:
            position = self.position
        if color == None:
            color = self.color
        lst_position = []
        lst_posibility = [(-1, -1), (-1, 0), (-1, 1), (1, 0),
                          (1, 1), (0, 1), (1, -1), (0, -1)]

        # MAKE ALL MOVE POSSIBILITY
        for pos in lst_posibility:
            if (position[0] + pos[0] >= 0 and position[0] + pos[0] <= 7) and (position[1] + pos[1] >= 0 and position[1] + pos[1] <= 7):
                if check_move:
                    lst_position.append(
                        (position[0] + pos[0], position[1] + pos[1]))
                elif board.get_color_pawn((position[0] + pos[0], position[1] + pos[1])) != color:
                    lst_position.append(
                        (position[0] + pos[0], position[1] + pos[1]))

        if recursive_call == False:
            # SORTS IN THE LIST OF POSSIBILITY OF MOVEMENT OF THE KING, WHICH SQUARE ARE NOT ACCESSIBLE BECAUSE WOULD PUT THE RO IN FAILUR
            pos_king = 0 if color == 'black' else 7
            n_lst = []
            for pos in lst_position:
                if not board.is_attacked(pos):
                    n_lst.append(pos)
            lst_position = n_lst

            casteling_left = False
            casteling_right = False
            # MANAGE IF CASTELING IS POSSIBLE
            if self.first_move == True:
                if (board.square[pos_king][0].name == 'ROOK' and board.square[pos_king][0].color == color and
                        board.square[pos_king][0].first_move and board.square[pos_king][0].first_move):
                    for i in range(1, 4):
                        if board.square[pos_king][i].name != 'EMPTY' or board.is_attacked((pos_king, i)):
                            casteling_left = False
                            break
                        else:
                            casteling_left = True
                    if casteling_left:
                        n_lst.append((pos_king, 2))

                if (board.square[pos_king][7].name == 'ROOK' and board.square[pos_king][7].color == color and
                        board.square[pos_king][7].first_move and board.square[pos_king][7].first_move):
                    for i in range(5, 7):
                        if board.square[pos_king][i].name != 'EMPTY' or board.is_attacked((pos_king, i)):
                            casteling_right = False
                            break
                        else:
                            casteling_right = True
                    if casteling_right:
                        n_lst.append((pos_king, 6))
            if casteling_right or casteling_left:
                self.castling_possibility = True
            else:
                self.castling_possibility = False
            return n_lst

        return lst_position

    def move(self, board, new_position: tuple, move_possibility: list) -> None:
        """
        Move a piece on the board

        keyword arguments:
        board -- instance of class Board
        new_position -- new position on the board for the piece
        move_possibility -- list of possible positions for the piece
        """
        super().move(board, new_position, move_possibility)
        if self.first_move:
            self.first_move = False
        if self.castling_possibility:
            pos_king = 0 if self.color == 'black' else 7
            if new_position == (pos_king, 2):
                board.square[pos_king][0].move(
                    board, (pos_king, 3), [(pos_king, 3)])
            elif new_position == (pos_king, 6):
                board.square[pos_king][7].move(
                    board, (pos_king, 5), [(pos_king, 5)])


class Pawn(Piece):

    def __init__(self, position, color) -> None:
        super().__init__(position, color, 'PAWN', 1)
        self.first_move = None
        if color == 'white':
            self.img = config.WHITE_PAWN
        else:
            self.img = config.BLACK_PAWN

    def __str__(self) -> str:
        return f"{self.color} Pawn"

    def move_possibility(self,  board, position: tuple = (), color: str = None, check_move: str = False) -> list:
        """
        Created a list of allowed positions for the Piece

        keyword arguments:
        position -- position of the piece
        board -- instance of the Board class
        color -- color of the piece
        check_move -- option to also check for forbidden moves for the opponent king
        """

        if len(position) == 0:
            position = self.position

        if color == None:
            color = self.color
        if color == 'white':
            base_position = 6
            value = -1
            en_passant = 3
        else:
            base_position = 1
            value = 1
            en_passant = 4

        position_attack = [(position[0] + value, position[1] - 1),
                           (position[0] + value, position[1] + 1)]
        position_en_passant = [(position[0], position[1] - 1),
                               (position[0], position[1] + 1)]

        lst_position = []
        if not check_move:
            if position[0] + value <= 7 and position[0] >= 0 and board.is_empty_square((position[0] + value, position[1])):
                lst_position.append((position[0] + value, position[1]))
                if position[0] == base_position and board.is_empty_square((position[0] + value * 2, position[1])):
                    lst_position.append((position[0] + value * 2, position[1]))

            for pos in position_attack:
                if (pos[0] <= 7 and pos[0] >= 0 and pos[1] <= 7 and pos[1] >= 0 and not board.is_empty_square(pos) and
                        board.get_color_pawn(pos) != color):
                    lst_position.append(pos)

            if position[0] == en_passant:
                for pos in position_en_passant:
                    if (pos[0] <= 7 and pos[0] >= 0 and pos[1] <= 7 and pos[1] >= 0 and not board.is_empty_square(pos) and
                            board.get_color_pawn(pos) != color and board.square[pos[0]][pos[1]].name == "PAWN" and board.square[pos[0]][pos[1]].first_move):

                        lst_position.append((pos[0] + value, pos[1]))

        else:
            for pos in position_attack:
                if pos[0] <= 7 and pos[0] >= 0 and pos[1] <= 7 and pos[1] >= 0:
                    lst_position.append(pos)
        return lst_position

    def move(self, board, new_position: tuple, move_possibility: list) -> None:
        """
        Move a piece on the board

        keyword arguments:
        board -- instance of class Board
        new_position -- new position on the board for the piece
        move_possibility -- list of possible positions for the piece
        """

        # MANAGE EN PASSANT
        if self.position[1] != new_position[1] and board.is_empty_square(new_position):
            value = 1 if self.color == "white" else -1
            board.square[new_position[0] + value][new_position[1]] = Piece()

        super().move(board, new_position, move_possibility)

        level_up_pos = 0 if self.color == "white" else 7

        if self.position[0] == level_up_pos:
            board.square[self.position[0]][self.position[1]] = Queen(self.position, self.color)

        for row in board.square:
            for piece in row:
                if piece.color == board.color_play and piece.name == "PAWN" and piece.first_move:
                    piece.first_move = False
        if self.first_move == None:
            self.first_move = True
        elif self.first_move:
            self.first_move = False
