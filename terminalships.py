import random

#### Greeting and rules

print("""
Welcome, Player, to Terminalships! \n 
Here's how the game works! \n
1. The setup. \n
\t The game is played on four grids, two for each player. The grids are square 9x9 and the individual squares in the \n
\t grid are identified by letter and number. On one grid the player arranges ships and records the shots by the \n
\t opponent. On the other grid the player records their own shots. Before play begins, each player secretly arranges \n
\t their ships on their primary grid. \n
\t Each ship occupies a number of consecutive squares on the grid, arranged either horizontally or vertically. The \n
\t number of squares for each ship is determined by the type of the ship. The ships cannot overlap (i.e., only one \n
\t ship can occupy any given square in the grid). The types and numbers of ships allowed are the same for each \n
\t player. The ships mustn't be touching (i.e., there must be at least a 1 square gap). \n
2. The battle. \n
\t After the ships have been positioned, the game proceeds in a series of rounds. In each round, each player takes a \n
\t turn to announce a target square in the opponent's grid which is to be shot at. The opponent announces whether or \n
\t not the square is occupied by a ship. If it is a "hit", the player who is hit marks this on their own or "ocean" \n
\t grid. The attacking player marks the hit or miss on their own "tracking" or "target" grid, in order to build up a \n
\t picture of the opponent's fleet. When all of the squares of a ship have been hit, the ship's owner announces the \n
\t sinking of the Carrier, Submarine, Patrol Boat, or the Battleship. If all of a player's ships have been sunk, the \n
\t game is over and their opponent wins. If all ships of both players are sunk by the end of the round, the game is a \n
\t draw.""")
