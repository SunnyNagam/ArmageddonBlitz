from termcolor import colored
from enum import Enum
from pygame import Color


class Move(Enum):
    IDLE = 0
    FORWARD = 1
    JUMP = 2
    TURN_LEFT = 3
    TURN_RIGHT = 4


class Dir(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class BotState:
    """
    Class that the game keeps track of for the players position
    """

    def __init__(self, pid: int, pos: (int, int), color: Color):
        self.pid = pid
        self.pos = pos
        self.dir = Dir.UP
        self.color = color

    def move(self, action: Move) -> None:
        """
        Updates the bot's position and direction based on the action given
        :param action: Action to perform
        """
        if action == Move.IDLE:
            return

        update = self.get_update_scale()

        if action == Move.FORWARD:
            self.pos = (self.pos[0] + (1 * update[0]), self.pos[1] + (1 * update[1]))
        elif action == Move.JUMP:
            self.pos = (self.pos[0] + (2 * update[0]), self.pos[1] + (2 * update[1]))
        elif action == Move.TURN_RIGHT:
            if self.dir == Dir.LEFT:
                self.dir = Dir.UP
            else:
                self.dir = Dir(self.dir.value + 1)
        elif action == Move.TURN_LEFT:
            if self.dir == Dir.UP:
                self.dir = Dir.LEFT
            else:
                self.dir = Dir(self.dir.value - 1)

    def get_update_scale(self) -> (int, int):
        """
        Gets the scaling factor to determine which direction to move
        """
        if self.dir == Dir.UP:
            update = (0, -1)
        elif self.dir == Dir.LEFT:
            update = (1, 0)
        elif self.dir == Dir.DOWN:
            update = (0, 1)
        elif self.dir == Dir.RIGHT:
            update = (-1, 0)
        return update


class Bot:
    """
    The base class to inherit from for each player
    """

    def __init__(self, pid: int):
        self.pid = pid

    def move(self, board: [[int]], bot_state: BotState) -> Move:
        """
        Function to be implemented by bot to make a decision of where to move
        :param bot_state: Current state of the bot
            DO NOT MODIFY
            If you do, you're a f***ing coward and a cheat
        :param board: 2d array representing the game board
        value 0 means that the block has not been claimed
        any other value represents the id of the player who owns it
        :return: The move that the bot wants to take
        """
        print(colored(f"Not implemented for bot {self.pid}", "red"))
        return Move.IDLE
