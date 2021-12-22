import pygame
from board import Board
from config import BOARD
from graphEngine import GraphEngine


if __name__ == "__main__":
    board = Board()
    graph_engine = GraphEngine() 
    graph_engine.blit_game(board)
    clock=pygame.time.Clock()
    clock.tick(30)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(graph_engine.get_position_board(event.pos))
                    graph_engine.test(graph_engine.get_position_board(event.pos), board)

    pygame.quit()
