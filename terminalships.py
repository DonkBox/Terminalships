import random

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
\n\n\n\n\n\n\n\n\n""")

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


def print_grid(grid):
    print("--------------------------------------------------------------------------------")
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            tempstr = ""
            for c in range(len(grid[a][b])):
                tempstr += grid[a][b][c] + "|"
            print(tempstr)

        print("--------------------------------------------------------------------------------")


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


def print_setup():
    print("\nYou still have:")
    temp_str = ""
    if carrier == 1:
        temp_str += "\t1 carrier \n"
    elif carrier == 0:
        pass
    else:
        temp_str += "\t" + str(carrier) + " carriers \n"

    if battleships == 1:
        temp_str += "\t1 battleship \n"
    elif battleships == 0:
        pass
    else:
        temp_str += "\t" + str(battleships) + " battleships \n"

    if submarines == 1:
        temp_str += "\t1 submarine \n"
    elif submarines == 0:
        pass
    else:
        temp_str += "\t" + str(submarines) + " submarines \n"

    if patrols == 1:
        temp_str += "\t1 patrol boat \n"
    elif patrols == 0:
        pass
    else:
        temp_str += "\t" + str(patrols) + " patrol boats \n"

    print(temp_str)

    print("Here is your grid: \n")

    print_grid(grid_list_player)


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
        print(in2)
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
        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
                \n\n\n\n\n\n\n\n\n""")
        return [in1, in2, in3]


def update_grid():
    inputs = take_inputs()
    if not inputs == True:
        in1 = inputs[0]
        in2 = inputs[1]
        in3 = inputs[2]
        spaces = 0
        area = in2
        if in1 == "carrier":
            global carrier
            carrier -= 1
            spaces = 5
        elif in1 == "battleship":
            global battleships
            battleships -= 1
            spaces = 4
        elif in1 == "submarine":
            global submarines
            submarines -= 1
            spaces = 3
        elif in1 == "patrol":
            global patrols
            patrols -= 1
            spaces = 2

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

####

valid_areas_lists = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 1], [2, 2], [2, 3],
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
        if 0 < area[0] < 10 and 0 < area[1] < 10 and area in valid_areas_lists:
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
            if 0 < b[0] < 10 and 0 < b[1] < 10 and b in valid_areas_lists:
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
                valid_areas_lists.remove(e)
            except:
                pass
    the_range += 1

####

sinks = 0


def player_shot():
    input1 = input("ENTER AREA TO SHOOT:")
    area1 = []
    try:
        area1 = [int(input1[1]), alphabet_order.get(input1[0].upper())]
    except:
        print("INVALID INPUT:")
        input("PRESS ENTER TO CONTINUE:")
        print("\n")
        player_shot()

    if area1 in player_unshot_areas:
        player_unshot_areas.remove(area1)
        if area1 in bot_ship_areas:
            grid_shot_player[area1[0]][0][area1[1]] = "XXXXXXX"
            grid_shot_player[area1[0]][1][area1[1]] = "XXXXXXX"
            grid_shot_player[area1[0]][2][area1[1]] = "XXXXXXX"
            print("\nHIT!")

            sunk_check = 4
            for d in bot_ship_areas:
                if d == [area1[0] + 1, area1[1]]:
                    sunk_check -= 1
                    continue

            for d in bot_ship_areas:
                if d == [area1[0], area1[1] + 1]:
                    sunk_check -= 1
                    continue

            for d in bot_ship_areas:
                if d == [area1[0] - 1, area1[1]]:
                    sunk_check -= 1
                    continue

            for d in bot_ship_areas:
                if d == [area1[0], area1[1] - 1]:
                    sunk_check += 1
                    continue

            if sunk_check == 4:
                print("SUNK!")
                global sinks
                sinks += 1

            bot_ship_areas.remove(area1)

        else:
            grid_shot_player[area1[0]][0][area1[1]] = "======="
            grid_shot_player[area1[0]][1][area1[1]] = "======="
            grid_shot_player[area1[0]][2][area1[1]] = "======="
            print("\nMISS!")

    else:
        print("INVALID INPUT:")
        input("PRESS ENTER TO CONTINUE:")
        print("\n")
        player_shot()


var = []
counter1 = 0
best = 0
area = []


