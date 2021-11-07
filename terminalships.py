import random

#### Intro.

print("""\n\n\n\nWelcome, Player, to \n""")
print("""
 _____  _____ ______ ___  ___ _____  _   _   ___   _      _____  _   _  _____ ______  _____ 
|_   _||  ___|| ___ \|  \/  ||_   _|| \ | | / _ \ | |    /  ___|| | | ||_   _|| ___ \/  ___|
  | |  | |__  | |_/ /| .  . |  | |  |  \| |/ /_\ \| |    \ `--. | |_| |  | |  | |_/ /\ `--. 
  | |  |  __| |    / | |\/| |  | |  | . ` ||  _  || |     `--. \|  _  |  | |  |  __/  `--. \\
  | |  | |___ | |\ \ | |  | | _| |_ | |\  || | | || |____/\__/ /| | | | _| |_ | |    /\__/ /
  \_/  \____/ \_| \_|\_|  |_/ \___/ \_| \_/\_| |_/\_____/\____/ \_| |_/ \___/ \_|    \____/ 
                                                                                            
                                                                                            
""")
print("""
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
\n\n\n\n\n\n\n\n\n""")

#### Grid and grid converter. I don't really need to keep them but I needed it for the first time to get the empty grid
#### list. I could use if I want to make a smaller or bigger grid.

grid_str = """	|	|	|	|	|	|	|	|	|	|
	|   A	|   B	|   C	|   D	|   E	|   F	|   G	|   H	|   I	|
	|	|	|	|	|	|	|	|	|	|
--------------------------------------------------------------------------------
	|	|	|	|	|	|	|	|	|	|
   1	|	|	|	|	|	|	|	|	|	|
	|	|	|	|	|	|	|	|	|	|
--------------------------------------------------------------------------------
	|	|	|	|	|	|	|	|	|	|
   2	|	|	|	|	|	|	|	|	|	|
	|	|	|	|	|	|	|	|	|	|
--------------------------------------------------------------------------------
	|	|	|	|	|	|	|	|	|	|
   3	|	|	|	|	|	|	|	|	|	|
	|	|	|	|	|	|	|	|	|	|
--------------------------------------------------------------------------------
	|	|	|	|	|	|	|	|	|	|
   4	|	|	|	|	|	|	|	|	|	|
	|	|	|	|	|	|	|	|	|	|
--------------------------------------------------------------------------------
	|	|	|	|	|	|	|	|	|	|
   5	|	|	|	|	|	|	|	|	|	|
	|	|	|	|	|	|	|	|	|	|
--------------------------------------------------------------------------------
	|	|	|	|	|	|	|	|	|	|
   6	|	|	|	|	|	|	|	|	|	|
	|	|	|	|	|	|	|	|	|	|
--------------------------------------------------------------------------------
	|	|	|	|	|	|	|	|	|	|
   7	|	|	|	|	|	|	|	|	|	|
	|	|	|	|	|	|	|	|	|	|
--------------------------------------------------------------------------------
	|	|	|	|	|	|	|	|	|	|
   8	|	|	|	|	|	|	|	|	|	|
	|	|	|	|	|	|	|	|	|	|
--------------------------------------------------------------------------------
	|	|	|	|	|	|	|	|	|	|
   9	|	|	|	|	|	|	|	|	|	|
	|	|	|	|	|	|	|	|	|	|
--------------------------------------------------------------------------------"""


def convert_grid():
    grid = grid_str.split(
        """--------------------------------------------------------------------------------""")

    for a in range(len(grid)):
        grid[a] = grid[a].split('\n')
        grid[a].pop()
    grid.pop()
    for a in range(len(grid) - 1):
        grid[a + 1].pop(0)
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            grid[a][b] = grid[a][b].split('|')
            grid[a][b].pop()

    return grid


grid_list_player = convert_grid()
grid_list_bot = convert_grid()
grid_shot_player = convert_grid()
grid_shot_bot = convert_grid()

####  Function, that prints the grid list into an actual grid correctly.

def print_grid(grid):
    print("--------------------------------------------------------------------------------")
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            tempstr = ""
            for c in range(len(grid[a][b])):
                tempstr += grid[a][b][c] + "|"
            print(tempstr)

        print("--------------------------------------------------------------------------------")

#### Setup phase.

print("""It's time to set up your battleship grid! \n \n""")

