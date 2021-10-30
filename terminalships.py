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
\n\n\n\n\n\n\n\n\n""")

#### Start of prep game prep code.

#### Defines function, that converts playergrid string to playergrid dict

playergridstr = """	|	|	|	|	|	|	|	|	|	|
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

newplayergrid2 = []


def convertplayergrid():
    newplayergrid2 = playergridstr.split(
        """--------------------------------------------------------------------------------""")

    for a in range(len(newplayergrid2)):
        newplayergrid2[a] = newplayergrid2[a].split('\n')
        newplayergrid2[a].pop()
    newplayergrid2.pop()
    for a in range(len(newplayergrid2) - 1):
        newplayergrid2[a + 1].pop(0)
    for a in range(len(newplayergrid2)):
        for b in range(len(newplayergrid2[a])):
            newplayergrid2[a][b] = newplayergrid2[a][b].split('|')
            newplayergrid2[a][b].pop()

    return newplayergrid2


newplayergrid = convertplayergrid()


# print(newplayergrid)

#### Defines function, that prints playergrid correctly

def printplayergrid():
    print("--------------------------------------------------------------------------------")
    for a in range(len(newplayergrid)):
        for b in range(len(newplayergrid[a])):
            tempstr = ""
            for c in range(len(newplayergrid[a][b])):
                tempstr += newplayergrid[a][b][c] + "|"
            print(tempstr)

        print("--------------------------------------------------------------------------------")


# printplayergrid()

#### Setup stage

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
submarines = 3
patrols = 3
ships = ["carrier", "battleship", "submarine", "patrol"]
areas = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2",
         "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4",
         "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6",
         "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8",
         "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9"]
directions = ["up", "right", "down", "left"]
alphabet_order = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9}
alphabet_order_other = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I"}
all_ship_areas = [[] for i in range(carrier + battleships + submarines + patrols)]
valid_areas = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
               "I2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "A4", "B4", "C4", "D4", "E4", "F4", "G4",
               "H4", "I4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "A6", "B6", "C6", "D6", "E6", "F6",
               "G6", "H6", "I6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "A8", "B8", "C8", "D8", "E8",
               "F8", "G8", "H8", "I8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9"]
valid_areas_lists = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 1], [2, 2], [2, 3],
                     [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6],
                     [3, 7], [3, 8], [3, 9], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9],
                     [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 1], [6, 2], [6, 3],
                     [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6],
                     [7, 7], [7, 8], [7, 9], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9],
                     [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]

print("Let's build your grid!")


def printsetup():
    print("\nYou still have:")
    tempstr = ""
    if carrier == 1:
        tempstr += "\t1 carrier \n"
    elif carrier == 0:
        pass
    else:
        tempstr += "\t" + str(carrier) + " carriers \n"

    if battleships == 1:
        tempstr += "\t1 battleship \n"
    elif battleships == 0:
        pass
    else:
        tempstr += "\t" + str(battleships) + " battleships \n"

    if submarines == 1:
        tempstr += "\t1 submarine \n"
    elif submarines == 0:
        pass
    else:
        tempstr += "\t" + str(submarines) + " submarines \n"

    if patrols == 1:
        tempstr += "\t1 patrol boat \n"
    elif patrols == 0:
        pass
    else:
        tempstr += "\t" + str(patrols) + " patrol boats \n"

    print(tempstr)

    print("Here is your grid: \n")

    printplayergrid()


def takeinputs():
    retry = False
    in1 = input("\nSELECT SHIP (carrier, battleship, submarine or patrol): ")
    in2 = input("SELECT AREA (A1, B7, E3, so on): ")
    in3 = input("SELECT DIRECTION (up, right, down, left): ")
    in1 = in1.lower()
    in2 = in2[0].upper() + str(in2[1])
    in3 = in3.lower()

    print("")
    if not in1 in ships:
        print("ERROR: INVALID INPUT FOR SHIP.")
        retry = True
    if not in2 in areas:
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


def updategrid():
    inputs = takeinputs()
    if not inputs == True:
        in1 = inputs[0]
        in2 = inputs[1]
        in3 = inputs[2]
        spaces = 0
        area = []
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

        area.append(int(in2[1]))
        area.append(alphabet_order.get(in2[0]))

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
                for e in range(0, 3):
                    global newplayergrid
                    newplayergrid[i[0]][e][i[1]] = "[#####]"
                templist = [[i[0], i[1]], [i[0] + 1, i[1]], [i[0] + 1, i[1] + 1], [i[0], i[1] + 1],
                            [i[0] - 1, i[1] + 1], [i[0] - 1, i[1]], [i[0] - 1, i[1] - 1], [i[0], i[1] - 1],
                            [i[0] + 1, i[1] - 1]]
                for i in templist:
                    try:
                        valid_areas_lists.remove(i)
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
    printsetup()
    updategrid()

print("Your grid is ready!\nHere is your finished grid:\n")

printplayergrid()

input("PRESS ENTER TO CONTINUE.")

print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n""")
