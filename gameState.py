from termcolor import colored
import pygame as pg
import math
from bots.bot import Bot, BotState

BOT_SPRITE_PATH = "./res/bot.png"


class GameState:

    def __init__(self, b_width, b_height, square_len=10):
        """
        Initialize the object
        :param b_width: The number of squares horizontally
        :param b_height: The number of squares vertically
        :param square_len: How wide each square is in pixels
        """
        pg.init()

        self.bots = dict()
        self.bot_states = dict()

        self.b_width = b_width
        self.b_height = b_height
        self.square_width = square_len
        self.init_pos = (math.floor(b_width/2), math.floor(b_height/2))
        self.board = list()

        self.clock = pg.time.Clock()
        self.curr_time = pg.time.get_ticks()

        self.screen = pg.display.set_mode((b_width * square_len, b_height * square_len))
        self.bot_sprite = pg.transform.scale(pg.image.load(BOT_SPRITE_PATH),
                                             (self.square_width, self.square_width))
        pg.display.set_caption("Armageddon Blitz")

        for row in range(b_width):
            self.board.append(list())
            for col in range(b_height):
                self.board[row].append(0)

    def add_bot(self, bot: Bot, color: pg.Color) -> None:
        """
        Add a bot to the competitors in the game
        :param bot: The bot to add
        :param color: The bot's color to be used when coloring rectangles
        """
        self.bots.update({bot.pid: bot})
        self.bot_states.update({bot.pid: BotState(bot.pid, self.init_pos, color)})

    def run_game_loop(self) -> None:
        """
        This runs the game loop. Will not stop until the game is over
        """
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            time = pg.time.get_ticks()
            if time - self.curr_time > 200:
                self.update()
                self.curr_time = time
                # TODO if all the bots are dead. Display score

            self.draw()
            self.clock.tick(60)

    def update(self) -> None:
        """
        Update the game state and all the bot states
        """
        # Figure out all the bots' moves
        moves = dict()
        for bot in self.bots.values():
            bot_state = self.bot_states.get(bot.pid)
            move = bot.move(self.board, bot_state)
            update_tile = True
            for pid, other_bot in self.bot_states.items():
                if pid == bot.pid:
                    continue
                elif other_bot.pos == bot_state.pos:
                    update_tile = False

            if update_tile:
                self.board[bot_state.pos[0]][bot_state.pos[1]] = bot.pid

            moves.update({bot.pid: move})

        # Actually update the bots now
        for pid, move in moves.items():
            self.bot_states.get(pid).move(move)

        # Determine if any of the bots died
        dead_bots = list()
        for bot in self.bot_states.values():
            pos = bot.pos
            # Kill any bots that ran off the board
            if pos[0] < 0 or pos[0] >= self.b_width\
                    or pos[1] < 0 or pos[1] >= self.b_height:
                dead_bots.append(bot.pid)
                continue

            value = self.board[pos[0]][pos[1]]
            if(value != bot.pid) and (value != 0):
                dead_bots.append(bot.pid)

        for pid in dead_bots:
            if pid in self.bots:
                print(colored(f"Player {pid} has been killed :("))
                self.bots.pop(pid)

    def draw(self) -> None:
        """
        Draws all components to the screen
        """
        bg_colour = (255, 255, 255)
        self.screen.fill(bg_colour)

        for x in range(self.b_width):
            for y in range(self.b_height):
                pid = self.board[x][y]
                if pid in self.bot_states:
                    color = self.bot_states.get(pid).color
                else:
                    color = pg.Color('white')
                rect = (x*self.square_width, y*self.square_width, self.square_width, self.square_width)
                pg.draw.rect(self.screen, color, rect, 0)
                pg.draw.rect(self.screen, pg.Color('black'), rect, 1)

        for bot in self.bot_states.values():
            # Add an outline to each bot's square
            rect = (bot.pos[0]*self.square_width, bot.pos[1]*self.square_width, self.square_width, self.square_width)
            pg.draw.rect(self.screen, bot.color, rect, 2)

            # Draw the transformed bot sprite
            trans_pos = (bot.pos[0] * self.square_width, bot.pos[1] * self.square_width)
            self.screen.blit(self.bot_sprite, trans_pos)

        pg.display.flip()
        pass
