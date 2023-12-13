
##################"[[MAPEADO / SNAKE / COLISIONES y OBSTACULOS]]"###################
import readchar as readchar #libreria de input automatico sin enter, pero en bytes)
import os
import random

POS_X = 0
POS_Y = 1
NUM_MAP_OBJECTS = 11
MAP_OBJECTS_FOR_LEVEL = 4             # la contrabarra quita el enter.
obstacle_definition = """\
####                        ###     
####                        ###     
       #######     ############   ##
       #######     ############   ##
####   #######     ############   ##
####   #######     ############   ##
####                    #######   ##
                        #######   ##
                        #####       
####################    #####       
####################    #####     ##
####     #     #####    #####      #
####     #     #####    #####      #
####           #####     #####     #
            ######     #########   #
       ##########     ##########    
####   #########     ###############
####   ########     ################
####         ##     ################
##########   ##             ########
##########   ##                   ##
##########   ##             ####  ##
##########           ###########  ##
##########   ##      ###########  ##\
"""
# Create obstacle map: por (fila) hace una lista y estas listas en otra lista
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)
MEDIO_X = (len(obstacle_definition[0]) / 2)
MEDIO_Y = (len(obstacle_definition) / 2)
encabezado = ("#" * (MAP_WIDTH * 3 + 2))
position_player = [1, 2]
map_objects = []
tail_length = 0
tail = []

# LOCALIZACION DE PLAYER (la mia)
"""
for player in position_player[0:1]:
    POS_X = player
    for player in position_player[1:]:
        POS_Y = player
""" ########################

# Loop Game
while True:
    # generate random
    while len(map_objects) < NUM_MAP_OBJECTS:
        random_object = [random.randint(1, (MAP_WIDTH - 1)), random.randint(1, (MAP_HEIGHT - 1))]

        if random_object not in map_objects and random_object != position_player and \
                obstacle_definition[random_object[POS_Y]][random_object[POS_X]] != "#":
            map_objects.append(random_object)

    #Draw Map
    print("\n" + encabezado)
    print(("#" * int(((MAP_WIDTH * 3 + 2) - 11) / 2) + "[[[SNAKE]]]" + "#" *
           int(((MAP_WIDTH * 3 + 2) - 10) / 2)))
    print(encabezado + "\n")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coord_y in range(MAP_HEIGHT):
        print("|", end="")

        for coord_x in range(MAP_WIDTH):

            char_to_draw = "   "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coord_x and map_object[POS_Y] == coord_y:
                    char_to_draw = " * "
                    object_in_cell = map_object


            for tail_piece in tail:
                if tail_piece[POS_X] == coord_x and tail_piece[POS_Y] == coord_y:
                    char_to_draw = "[*]"

            if position_player[POS_X] == coord_x and position_player[POS_Y] == coord_y:
                char_to_draw = "[@]"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

            if obstacle_definition[coord_y][coord_x] == "#":
                char_to_draw = "###"



            print("{}".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))


    #Ask user  where wants to move:
    #(direction = input(where you wants to move? [WSAD]
    direction = readchar.readchar().decode() #.decode pasa a str
    new_position = None

    #Movements
    if direction == "w":
        new_position = [position_player[POS_X], (position_player[POS_Y] - 1) % MAP_WIDTH]


    elif direction == "s":
        new_position = [position_player[POS_X], (position_player[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "d":
        new_position = [(position_player[POS_X] + 1) % MAP_WIDTH, position_player[POS_Y]]

    elif direction == "a":
        new_position = [(position_player[POS_X] - 1) % MAP_WIDTH, position_player[POS_Y]]

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, position_player.copy())
            tail = tail[:tail_length]
            position_player = new_position
            if position_player in tail:
                break

    elif direction == "q":
        exit()
    elif direction == "p":
        os.system('cls')
        print("\n" + encabezado)
        print(("#" * int(((MAP_WIDTH * 3 + 2) - 11) / 2) + "[[[PAUSE]]]" + "#" *
               int(((MAP_WIDTH * 3 + 2) - 10) / 2)))
        print(encabezado + "\n")
        print("+" + "-" * MAP_WIDTH * 3 + "+")
        for coord_y in range(MAP_HEIGHT):
            print("|", end="")
            for coord_x in range(MAP_WIDTH):
                if MEDIO_X == coord_x and MEDIO_Y == coord_y:
                    print("-P-", end="")
                else:
                    print("   ", end="")
            print("|")
        print("+" + "-" * MAP_WIDTH * 3 + "+")
        input("Presiona Enter para continuar...")
    os.system('cls')
os.system('cls')

print("\n" + encabezado)
print(("#" * int(((MAP_WIDTH * 3 + 2) - 11) / 2) + "[[[SNAKE]]]" + "#" *
       int(((MAP_WIDTH * 3 + 2) - 10) / 2)))
print(encabezado + "\n")
print("+" + "-" * MAP_WIDTH * 3 + "+")
for coord_y in range(MAP_HEIGHT):
    print("|", end="")
    for coord_x in range(MAP_WIDTH):
        if MEDIO_X == coord_x and MEDIO_Y == coord_y:
             print("END", end="")
        else:
            print("   ", end="")
    print("|")
print("+" + "-" * MAP_WIDTH * 3 + "+")
input("Enter para salir...")


