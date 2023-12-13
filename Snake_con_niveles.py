
##################"[[SNAKE]]"###################
import readchar as readchar #libreria de input automatico sin enter, pero en bytes)
import os
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20 #ancho mapa
MAP_HEIGHT = 15 #alto mapa
NUM_MAP_OBJECTS = 11
MAP_OBJECTS_FOR_LEVEL = 4
MEDIO_X = 9
MEDIO_Y = 7
encabezado = ("#" * (MAP_WIDTH * 3 + 2))
position_player = [3, 1]
map_objects = []
tail_length = 0
tail = []
# generate random
while len(map_objects) < NUM_MAP_OBJECTS:
    random_object = [random.randint(1, (MAP_WIDTH - 1)), random.randint(1, (MAP_HEIGHT - 1))]

    if random_object not in map_objects and random_object != position_player:
        map_objects.append(random_object)

#LOCALIZACION DE PLAYER (la mia)
"""
for player in position_player[0:1]:
    POS_X = player
    for player in position_player[1:]:
        POS_Y = player
""" ########################

# Loop Game
while True:

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

            print("{}".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))

    # levels up:
    if len(map_objects) == 0:
        NUM_MAP_OBJECTS += MAP_OBJECTS_FOR_LEVEL
        tail_length = 0
        while len(map_objects) < NUM_MAP_OBJECTS:
            random_object = [random.randint(1, (MAP_WIDTH - 1)), random.randint(1, (MAP_HEIGHT - 1))]

            if random_object not in map_objects and random_object != position_player:
                map_objects.append(random_object)
    #Ask user  where wants to move:
    #(direction = input(where you wants to move? [WSAD]
    direction = readchar.readchar().decode() #.decode pasa a str
    print(direction)
    #Movements
    if direction == "w":
        tail.insert(0, position_player.copy())
        position_player[POS_Y] -= 1
        position_player[POS_Y] %= MAP_HEIGHT    #hace que no salga del mapeado con la funcion modulo (%)
        tail = tail[:tail_length]
        if position_player in tail:
            break                                        #(esta era mi solucion):
    elif direction == "s":                           #if position_player[POS_Y] <= -1:
        tail.insert(0, position_player.copy())           #position_player[POS_Y] = 14
        position_player[POS_Y] += 1
        position_player[POS_Y] %= MAP_HEIGHT
        tail = tail[:tail_length] #calcula el largo de la cola
        if position_player in tail:
            break
    elif direction == "d":
        tail.insert(0, position_player.copy())
        position_player[POS_X] += 1
        position_player[POS_X] %= MAP_WIDTH
        tail = tail[:tail_length]
        if position_player in tail:
            break
    elif direction == "a":
        tail.insert(0, position_player.copy())
        position_player[POS_X] -= 1
        position_player[POS_X] %= MAP_WIDTH
        tail = tail[:tail_length]
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


