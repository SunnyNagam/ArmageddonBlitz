# Armageddon Blitz
## The Rules
Your bot must be derived from the bot class and override the move function.
The function is when your bot decides what it's next move will be. There are
four moves.

1. Move Forward

    Move forward one block in the direction that your bot is facing

2. Jump Forward

    Move 2 blocks forward by skipping one block in the direction that your bot is facing

3. Turn Right

    Rotate your bot clockwise
    
4. Turn Left

    Rotate your bot counterclockwise
    
5. Idle
    
    Do nothing
    
## How to win

Every time you enter or leave a block and it's not owned by anyone else, you take ownership
of the block. If you enter a block and it's owned by someone else, you die. If 2 people enter
the same block on the same turn, then neither bot takes ownership of the block.

The goal of the game is to take ownership of the most blocks and survive the longest.
