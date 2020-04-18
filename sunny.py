from bot import *


class Sunny(Bot):
    def move(self, board: [[int]], bot_state: BotState) -> Move:
        return Move.IDLE
