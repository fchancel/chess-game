import pygame
from board import Board
from config import BOARD, FPS
from graphEngine import GraphEngine


if __name__ == "__main__":
    board = Board()
    graph_engine = GraphEngine() 
    graph_engine.blit_board(board)
    graph_engine.blit_pieces(board)
    graph_engine.flip()
    clock=pygame.time.Clock()
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
                        piece_selected.move(board, old_position, position, lst_move_possibility)
                        graph_engine.blit_board(board)
                        graph_engine.blit_pieces(board)
                        piece_selected.selected = False
                        board.color_play = "black" if board.color_play == "white" else "white"

                    elif piece.color == board.color_play:
                        board.all_deselect_piece()
                        piece.selected = True
                        graph_engine.blit_board(board)
                        graph_engine.blit_pieces(board)
                        graph_engine.blit_select_piece(position)
                        lst_move_possibility = piece.move_possibility(position, board)
                        graph_engine.blit_move_possibility(lst_move_possibility, board)
                        old_position = position

        graph_engine.flip()
    pygame.quit()
