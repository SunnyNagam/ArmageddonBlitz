class GameState:

	def __init__(self, bWidth = 200, bHeight = 100):
		Bots = list()
		Board = new Block[bWidth][bHeight]

	def AddBot( bot : Bot ):
		Bots.push_back( bot )

	def RunGameLoop( self ):
		while( true ):
			self.Update()
			self.Draw()

	def Update(self):
		for( bot in Bots ):
			bot.Update()

	def Draw(self):
		for y in range(0, len(Board)):
			for x in range(0, len(Board[y])):

				block = Board[y][x]

				for bot in Bots: 
					if block.owner == bot.id:
						drawRect(x*10, y*10, (x+1)*10, (y+1)*10, bot.color)

#MAIN
game = new GameState()
game.AddBot(Sunny())
game.AddBot(Jack())
game.RunGameLoop()