print("""Instructions

To set up your battleship grid, you select which ship you want to place down, the area on which you want the
tail of the ship be on and in which direction you want the ship to go. \nHere's an example:\n
    SELECT SHIP: carrier
    SELECT AREA: B3
    SELECT DIRECTION: right

    Output:

--------------------------------------------------------------------------------
        |       |       |       |       |       |       |       |       |       |
        |   A   |   B   |   C   |   D   |   E   |   F   |   G   |   H   |   I   |
        |       |       |       |       |       |       |       |       |       |
--------------------------------------------------------------------------------
        |       |       |       |       |       |       |       |       |       |
   1    |       |       |       |       |       |       |       |       |       |
        |       |       |       |       |       |       |       |       |       |
--------------------------------------------------------------------------------
        |       |       |       |       |       |       |       |       |       |
   2    |       |       |       |       |       |       |       |       |       |
        |       |       |       |       |       |       |       |       |       |
--------------------------------------------------------------------------------
        |       |[#####]|[#####]|[#####]|[#####]|       |       |       |       |
   3    |       |[#####]|[#####]|[#####]|[#####]|       |       |       |       |
        |       |[#####]|[#####]|[#####]|[#####]|       |       |       |       |
--------------------------------------------------------------------------------
        |       |       |       |       |       |       |       |       |       |
   4    |       |       |       |       |       |       |       |       |       |
        |       |       |       |       |       |       |       |       |       |
--------------------------------------------------------------------------------
        |       |       |       |       |       |       |       |       |       |
   5    |       |       |       |       |       |       |       |       |       |
        |       |       |       |       |       |       |       |       |       |
--------------------------------------------------------------------------------
        |       |       |       |       |       |       |       |       |       |
   6    |       |       |       |       |       |       |       |       |       |
        |       |       |       |       |       |       |       |       |       |
--------------------------------------------------------------------------------
        |       |       |       |       |       |       |       |       |       |
   7    |       |       |       |       |       |       |       |       |       |
        |       |       |       |       |       |       |       |       |       |
--------------------------------------------------------------------------------
        |       |       |       |       |       |       |       |       |       |
   8    |       |       |       |       |       |       |       |       |       |
        |       |       |       |       |       |       |       |       |       |
--------------------------------------------------------------------------------
        |       |       |       |       |       |       |       |       |       |
   9    |       |       |       |       |       |       |       |       |       |
        |       |       |       |       |       |       |       |       |       |
--------------------------------------------------------------------------------\n""")

input("PRESS ENTER TO CONTINUE.")

print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n""")

carrier = 1
battleships = 2
submarines = 2
patrols = 3
ships = ["carrier", "battleship", "submarine", "patrol"]
areas = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2",
         "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4",
         "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6",
         "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8",
         "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9"]
directions = ["up", "right", "down", "left"]
alphabet_order = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9}
valid_areas_lists = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 1], [2, 2], [2, 3],
                     [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6],
                     [3, 7], [3, 8], [3, 9], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9],
                     [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 1], [6, 2], [6, 3],
                     [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6],
                     [7, 7], [7, 8], [7, 9], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9],
                     [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]
player_ship_areas = []
bot_ship_areas = []
bot_ships_left = ["carrier", "battleship", "battleship", "submarine", "submarine", "patrol", "patrol",
                  "patrol"]
player_unshot_areas = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 1], [2, 2], [2, 3],
                       [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6],
                       [3, 7], [3, 8], [3, 9], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9],
                       [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 1], [6, 2], [6, 3],
                       [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6],
                       [7, 7], [7, 8], [7, 9], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9],
                       [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]

bot_unshot_areas = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 1], [2, 2], [2, 3],
                    [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6],
                    [3, 7], [3, 8], [3, 9], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9],
                    [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 1], [6, 2], [6, 3],
                    [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6],
                    [7, 7], [7, 8], [7, 9], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9],
                    [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]

print("Let's build your grid!")

#### Function for looks, but why not? We're not trying to save memory, so might as well make it look better.

def print_setup():
    print("\nYou still have:")
    temp_str = ""
    if carrier == 1:
        temp_str += "\t1 carrier (length 5 areas)\n"
    elif carrier == 0:
        pass
    else:
        temp_str += "\t" + str(carrier) + " carriers (length 5 areas)\n"

    if battleships == 1:
        temp_str += "\t1 battleship (length 4 areas)\n"
    elif battleships == 0:
        pass
    else:
        temp_str += "\t" + str(battleships) + " battleships (length 4 areas)\n"

    if submarines == 1:
        temp_str += "\t1 submarine (length 3 areas)\n"
    elif submarines == 0:
        pass
    else:
        temp_str += "\t" + str(submarines) + " submarines (length 3 areas)\n"

    if patrols == 1:
        temp_str += "\t1 patrol boat (length 2 areas)\n"
    elif patrols == 0:
        pass
    else:
        temp_str += "\t" + str(patrols) + " patrol boats (length 2 areas)\n"

    print(temp_str)

    print("Here is your grid: \n")

    print_grid(grid_list_player)

#### Function, that takes inputs in the setup phase.

def take_inputs():
    retry = False
    in1 = input("\nSELECT SHIP (carrier, battleship, submarine or patrol): ")
    in2 = input("SELECT AREA (A1, B7, E3, so on): ")
    in3 = input("SELECT DIRECTION (up, right, down, left): ")
    in1 = in1.lower()
    try:
        in2 = [int(in2[1]), alphabet_order.get(in2[0].upper())]
    except:
        print("INVALID INPUT FOR AREA:")
        input("PRESS ENTER TO CONTINUE:")
        print("\n")
        update_grid()
    in3 = in3.lower()

    print("")
    if not in1 in ships:
        print("ERROR: INVALID INPUT FOR SHIP.")
        retry = True
    if not in2 in valid_areas_lists:
        print("ERROR: INVALID INPUT FOR AREA.")
        retry = True
    if not in3 in directions:
        print("ERROR: INVALID INPUT FOR DIRECTION.")
        retry = True

    if retry == True:
        input("\nPRESS ENTER TO CONTINUE.")
        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
                \n\n\n\n\n\n\n\n\n""")
        return retry

    else:
        print("""\n\n\n\n""")
        return [in1, in2, in3]

