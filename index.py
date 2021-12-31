import pygame
from board import Board
from config import BOARD, FPS
from graphEngine import GraphEngine
import copy

if __name__ == "__main__":
    board = Board()
    graph_engine = GraphEngine()
    graph_engine.blit_board()
    graph_engine.blit_pieces(board)
    graph_engine.flip()
    clock = pygame.time.Clock()
    clock.tick(FPS)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    position = graph_engine.get_position_board(event.pos)
                    piece = board.square[position[0]][position[1]]
                    piece_selected = board.piece_selected()

                    if piece_selected and position in lst_move_possibility:
                        piece_selected.move(
                            board, position, lst_move_possibility)
                        board.change_color_play()
                        graph_engine.blit_board()
                        if board.is_check():
                            graph_engine.blit_king_check(board)
                        graph_engine.blit_pieces(board)
                        piece_selected.selected = False

                    elif piece.color == board.color_play:
                        board.all_deselect_piece()
                        piece.selected = True
                        graph_engine.blit_board()
                        graph_engine.blit_pieces(board)
                        graph_engine.blit_select_piece(position)
                        lst_move_possibility = board.move_authorized(piece)
                        if board.is_check():
                            graph_engine.blit_king_check(board)
                        graph_engine.blit_move_possibility(
                            lst_move_possibility, board)
        graph_engine.flip()
    pygame.quit()
