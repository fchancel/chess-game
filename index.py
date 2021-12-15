import pygame
from board import Board
from config import BOARD
from graphEngine import GraphEngine

if __name__ == "__main__":
    board = Board()
    graph_engine = GraphEngine() 
    graph_engine.blit_game(board)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
