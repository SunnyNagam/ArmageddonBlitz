from termcolor import colored
import pygame as pg
from bot import Bot


class GameState:

    def __init__(self, b_width, b_height, square_len=10):
        pg.init()

        self.bots = dict()
        self.bot_states = dict()

        self.b_width = b_width
        self.b_height = b_height
        self.board = list()

        self.clock = pg.time.Clock()
        self.gameDisplay = pg.display.set_mode((b_width * square_len, b_height * square_len))
        pg.display.set_caption("Armageddon Blitz")

        for row in range(b_width):
            self.board[row].append(list())
            for col in range(b_height):
                self.board[row][col] = 0

    def add_bot(self, bot: Bot, color: pg.Color):
        self.bots.update({bot.pid: (bot, color)})

    def run_game_loop(self):
        while True:
            self.update()
            self.draw()
            self.clock.tick(60)

    def update(self):
        for bot in self.bots:
            move = bot.move(self.board)
            self.bot_states[bot.pid].move(move)

        for bot in self.bot_states:
            pos = bot.pos
            # Kill any bots that ran off the board
            if pos[0] < 0 or pos[0] > self.b_width\
                    or pos[1] < 0 or pos[1] > self.b_height:
                self.bots.pop(bot.pid)

            value = self.board[pos[0]][pos[1]]
            if(value != bot.id) or (value != 0):
                print(colored(f"Player {id} has been killed :("))
                self.bots.pop(bot.pid)


    def draw(self):
        pass


