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


class Bot:
	"""
	The base class to inherit from for each player
	"""

	def __init__(self, pid: int, pos: (int, int)):
		self.pid = pid
		self.pos = pos

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

