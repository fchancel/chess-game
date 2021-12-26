import pygame
import config
from board import Board


class GraphEngine():
    position_board = (0, 0)
    size_board = (800, 800)
    size_square = (size_board[0] // 8)
    size_piece = (size_board[0] // 8, size_board[1] // 8)

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(config.PROGRAM_NAME)

        self.screen = pygame.display.set_mode((800, 800))
        self.board_img = self._make_board_img()
        self.lst_board_rect = self._make_list_rect_board()

    def _make_list_rect_board(self) -> list:
        board_rect = []
        for i in range(0, 8):
            board_rect.append([])
            for j in range(0, 8):
                board_rect[i].append(pygame.Rect(
                    j * self.size_square, i * self.size_square, self.size_square, self.size_square))
        return board_rect

    def _make_board_img(self):
        board_img = pygame.image.load(config.BOARD)
        return pygame.transform.scale(board_img, self.size_board)

    def flip(self):
        pygame.display.flip()

    def blit_pieces(self, board):
        for i, line in enumerate(board.square):
            for j, piece in enumerate(line):
                if piece.img:
                    piece_img = pygame.image.load(piece.img)
                    piece_img = pygame.transform.scale(
                        piece_img, self.size_piece)
                    piece_img_rect = piece_img.get_rect(
                        center=self.lst_board_rect[i][j].center)
                    self.screen.blit(piece_img, piece_img_rect)

    def blit_board(self, board):
        self.screen.blit(self.board_img, self.position_board)

    def get_position_board(self, mouse_position) -> tuple:
        pos_y = mouse_position[0] // self.size_square
        pos_x = mouse_position[1] // self.size_square
        return (pos_x, pos_y)

    def blit_select_piece(self, position):
        pygame.draw.rect(self.screen, pygame.Color(15, 15, 15),
                         self.lst_board_rect[position[0]][position[1]])

    def blit_move_possibility(self, move_possibility, board):
        for pos in move_possibility:
            pygame.draw.rect(self.screen, pygame.Color(config.COLOR_MOVE_POSSIBILITY),
                             self.lst_board_rect[pos[0]][pos[1]])
        self.blit_pieces(board)
