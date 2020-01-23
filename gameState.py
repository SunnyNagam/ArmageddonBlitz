class GameState:

	def __init__(self):
		Bots = list()

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
		for( bot in Bots ):
			bot.Draw()


#MAIN
game = new GameState()
game.AddBot(Sunny())
game.AddBot(Jack())
game.RunGameLoop()