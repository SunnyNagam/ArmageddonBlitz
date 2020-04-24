from .bot import *


class Sunny(Bot):
    ting = 0
    def move(self, board: [[int]], bot_state: BotState) -> Move:
        self.ting = self.ting + 1
        if self.ting % 4 != 0 or self.ting > 47:
            return Move.FORWARD
        else:
            return Move(4 if int(self.ting/16 % 2) == 1 else 3)


