from .bot import *


class Jack(Bot):

    def move(self, board: [[int]], bot_state: BotState) -> Move:
        return Move.FORWARD
