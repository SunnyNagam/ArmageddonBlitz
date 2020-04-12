from termcolor import colored
import pygame as pg
from bot import Bot


class GameState:

    def __init__(self, bWidth=200, bHeight=100):
        pg.init()

        self.Bots = dict()
        self.Board = list()
        self.clock = pg.time.Clock()
        self.gameDisplay = pg.display.set_mode((800, 600))
        pg.display.set_caption("Armageddon Blitz")

        for row in range(bWidth):
            self.Board[row].append(list())
            for col in range(bHeight):
                self.Board[row][col] = 0

    def add_bot(self, bot: Bot, color: pg.Color):
        self.Bots.update({bot.id: (bot, color)})

    def run_game_loop(self):
        while True:
            self.update()
            self.draw()
            self.clock.tick(60)

    def update(self):
        for bot in self.Bots:
            bot.move(self.Board)

        for bot in self.Bots:
            pos = bot.get_pos()
            value = self.Board[pos[0]][pos[1]]
            if(value != bot.id) or (value != 0):
                print(colored(f"Player {id} has been killed :("))

    def draw(self):
        pass


