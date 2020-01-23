import pygame
import block
import bot
import jack
import sunny

class GameState:

	def __init__(self, bWidth = 200, bHeight = 100):
		pygame.init()

		self.Bots = list()
		self.Board = list()
		self.clock = pygame.time.Clock()
		self.gameDisplay = pygame.display.set_mode((800,600))
		pygame.display.set_caption("Armageddon Blitz")

		for row in range(bWidth):
			self.Board[row].append( list() )
			for col in range(bHeight):
				self.Board[row][col] = Block()

	def AddBot(self, bot : Bot ):
		self.Bots.append( bot )

	def RunGameLoop( self ):
		while( True ):
			self.Update()
			self.Draw()
			self.clock.tick(60)

	def Update(self):
		for bot in self.Bots:
			bot.Update()

	def Draw(self):
		for y in range(0, len(self.Board)):
			for x in range(0, len(self.Board[y])):

				block = self.Board[y][x]

				for bot in self.Bots: 
					if block.owner == bot.id:
						drawRect(x*10, y*10, (x+1)*10, (y+1)*10, bot.color)

#MAIN
game = GameState()
game.AddBot(Sunny())
game.AddBot(Jack())
game.RunGameLoop()