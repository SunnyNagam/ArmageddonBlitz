import pygame
from pygame import Color
from gameState import GameState
from bots.jack import Jack
from bots.sunny import Sunny

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    gameWidth = 20
    gameHeight = 15
    blockWidth = 40
    initPos = (gameWidth/blockWidth/2, gameHeight/blockWidth/2)

    pygame.display.set_caption("Armageddon Blitz")

    game = GameState(gameWidth, gameHeight, blockWidth)
    game.add_bot(Jack(69), Color('cyan'))
    game.add_bot(Sunny(420), Color('red'))
    game.run_game_loop()