#### Function that takes the inputs and uses them to update the player's ship grid.

def update_grid():
    global carrier
    global battleships
    global submarines
    global patrols
    inputs = take_inputs()
    if not inputs == True:
        in1 = inputs[0]
        in2 = inputs[1]
        in3 = inputs[2]
        spaces = 0
        area = in2
        if in1 == "carrier" and carrier > 0:
            carrier -= 1
            spaces = 5
        elif in1 == "battleship" and battleships > 0:
            battleships -= 1
            spaces = 4
        elif in1 == "submarine" and submarines > 0:
            submarines -= 1
            spaces = 3
        elif in1 == "patrol" and patrols > 0:
            patrols -= 1
            spaces = 2
        else:
            print("ERROR: INVALID INPUT FOR SHIP.")
            input("\nPRESS ENTER TO CONTINUE.")
            take_inputs()

        ship_areas_grid = [[] for i in range(0, spaces)]

        if in3 == "up":
            for i in range(0, spaces):
                ship_areas_grid[i].append(area[0] - i)
                ship_areas_grid[i].append(area[1])
        elif in3 == "right":
            for i in range(0, spaces):
                ship_areas_grid[i].append(area[0])
                ship_areas_grid[i].append(area[1] + i)
        elif in3 == "down":
            for i in range(0, spaces):
                ship_areas_grid[i].append(area[0] + i)
                ship_areas_grid[i].append(area[1])
        elif in3 == "left":
            for i in range(0, spaces):
                ship_areas_grid[i].append(area[0])
                ship_areas_grid[i].append(area[1] - i)

        valid = True
        for i in ship_areas_grid:
            if 0 < i[0] < 10 and 0 < i[1] < 10 and i in valid_areas_lists:
                pass
            else:
                valid = False
                break

        if valid:
            for i in ship_areas_grid:
                player_ship_areas.append(i)
                for e in range(0, 3):
                    global grid_list_player
                    grid_list_player[i[0]][e][i[1]] = "[#####]"
                temp_list = [[i[0], i[1]], [i[0] + 1, i[1]], [i[0] + 1, i[1] + 1], [i[0], i[1] + 1],
                             [i[0] - 1, i[1] + 1], [i[0] - 1, i[1]], [i[0] - 1, i[1] - 1], [i[0], i[1] - 1],
                             [i[0] + 1, i[1] - 1]]
                for e in temp_list:
                    try:
                        valid_areas_lists.remove(e)
                    except:
                        pass
        else:
            if in1 == "carrier":
                carrier += 1
            elif in1 == "battleship":
                battleships += 1
            elif in1 == "submarine":
                submarines += 1
            elif in1 == "patrol":
                patrols += 1
    else:
        pass


while carrier + battleships + submarines + patrols > 0:
    print_setup()
    update_grid()

print("Your grid is ready!\nHere is your finished grid:\n")

print_grid(grid_list_player)

input("PRESS ENTER TO CONTINUE.")

