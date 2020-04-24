from .bot import *


class Sunny(Bot):
    ting = 0
    def move(self, board: [[int]], bot_state: BotState) -> Move:
        self.ting = self.ting + 1

        if self.ting % 3 == 0:
            return Move.FORWARD
        else:
            return Move.TURN_RIGHT
