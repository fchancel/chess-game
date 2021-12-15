import pygame
import config


class GraphEngine():
    position_board = (0, 0)
    size_board = (600, 600)
    size_square = (size_board[0] // 8)

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(config.PROGRAM_NAME)
        self.screen = pygame.display.set_mode((800, 800))
        self.board_rect = pygame.Rect(self.position_board, self.size_board)
        board_img = pygame.image.load(config.BOARD)
        self.board_img = pygame.transform.scale(board_img, self.size_board)


        board_rect = []
        for i in range(0, 8):
            board_rect.append([])
            for j in range(0,8):
                board_rect[i].append(pygame.Rect(j * self.size_square, i * self.size_square, self.size_square, self.size_square))
        self.board_rect = board_rect

    def blit_game(self, board):
        self.screen.blit(self.board_img, self.position_board)
        # pygame.draw.rect(self.screen, pygame.Color(15, 15, 15), self.board_rect[1][1])
        for i, line in enumerate(board.square):
            for j, piece in enumerate(line):
                print(piece)
                if piece.img:
                    piece_img = pygame.image.load(piece.img)
                    piece_img = pygame.transform.scale(piece_img, piece.size)
                    self.screen.blit(piece_img, (73 * j, 73 * i))
        pygame.display.flip()
