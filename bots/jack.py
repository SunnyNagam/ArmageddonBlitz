from .bot import *


class Jack(Bot):

    def move(self, board: [[int]], bot_state: BotState) -> Move:
        pos = bot_state.pos
        scale = bot_state.get_update_scale()

        forward = (pos[0] + (1 * scale[0]), pos[1] + (1 * scale[1]))
        jump = (pos[0] + (2 * scale[0]), pos[1] + (2 * scale[1]))

        if (forward[0] < 0) or (forward[0] >= len(board)) or\
                (forward[1] < 0) or (forward[1] >= len(board[0])):
            return Move.TURN_LEFT
        elif board[forward[0]][forward[1]] == 0:
            return Move.FORWARD
        elif (jump[0] < 0) or (jump[0] >= len(board)) or\
                (jump[1] < 0) or (jump[1] >= len(board[0])):
            return Move.TURN_LEFT
        elif board[jump[0]][jump[1]] == 0:
            return Move.JUMP
        else:
            return Move.TURN_LEFT