print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n""")

#### This makes the AI's grid. I was sloppy and messy around this part.

valid_areas_lists1 = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 1], [2, 2], [2, 3],
                     [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6],
                     [3, 7], [3, 8], [3, 9], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9],
                     [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 1], [6, 2], [6, 3],
                     [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6],
                     [7, 7], [7, 8], [7, 9], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9],
                     [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]

the_range = 0
the_range2 = 0

while the_range < len(bot_ships_left):
    the_range2 += 1

    if the_range2 > 23:
        grid_list_bot = convert_grid()
        valid_areas_lists1 = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 1], [2, 2],
                             [2, 3],
                             [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
                             [3, 6],
                             [3, 7], [3, 8], [3, 9], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8],
                             [4, 9],
                             [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 1], [6, 2],
                             [6, 3],
                             [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5],
                             [7, 6],
                             [7, 7], [7, 8], [7, 9], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8],
                             [8, 9],
                             [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]

    spaces = 0
    area = []
    if bot_ships_left[the_range] == "carrier":
        spaces = 5
    elif bot_ships_left[the_range] == "battleship":
        spaces = 4
    elif bot_ships_left[the_range] == "submarine":
        spaces = 3
    elif bot_ships_left[the_range] == "patrol":
        spaces = 2

    counter3 = 0
    while area == [] and counter3 < 80:
        counter3 += 1
        for e in range(2):
            area.append(random.randint(1, 9))
        if 0 < area[0] < 10 and 0 < area[1] < 10 and area in valid_areas_lists1:
            pass
        else:
            area = []

    if counter3 == 80:
        continue

    ship_areas_grid = []
    direction = ""
    counter = 0
    counter2 = 0
    while_directions = ["up", "right", "down", "left"]

    while_key = True
    while counter < 4:
        direction = ""
        dir_int = random.randint(1, 4)

        if dir_int == 1 and "up" in while_directions:
            direction = "up"
            while_directions.remove("up")
        if dir_int == 2 and "right" in while_directions:
            direction = "right"
            while_directions.remove("right")
        if dir_int == 3 and "down" in while_directions:
            direction = "down"
            while_directions.remove("down")
        if dir_int == 4 and "left" in while_directions:
            direction = "left"
            while_directions.remove("left")

        if direction == "":
            continue

        ship_areas_grid = [[] for i in range(0, spaces)]

        if direction == "up":
            for a in range(0, spaces):
                ship_areas_grid[a].append(area[0] - a)
                ship_areas_grid[a].append(area[1])
        elif direction == "right":
            for a in range(0, spaces):
                ship_areas_grid[a].append(area[0])
                ship_areas_grid[a].append(area[1] + a)
        elif direction == "down":
            for a in range(0, spaces):
                ship_areas_grid[a].append(area[0] + a)
                ship_areas_grid[a].append(area[1])
        elif direction == "left":
            for a in range(0, spaces):
                ship_areas_grid[a].append(area[0])
                ship_areas_grid[a].append(area[1] - a)

        valid = True
        for b in ship_areas_grid:
            if 0 < b[0] < 10 and 0 < b[1] < 10 and b in valid_areas_lists1:
                pass
            else:
                valid = False
                break

        if valid:
            counter = 4
        else:
            counter2 += 1
            counter += 1

    if counter2 == 4:
        continue

    for c in ship_areas_grid:
        bot_ship_areas.append(c)
        for e in range(0, 3):
            grid_list_bot[c[0]][e][c[1]] = "[#####]"
        temp_list = [[c[0], c[1]], [c[0] + 1, c[1]], [c[0] + 1, c[1] + 1], [c[0], c[1] + 1],
                     [c[0] - 1, c[1] + 1], [c[0] - 1, c[1]], [c[0] - 1, c[1] - 1], [c[0], c[1] - 1],
                     [c[0] + 1, c[1] - 1]]
        for e in temp_list:
            try:
                valid_areas_lists1.remove(e)
            except:
                pass
    the_range += 1

#### Function, that's used to help identify if a ship has been sunken.

sinks = 0


def temp_ship_info(area2, all_ship_areas):
    counter4 = 1
    ship_areas = []
    ship_areas.append(area2)
    for i in range(5):
        if [area2[0] + counter4, area2[1]] in all_ship_areas:
            ship_areas.append([area2[0] + counter4, area2[1]])
            counter4 += 1
        else:
            break

    counter4 = 1
    for i in range(5):
        if [area2[0], area2[1] + counter4] in all_ship_areas:
            ship_areas.append([area2[0], area2[1] + counter4])
            counter4 += 1
        else:
            break

    counter4 = 1
    for i in range(5):
        if [area2[0] - counter4, area2[1]] in all_ship_areas:
            ship_areas.append([area2[0] - counter4, area2[1]])
            counter4 += 1
        else:
            break

    counter4 = 1
    for i in range(5):
        if [area2[0], area2[1] - counter4] in all_ship_areas:
            ship_areas.append([area2[0], area2[1] - counter4])
            counter4 += 1
        else:
            break

    return ship_areas

#### Function, that takes and uses the player's input to shoot.

removals1 = []
ship1 = []

def player_shot():
    global removals1
    global ship1
    input1 = input("ENTER AREA TO SHOOT:")
    area1 = []
    try:
        area1 = [int(input1[1]), alphabet_order.get(input1[0].upper())]
    except:
        pass

    if area1 in player_unshot_areas:

        player_unshot_areas.remove(area1)
        if area1 in removals1:
            if len(removals1) == 1:
                grid_shot_player[area1[0]][0][area1[1]] = "XXXXXXX"
                grid_shot_player[area1[0]][1][area1[1]] = "XXXXXXX"
                grid_shot_player[area1[0]][2][area1[1]] = "XXXXXXX"
                bot_ship_areas.remove(area1)
                removals1.remove(area1)
                print("\nHIT!")
                print("SUNK!")
                global sinks
                sinks += 1
                for i in ship1:
                    temp_list1 = [[i[0], i[1]], [i[0] + 1, i[1]], [i[0] + 1, i[1] + 1],
                                  [i[0], i[1] + 1],
                                  [i[0] - 1, i[1] + 1], [i[0] - 1, i[1]], [i[0] - 1, i[1] - 1],
                                  [i[0], i[1] - 1],
                                  [i[0] + 1, i[1] - 1]]
                    for h in temp_list1:
                        try:
                            player_unshot_areas.remove(h)
                            grid_shot_player[h[0]][0][h[1]] = "======="
                            grid_shot_player[h[0]][1][h[1]] = "======="
                            grid_shot_player[h[0]][2][h[1]] = "======="
                        except:
                            pass
                for i in ship1:
                    grid_shot_player[i[0]][0][i[1]] = "XXXXXXX"
                    grid_shot_player[i[0]][1][i[1]] = "XXXXXXX"
                    grid_shot_player[i[0]][2][i[1]] = "XXXXXXX"

            else:
                grid_shot_player[area1[0]][0][area1[1]] = "XXXXXXX"
                grid_shot_player[area1[0]][1][area1[1]] = "XXXXXXX"
                grid_shot_player[area1[0]][2][area1[1]] = "XXXXXXX"
                bot_ship_areas.remove(area1)
                removals1.remove(area1)
                print("\nHIT!")

        elif area1 in bot_ship_areas:
            grid_shot_player[area1[0]][0][area1[1]] = "XXXXXXX"
            grid_shot_player[area1[0]][1][area1[1]] = "XXXXXXX"
            grid_shot_player[area1[0]][2][area1[1]] = "XXXXXXX"
            print("\nHIT!")

            removals1 = temp_ship_info(area1, bot_ship_areas)
            removals1.remove(area1)
            ship1 = temp_ship_info(area1, bot_ship_areas)

            bot_ship_areas.remove(area1)

            if len(removals1) == 0:
                grid_shot_player[area1[0]][0][area1[1]] = "XXXXXXX"
                grid_shot_player[area1[0]][1][area1[1]] = "XXXXXXX"
                grid_shot_player[area1[0]][2][area1[1]] = "XXXXXXX"
                print("SUNK!")
                sinks += 1
                for i in ship1:
                    temp_list1 = [[i[0], i[1]], [i[0] + 1, i[1]], [i[0] + 1, i[1] + 1],
                                  [i[0], i[1] + 1],
                                  [i[0] - 1, i[1] + 1], [i[0] - 1, i[1]], [i[0] - 1, i[1] - 1],
                                  [i[0], i[1] - 1],
                                  [i[0] + 1, i[1] - 1]]
                    for h in temp_list1:
                        try:
                            bot_unshot_areas.remove(h)
                            grid_shot_player[h[0]][0][h[1]] = "======="
                            grid_shot_player[h[0]][1][h[1]] = "======="
                            grid_shot_player[h[0]][2][h[1]] = "======="
                        except:
                            pass
                for i in ship:
                    grid_shot_player[i[0]][0][i[1]] = "XXXXXXX"
                    grid_shot_player[i[0]][1][i[1]] = "XXXXXXX"
                    grid_shot_player[i[0]][2][i[1]] = "XXXXXXX"


        else:
            print("\nMISS!")
            grid_shot_player[area1[0]][0][area1[1]] = "======="
            grid_shot_player[area1[0]][1][area1[1]] = "======="
            grid_shot_player[area1[0]][2][area1[1]] = "======="


    else:
        print("INVALID INPUT:")
        input("PRESS ENTER TO CONTINUE:")
        print("\n")
        player_shot()

#### Function, that makes the AI shoot with strategy

var = []
counter1 = 0
ship_key = False
best = 0
area = []
removals = []
ship = []
shot_key = True
last_hit = []
counter4 = 0

def bot_sink():
    global var
    global best
    global ship_key
    global removals
    global last_hit
    global ship
    last_hit = []
    ship_key = False
    var = []
    best = 0
    grid_list_player[removals[0][0]][0][removals[0][1]] = "XXXXXXX"
    grid_list_player[removals[0][0]][1][removals[0][1]] = "XXXXXXX"
    grid_list_player[removals[0][0]][2][removals[0][1]] = "XXXXXXX"
    grid_shot_bot[removals[0][0]][0][removals[0][1]] = "XXXXXXX"
    grid_shot_bot[removals[0][0]][1][removals[0][1]] = "XXXXXXX"
    grid_shot_bot[removals[0][0]][2][removals[0][1]] = "XXXXXXX"
    try:
        player_ship_areas.remove(removals[0])
    except:
        pass
    removals.pop(0)
    print("THE ENEMY HAS HIT YOUR SHIP!")
    print("THE ENEMY HAS SUNK YOUR SHIP!")
    for i in ship:
        temp_list1 = [[i[0], i[1]], [i[0] + 1, i[1]], [i[0] + 1, i[1] + 1],
                      [i[0], i[1] + 1],
                      [i[0] - 1, i[1] + 1], [i[0] - 1, i[1]], [i[0] - 1, i[1] - 1],
                      [i[0], i[1] - 1],
                      [i[0] + 1, i[1] - 1]]
        for h in temp_list1:
            try:
                bot_unshot_areas.remove(h)
                grid_shot_bot[h[0]][0][h[1]] = "======="
                grid_shot_bot[h[0]][1][h[1]] = "======="
                grid_shot_bot[h[0]][2][h[1]] = "======="
            except:
                pass
    for i in ship:
        grid_list_player[i[0]][0][i[1]] = "XXXXXXX"
        grid_list_player[i[0]][1][i[1]] = "XXXXXXX"
        grid_list_player[i[0]][2][i[1]] = "XXXXXXX"
        grid_shot_bot[i[0]][0][i[1]] = "XXXXXXX"
        grid_shot_bot[i[0]][1][i[1]] = "XXXXXXX"
        grid_shot_bot[i[0]][2][i[1]] = "XXXXXXX"


def bot_shot():
    global var
    global best
    global area
    global ship_key
    global counter4
    global removals
    global ship
    global shot_key
    global last_hit
    global player_ship_areas
    i1 = 0
    i2 = 0
    if shot_key:
        shot_key = False
        if ship_key:
            if len(removals) == 1:
                bot_sink()
            else:
                try:
                    grid_list_player[removals[0][0]][0][removals[0][1]] = "XXXXXXX"
                    grid_list_player[removals[0][0]][1][removals[0][1]] = "XXXXXXX"
                    grid_list_player[removals[0][0]][2][removals[0][1]] = "XXXXXXX"
                    grid_shot_bot[removals[0][0]][0][removals[0][1]] = "XXXXXXX"
                    grid_shot_bot[removals[0][0]][1][removals[0][1]] = "XXXXXXX"
                    grid_shot_bot[removals[0][0]][2][removals[0][1]] = "XXXXXXX"
                except:
                    pass
                print("THE ENEMY HAS HIT YOUR SHIP!")
                try:
                    player_ship_areas.remove(removals[0])
                except:
                    pass
                try:
                    removals.pop(0)
                except:
                    pass
                try:
                    bot_unshot_areas.remove(removals[0])
                except:
                    pass

        elif not last_hit == []:
            if counter4 == 0:
                if [last_hit[0] + 1, last_hit[1]] in bot_unshot_areas:
                    area = [last_hit[0] + 1, last_hit[1]]
                    bot_unshot_areas.remove(area)
                    if area in ship:
                        if len(removals) == 1:
                            bot_sink()
                        else:
                            grid_list_player[area[0]][0][area[1]] = "XXXXXXX"
                            grid_list_player[area[0]][1][area[1]] = "XXXXXXX"
                            grid_list_player[area[0]][2][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][0][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][1][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][2][area[1]] = "XXXXXXX"
                            print("THE ENEMY HAS HIT YOUR SHIP!")
                            player_ship_areas.remove(area)
                            ship_key = True
                            counter4 = 0
                            last_hit = []
                            removals.pop(0)

                    else:
                        print("THE ENEMY MISSED!")
                        grid_shot_bot[area[0]][0][area[1]] = "======="
                        grid_shot_bot[area[0]][1][area[1]] = "======="
                        grid_shot_bot[area[0]][2][area[1]] = "======="

                else:
                    shot_key = True
                    counter4 += 1
                    bot_shot()

            elif counter4 == 1:
                if [last_hit[0], last_hit[1] + 1] in bot_unshot_areas:
                    area = [last_hit[0], last_hit[1] + 1]
                    bot_unshot_areas.remove(area)
                    if area in ship:
                        if len(removals) == 1:
                            bot_sink()
                        else:
                            grid_list_player[area[0]][0][area[1]] = "XXXXXXX"
                            grid_list_player[area[0]][1][area[1]] = "XXXXXXX"
                            grid_list_player[area[0]][2][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][0][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][1][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][2][area[1]] = "XXXXXXX"
                            print("THE ENEMY HAS HIT YOUR SHIP!")
                            player_ship_areas.remove(area)
                            ship_key = True
                            counter4 = 0
                            last_hit = []
                            removals.pop(0)

                    else:
                        print("THE ENEMY MISSED!")
                        grid_shot_bot[area[0]][0][area[1]] = "======="
                        grid_shot_bot[area[0]][1][area[1]] = "======="
                        grid_shot_bot[area[0]][2][area[1]] = "======="

                else:
                    shot_key = True
                    counter4 += 1
                    bot_shot()

            elif counter4 == 2:
                if [last_hit[0] - 1, last_hit[1]] in bot_unshot_areas:
                    area = [last_hit[0] - 1, last_hit[1]]
                    bot_unshot_areas.remove(area)
                    if area in ship:
                        if len(removals) == 1:
                            bot_sink()
                        else:
                            grid_list_player[area[0]][0][area[1]] = "XXXXXXX"
                            grid_list_player[area[0]][1][area[1]] = "XXXXXXX"
                            grid_list_player[area[0]][2][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][0][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][1][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][2][area[1]] = "XXXXXXX"
                            print("THE ENEMY HAS HIT YOUR SHIP!")
                            player_ship_areas.remove(area)
                            ship_key = True
                            counter4 = 0
                            last_hit = []
                            removals.pop(0)

                    else:
                        print("THE ENEMY MISSED!")
                        grid_shot_bot[area[0]][0][area[1]] = "======="
                        grid_shot_bot[area[0]][1][area[1]] = "======="
                        grid_shot_bot[area[0]][2][area[1]] = "======="

                else:
                    shot_key = True
                    counter4 += 1
                    bot_shot()

            elif counter4 == 3:
                if [last_hit[0], last_hit[1] - 1] in bot_unshot_areas:
                    area = [last_hit[0], last_hit[1] - 1]
                    bot_unshot_areas.remove(area)
                    if area in ship:
                        if len(removals) == 1:
                            bot_sink()
                        else:
                            grid_list_player[area[0]][0][area[1]] = "XXXXXXX"
                            grid_list_player[area[0]][1][area[1]] = "XXXXXXX"
                            grid_list_player[area[0]][2][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][0][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][1][area[1]] = "XXXXXXX"
                            grid_shot_bot[area[0]][2][area[1]] = "XXXXXXX"
                            print("THE ENEMY HAS HIT YOUR SHIP!")
                            player_ship_areas.remove(area)
                            ship_key = True
                            counter4 = 0
                            last_hit = []
                            removals.pop(0)

                    else:
                        print("THE ENEMY MISSED!")
                        grid_shot_bot[area[0]][0][area[1]] = "======="
                        grid_shot_bot[area[0]][1][area[1]] = "======="
                        grid_shot_bot[area[0]][2][area[1]] = "======="

                else:
                    shot_key = True
                    counter4 += 1
                    bot_shot()

            else:
                ship_key = True
                shot_key = True
                counter4 = 0
                bot_shot()

        elif not var == [] and best == 0:
            try:
                bot_unshot_areas.remove(var)

            except:
                grid_shot_bot[var[0]][0][var[1]] = "======="
                grid_shot_bot[var[0]][1][var[1]] = "======="
                grid_shot_bot[var[0]][2][var[1]] = "======="

                var = []
                shot_key = True
                bot_shot()
        else:
            for i in range(500):
                i1 = random.randint(1, 9)
                i2 = random.randint(1, 9)
                if [i1, i2] in bot_unshot_areas:
                    global counter1
                    counter1 = 0
                    if [i1 + 1, i2] in bot_unshot_areas:
                        counter1 += 1
                    if [i1, i2 + 1] in bot_unshot_areas:
                        counter1 += 1
                    if [i1 - 1, i2] in bot_unshot_areas:
                        counter1 += 1
                    if [i1, i2 - 1] in bot_unshot_areas:
                        counter1 += 1

                    if var == [] or counter1 < best:
                        var = [i1, i2]
                        best = counter1

            if [var[0] + 1, var[1]] in bot_unshot_areas:
                area = [var[0] + 1, var[1]]
            elif [var[0], var[1] + 1] in bot_unshot_areas:
                area = [var[0], var[1] + 1]
            elif [var[0] - 1, var[1]] in bot_unshot_areas:
                area = [var[0] - 1, var[1]]
            elif [var[0], var[1] - 1] in bot_unshot_areas:
                area = [var[0], var[1] - 1]
            else:
                area = var

            bot_unshot_areas.remove(area)
            if area in player_ship_areas:
                grid_list_player[area[0]][0][area[1]] = "XXXXXXX"
                grid_list_player[area[0]][1][area[1]] = "XXXXXXX"
                grid_list_player[area[0]][2][area[1]] = "XXXXXXX"
                grid_shot_bot[area[0]][0][area[1]] = "XXXXXXX"
                grid_shot_bot[area[0]][1][area[1]] = "XXXXXXX"
                grid_shot_bot[area[0]][2][area[1]] = "XXXXXXX"
                print("THE ENEMY HAS HIT YOUR SHIP!")

                removals = temp_ship_info(area, player_ship_areas)
                removals.pop(0)
                ship = temp_ship_info(area, player_ship_areas)

                last_hit = area

                player_ship_areas.remove(area)
            else:
                print("THE ENEMY MISSED!")
                grid_shot_bot[area[0]][0][area[1]] = "======="
                grid_shot_bot[area[0]][1][area[1]] = "======="
                grid_shot_bot[area[0]][2][area[1]] = "======="

#### Main part of the game.

rounds = 1
while not player_ship_areas == [] and not bot_ship_areas == []:
    print("Round " + str(rounds))
    print("Players turn!\n")
    print("Your ship grid:")
    print_grid(grid_list_player)
    print("\n")
    print("Your shot grid:")
    print_grid(grid_shot_player)
    print("Stats:\n\tEnemy ships sunk - " + str(sinks))
    print("\n")
    player_shot()
    input("PRESS ENTER TO CONTINUE:")

    bot_shot()
    shot_key = True
    input("PRESS ENTER TO CONTINUE:")

    print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n""")
    rounds += 1

