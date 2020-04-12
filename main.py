import pygame
from pygame import Color
from gameState import GameState

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Armageddon Blitz")

    game = GameState(800, 600)
    game.add_bot(Jack(), Color(255, 0, 0))
    game.add_bot(Sunny())
    game.run_game_loop()
