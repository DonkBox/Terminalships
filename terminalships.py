import random

#### Greeting and rules

print("""
Welcome, Player, to Terminalships! \n \n
Here's how the game works! \n
1. The setup.
\t The game is played on four grids, two for each player. The grids are square 9x9 and the individual squares in the
\t grid are identified by letter and number. On one grid the player arranges ships and records the shots by the
\t opponent. On the other grid the player records their own shots. Before play begins, each player secretly arranges
\t their ships on their primary grid.
\t Each ship occupies a number of consecutive squares on the grid, arranged either horizontally or vertically. The
\t number of squares for each ship is determined by the type of the ship. The ships cannot overlap (i.e., only one
\t ship can occupy any given square in the grid). The types and numbers of ships allowed are the same for each
\t player. The ships mustn't be touching (i.e., there must be at least a 1 square gap). \n
2. The battle.
\t After the ships have been positioned, the game proceeds in a series of rounds. In each round, each player takes a
\t turn to announce a target square in the opponent's grid which is to be shot at. The opponent announces whether or
\t not the square is occupied by a ship. If it is a "hit", the player who is hit marks this on their own or "ocean"
\t grid. The attacking player marks the hit or miss on their own "tracking" or "target" grid, in order to build up a
\t picture of the opponent's fleet. When all of the squares of a ship have been hit, the ship's owner announces the
\t sinking of the Carrier, Submarine, Patrol Boat, or the Battleship. If all of a player's ships have been sunk, the
\t game is over and their opponent wins. If all ships of both players are sunk by the end of the round, the game is a
\t draw. \n
""")

input("PRESS ENTER TO CONTINUE.")

print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")

#### Start of prep game prep code.

playergrid = {0: {0: {1: """	|""", 2: """	|""", 3: """	|"""}, 1: {1: """	|""", 2: """   A	|""", 3: """	|"""}}}

#### Defines function, that prints playergrid correctly

def printplayergrid():
    for key1 in range(10):
        for key3 in range(1, 4):
            key2string = ""
            for key2 in range(10):
                try:
                    key2string += playergrid[key1][key2][key3]
                except KeyError:
                    pass
            try:
                print(key2string)
            except KeyError:
                pass

        print("--------------------------------------------------------------------------------")

printplayergrid()