if player_ship_areas == [] and not bot_ship_areas == []:
    print("""
__   __ _____  _   _        _      _____  _____  _____  _ 
\ \ / /|  _  || | | |      | |    |  _  |/  ___||  ___|| |
 \ V / | | | || | | |      | |    | | | |\ `--. | |__  | |
  \ /  | | | || | | |      | |    | | | | `--. \|  __| | |
  | |  \ \_/ /| |_| |      | |____\ \_/ //\__/ /| |___ |_|
  \_/   \___/  \___/       \_____/ \___/ \____/ \____/ (_)
                                                          
                                                          
""")
    input("PRESS ENTER TO ACCEPT DEFEAT:")

elif not player_ship_areas == [] and bot_ship_areas == []:
    print("""
__   __ _____  _   _        _    _  _____  _   _  _ 
\ \ / /|  _  || | | |      | |  | ||_   _|| \ | || |
 \ V / | | | || | | |      | |  | |  | |  |  \| || |
  \ /  | | | || | | |      | |/\| |  | |  | . ` || |
  | |  \ \_/ /| |_| |      \  /\  / _| |_ | |\  ||_|
  \_/   \___/  \___/        \/  \/  \___/ \_| \_/(_)
                                                    
                                                    
""")
    input("PRESS ENTER TO CONTINUE WITH PRIDE:")

else:
    print("""
 _____  _____  _  _____          ___        ______ ______   ___   _    _  _ 
|_   _||_   _|( )/  ___|        / _ \       |  _  \| ___ \ / _ \ | |  | || |
  | |    | |  |/ \ `--.        / /_\ \      | | | || |_/ // /_\ \| |  | || |
  | |    | |      `--. \       |  _  |      | | | ||    / |  _  || |/\| || |
 _| |_   | |     /\__/ /       | | | |      | |/ / | |\ \ | | | |\  /\  /|_|
 \___/   \_/     \____/        \_| |_/      |___/  \_| \_|\_| |_/ \/  \/ (_)
                                                                            
                                                                            
""")
    input("PRESS ENTER TO CONTINUE WITH DISAPPOINTMENT:")