def bot_shot():
    global var
    global best
    global area
    i1 = 0
    i2 = 0
    if not var == [] and best == 0:
        try:
            bot_unshot_areas.remove(var)
        except:
            grid_shot_bot[var[0]][0][var[1]] = "======="
            grid_shot_bot[var[0]][1][var[1]] = "======="
            grid_shot_bot[var[0]][2][var[1]] = "======="

            var = []
            bot_shot()
            pass

        if var in player_ship_areas:
            grid_list_player[var[0]][0][var[1]] = "XXXXXXX"
            grid_list_player[var[0]][1][var[1]] = "XXXXXXX"
            grid_list_player[var[0]][2][var[1]] = "XXXXXXX"
            grid_shot_bot[var[0]][0][var[1]] = "XXXXXXX"
            grid_shot_bot[var[0]][1][var[1]] = "XXXXXXX"
            grid_shot_bot[var[0]][2][var[1]] = "XXXXXXX"
            print("THE ENEMY HAS HIT YOUR SHIP!")

            sunk_check = 4
            for d in player_ship_areas:
                if d == [var[0] + 1, var[1]]:
                    sunk_check -= 1
                    continue

            for d in player_ship_areas:
                if d == [var[0], var[1] + 1]:
                    sunk_check -= 1
                    continue

            for d in player_ship_areas:
                if d == [var[0] - 1, var[1]]:
                    sunk_check -= 1
                    continue

            for d in player_ship_areas:
                if d == [var[0], var[1] - 1]:
                    sunk_check += 1
                    continue

            if sunk_check == 4:
                print("THE ENEMY HAS SUNK YOUR SHIP!")
                temp_list1 = [[var[0], var[1]], [var[0] + 1, var[1]], [var[0] + 1, var[1] + 1],
                              [var[0], var[1] + 1],
                              [var[0] - 1, var[1] + 1], [var[0] - 1, var[1]], [var[0] - 1, var[1] - 1],
                              [var[0], var[1] - 1],
                              [var[0] + 1, var[1] - 1]]
                for h in temp_list1:
                    try:
                        bot_unshot_areas.remove(h)
                        grid_shot_bot[h[0]][0][h[1]] = "======="
                        grid_shot_bot[h[0]][1][h[1]] = "======="
                        grid_shot_bot[h[0]][2][h[1]] = "======="
                    except:
                        pass

            player_ship_areas.remove(var)
        else:
            grid_shot_bot[var[0]][0][var[1]] = "======="
            grid_shot_bot[var[0]][1][var[1]] = "======="
            grid_shot_bot[var[0]][2][var[1]] = "======="

        var = []
        bot_shot()
        pass
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

            sunk_check = 4
            for d in player_ship_areas:
                if d == [area[0] + 1, area[1]]:
                    sunk_check -= 1
                    continue

            for d in player_ship_areas:
                if d == [area[0], area[1] + 1]:
                    sunk_check -= 1
                    continue

            for d in player_ship_areas:
                if d == [area[0] - 1, area[1]]:
                    sunk_check -= 1
                    continue

            for d in player_ship_areas:
                if d == [area[0], area[1] - 1]:
                    sunk_check += 1
                    continue

            if sunk_check == 4:
                print("THE ENEMY HAS SUNK YOUR SHIP!")
                temp_list1 = [[area[0], area[1]], [area[0] + 1, area[1]], [area[0] + 1, area[1] + 1],
                              [area[0], area[1] + 1],
                              [area[0] - 1, area[1] + 1], [area[0] - 1, area[1]], [area[0] - 1, area[1] - 1],
                              [area[0], area[1] - 1],
                              [area[0] + 1, area[1] - 1]]
                for h in temp_list1:
                    try:
                        bot_unshot_areas.remove(h)
                        grid_shot_bot[h[0]][0][h[1]] = "======="
                        grid_shot_bot[h[0]][1][h[1]] = "======="
                        grid_shot_bot[h[0]][2][h[1]] = "======="
                    except:
                        pass

            player_ship_areas.remove(area)
        else:
            print("THE ENEMY MISSED!")
            grid_shot_bot[area[0]][0][area[1]] = "======="
            grid_shot_bot[area[0]][1][area[1]] = "======="
            grid_shot_bot[area[0]][2][area[1]] = "======="


rounds = 1
while not player_ship_areas == [] or not bot_ship_areas == []:
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
    input("PRESS ENTER TO CONTINUE:")

    print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n""")
    rounds += 1

if player_ship_areas == [] and not bot_ship_areas == []:
    print("YOU LOSE!")

elif not player_ship_areas == [] and bot_ship_areas == []:
    print("YOU WIN!")

else:
    print("IT'S A DRAW!")

input("PRESS ENTER TO CONTINUE:")