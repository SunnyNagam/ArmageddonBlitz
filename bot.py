from termcolor import colored


class Bot:
	"""
	The base class to inherit from for each player
	"""

	def __init__(self, id: int, pos: (int, int)):
		self.id = id
		self.pos = pos

	def move(self, board: [[int]]):
		"""
		Function to be implemented by bot to make a decision of where to move
		:param board: 2d array representing the game board
		value 0 means that the block has not been claimed
		any other value represents the id of the player who owns it
		:return:
		"""
		print(colored(f"Not implemented for bot {id}", "red"))
		pass

	def get_pos(self) -> (int, int):
		"""
		Returns the current position of the player
		"""
		return self.pos
