import pygame
from pygame import Color
from gameState import GameState
from jack import Jack
from sunny import Sunny

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    gameWidth = 80
    gameHeight = 60
    blockWidth = 10
    initPos = (gameWidth/blockWidth/2, gameHeight/blockWidth/2)

    pygame.display.set_caption("Armageddon Blitz")

    game = GameState(gameWidth, gameHeight)
    game.add_bot(Jack(69, initPos), Color(255, 0, 0))
    game.add_bot(Sunny(420, initPos), Color(0, 255, 0))
    game.run_game_loop()
