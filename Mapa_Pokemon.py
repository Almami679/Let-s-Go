

import readchar as readchar
import os
import random
import time

POS_X = 0
POS_Y = 1
TRAINERS_FOR_MAP = 5
VIDA_INICIAL_PIKACHU = 85
VIDA_INICIAL_PSYDUCK = 30 #80
VIDA_INICIAL_RATTATAT = 30 #65
VIDA_INICIAL_PIDGEY = 30 #75
TAMAÑO_BARRA_VIDA = 32
map_definition = """\
       ####        ######
       ####        ######
####   #######     ######
####   #######     ######
                        #
                        #
                        #
###################     #
###################     #
          #########     #
          ########     ##
          #######     ###
####   #########     ####
####   ########     #####
####   #######     ######\
"""
ascii_battle = ("|            _                                                              |\n"                               
                    "|           | \                                                             |\n"                              
                    "|      ____/__/...._                                                        |\n"                       
                    "|      | .`        _-;                                                      |\n"                       
                    "|      |/;-._     -_,'                                                      |\n"                      
                    "|      /  \  ``` (                                                          |\n"                      
                    "|      |   |  ^   ^ \                                                       |\n"                       
                    "|      /`'`   o  _ o \                                                      |\n"                     
                    "|      \_,      ' '  |                                                      |\n"                      
                    "|        ;.   /.__.' /                                                      |\n"                       
                    "|       .`._`·._____.·-.                                                    |\n"                    
                    "|      /`.| `-..____.-;\                               `;-.          ____   |\n"
                    "|     /   |  |      | \ \                                `.`\_...._/`.-´`   |\n"
                    "|     |   |  ·------· | |                                  \        /       |\n"   
                    "|                                                          / .--.--,\       |\n"   
                    "|                                                         | /__:  /  |      |\n"  
                    "|                                                          \   / /  /       |\n"   
                    "|                                                          (   / /  )       |")
map_definition = [list(row) for row in map_definition.split("\n")]

MAP_WIDTH = len(map_definition[0])
MAP_HEIGHT = len(map_definition)

# Centrado del mapa para pantalla de END y de PAUSE:

MEDIO_X = int(len(map_definition[0]) / 2)
MEDIO_Y = int(len(map_definition) / 2)

encabezado = ("#" * (MAP_WIDTH * 3 + 2))
position_player = [0, 5]
pokemon_trainers = []

# generate enemies:

while len(pokemon_trainers) < TRAINERS_FOR_MAP:
    random_trainer = [random.randint(1, (MAP_WIDTH - 1)), random.randint(1, (MAP_HEIGHT - 1))]
    if random_trainer not in pokemon_trainers and random_trainer != position_player and \
            map_definition[random_trainer[POS_Y]][random_trainer[POS_X]] != "#":
        pokemon_trainers.append(random_trainer)

# Draw map:
while True:
    if len(pokemon_trainers) == 0:
        break
    # encabezado:
    print("\n" + encabezado)
    print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[PUEBLO RASTRILLO]" + " " *
           int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
    print(encabezado + "\n")

    # Map:
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coord_y in range(MAP_HEIGHT):
        print("|", end="")

        for coord_x in range(MAP_WIDTH):

            char_to_draw = "   "
            object_in_cell = None

            for trainer in pokemon_trainers:
                if trainer[POS_X] == coord_x and trainer[POS_Y] == coord_y:
                    char_to_draw = "·&·"
                    object_in_cell = trainer

            if position_player[POS_X] == coord_x and position_player[POS_Y] == coord_y:
                char_to_draw = ".@."

                if object_in_cell:
                    pokemon_trainers.remove(object_in_cell)


            if map_definition[coord_y][coord_x] == "#":
                char_to_draw = "###"

            print("{}".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Ask user  where wants to move:
    # (direction = input(where you wants to move? [W-S-A-D]
    direction = readchar.readchar().decode()  # .decode pasa a str

    new_position = None

    # Movements
    if direction == "w":
        new_position = [position_player[POS_X], (position_player[POS_Y] - 1) % MAP_HEIGHT]


    elif direction == "s":
        new_position = [position_player[POS_X], (position_player[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "d":
        new_position = [(position_player[POS_X] + 1) % MAP_WIDTH, position_player[POS_Y]]

    elif direction == "a":
        new_position = [(position_player[POS_X] - 1) % MAP_WIDTH, position_player[POS_Y]]

    if new_position:
        if map_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            position_player = new_position

    if new_position in pokemon_trainers:
        os.system('cls')
        vida_actual_pikachu = VIDA_INICIAL_PIKACHU
        porcentage_pikachu = int(vida_actual_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
        barra_pikachu = "#" * porcentage_pikachu
        # encabezado:
        print("\n" + encabezado)
        print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[BATALLAS POKEMON]" + " " *
               int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
        print(encabezado + "\n")

        # Map:
        print("+" + "-" * MAP_WIDTH * 3 + "+")

        print(ascii_battle)
        print("+" + "-" * MAP_WIDTH * 3 + "+")
        print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
        print("+" + "-" * MAP_WIDTH * 3 + "+")

        print("Entrenador pokemon: eeeh, no tan rapido! a ver si puedes ganarme!")
        input("Pulsa Enter para continuar...")
        os.system('cls')
        combate = random.randint(1, 3)

        # Round 1:
        if combate == 1:
            vida_actual_trainer = VIDA_INICIAL_PSYDUCK
            porcentage_trainer = int(vida_actual_trainer * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PSYDUCK)
            barra_trainer = "#" * porcentage_trainer

            while vida_actual_trainer > 0 and vida_actual_pikachu > 0:

                print("\n" + encabezado)
                print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[    -PSYDUCK-     ]" + " " *
                       int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                print(encabezado + "\n")

                # ART:
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                      "(", vida_actual_trainer, "/", VIDA_INICIAL_PSYDUCK, ")" +
                      (((MEDIO_X * 3) - 8) * " "))
                print(ascii_battle)
                print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "), "(",
                      vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("Es el turno de PSYDUCK    ")
                time.sleep(0.5)
                ataque_trainer = random.randint(1, 3)
                if ataque_trainer == 1:
                    print("PSYDUCK ataca con SALPICADURA!")
                    vida_actual_pikachu -= 10
                elif ataque_trainer == 2:
                    print("PSYDUCK ataca con ALETEO!")
                    vida_actual_pikachu -= 8
                else:
                    print("PSYDUCK ataca con CAIDA BOMBA!")
                    vida_actual_pikachu -= 11
                input("Enter para continuar...\n")

                porcentage_pikachu = int(vida_actual_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
                barra_pikachu = ("#" * porcentage_pikachu) + (
                        "." * (TAMAÑO_BARRA_VIDA - porcentage_pikachu))

                if vida_actual_pikachu < 0:
                    vida_actual_pikachu = 0
                    break

                os.system('cls')
                print("\n" + encabezado)
                print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[    -PSYDUCK-     ]" + " " *
                       int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                print(encabezado + "\n")

                # ART:
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                      "(", vida_actual_trainer, "/", VIDA_INICIAL_PSYDUCK, ")" +
                      (((MEDIO_X * 3) - 8) * " "))
                print(ascii_battle)
                print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "), "(",
                      vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))

                time.sleep(0.5)
                os.system('cls')

                ####################################################################
                ataques_pikachu = ["P", "O", "R", "S", "p", "o", "r", "s"]
                ataque_pikachu = None
                while ataque_pikachu not in ataques_pikachu:
                    print("\n" + encabezado)
                    print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[    -PSYDUCK-     ]" + " " *
                           int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                    print(encabezado + "\n")

                    # ART:
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                          "(", vida_actual_trainer, "/", VIDA_INICIAL_PSYDUCK, ")" +
                          (((MEDIO_X * 3) - 8) * " "))
                    print(ascii_battle)
                    print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "),
                          "(",
                          vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print("Es tu turno!    PIKACHU    ")
                    ataque_pikachu = input("Que ataque deseas realizar?\n"
                                           " - [P]lacaje\n"
                                           " - [O]nda Trueno\n"
                                           " - [R]ayo\n"
                                           " - Pa[S]ar Turno\n")

                    if ataque_pikachu == "P" or ataque_pikachu == "p":
                        print("PIKACHU ataca con PLACAJE!")
                        vida_actual_trainer -= 10
                    elif ataque_pikachu == "O" or ataque_pikachu == "o":
                        print("PIKACHU ataca con ONDA TRUENO!")
                        vida_actual_trainer -= 12
                    elif ataque_pikachu == "R" or ataque_pikachu == "r":
                        print("PIKACHU ataca con RAYO!")
                        vida_actual_trainer -= 14
                    elif ataque_pikachu == "S" or ataque_pikachu == "s":
                        print("JUGADOR, ha pasado el turno")


                    porcentage_trainer = int(vida_actual_trainer * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PSYDUCK)
                    barra_trainer = ("#" * porcentage_trainer) + (
                            "." * (TAMAÑO_BARRA_VIDA - porcentage_trainer))
                    if vida_actual_trainer < 0:
                        vida_actual_trainer = 0

                    time.sleep(1)
                    os.system('cls')

                    print("\n" + encabezado)
                    print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[    -PSYDUCK-     ]" + " " *
                           int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                    print(encabezado + "\n")

                    # ART:
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                          "(", vida_actual_trainer, "/", VIDA_INICIAL_PSYDUCK, ")" +
                          (((MEDIO_X * 3) - 8) * " "))
                    print(ascii_battle)
                    print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "),
                          "(",
                          vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                    print("+" + "-" * MAP_WIDTH * 3 + "+")

                    input("Enter para continuar...\n\n")
                    time.sleep(0.5)
                    os.system('cls')
        # Round 2

        elif combate == 2:
            vida_actual_trainer = VIDA_INICIAL_RATTATAT
            porcentage_trainer = int(vida_actual_trainer * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_RATTATAT)
            barra_trainer = "#" * porcentage_trainer

            while vida_actual_trainer > 0 and vida_actual_pikachu > 0:

                print("\n" + encabezado)
                print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[   -RATTATAT-    ]" + " " *
                       int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                print(encabezado + "\n")

                # ART:
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                      "(", vida_actual_trainer, "/", VIDA_INICIAL_RATTATAT, ")" +
                      (((MEDIO_X * 3) - 8) * " "))
                print(ascii_battle)
                print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "), "(",
                      vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("Es el turno de RATTATAT    ")
                time.sleep(0.5)
                ataque_trainer = random.randint(1, 2)

                if ataque_trainer == 1:
                    print("RATTATAT ataca con LATIGO CEPA!")
                    vida_actual_pikachu -= 10

                else:
                    print("RATTATAT ataca con MORDISCO!")
                    vida_actual_pikachu -= 11
                input("Enter para continuar...\n")

                porcentage_pikachu = int(vida_actual_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
                barra_pikachu = ("#" * porcentage_pikachu) + (
                        "." * (TAMAÑO_BARRA_VIDA - porcentage_pikachu))

                if vida_actual_pikachu < 0:
                    vida_actual_pikachu = 0
                    break
                os.system('cls')
                print("\n" + encabezado)
                print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[   -RATTATAT-    ]" + " " *
                       int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                print(encabezado + "\n")

                # ART:
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                      "(", vida_actual_trainer, "/", VIDA_INICIAL_RATTATAT, ")" +
                      (((MEDIO_X * 3) - 8) * " "))
                print(ascii_battle)
                print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "), "(",
                      vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                time.sleep(0.5)
                os.system('cls')

                ####################################################################
                ataques_pikachu = ["P", "O", "R", "S", "p", "o", "r", "s"]
                ataque_pikachu = None
                while ataque_pikachu not in ataques_pikachu:
                    print("\n" + encabezado)
                    print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[    -RATTATAT-    ]" + " " *
                           int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                    print(encabezado + "\n")

                    # ART:
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                          "(", vida_actual_trainer, "/", VIDA_INICIAL_RATTATAT, ")" +
                          (((MEDIO_X * 3) - 8) * " "))
                    print(ascii_battle)
                    print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "),
                          "(",
                          vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print("Es tu turno!    PIKACHU    ")
                    ataque_pikachu = input("Que ataque deseas realizar?\n"
                                           " - [P]lacaje\n"
                                           " - [O]nda Trueno\n"
                                           " - [R]ayo\n"
                                           " - Pa[S]ar Turno\n")

                    if ataque_pikachu == "P" or ataque_pikachu == "p":
                        print("PIKACHU ataca con PLACAJE!")
                        vida_actual_trainer -= 10
                    elif ataque_pikachu == "O" or ataque_pikachu == "o":
                        print("PIKACHU ataca con ONDA TRUENO!")
                        vida_actual_trainer -= 12
                    elif ataque_pikachu == "R" or ataque_pikachu == "r":
                        print("PIKACHU ataca con RAYO!")
                        vida_actual_trainer -= 14
                    elif ataque_pikachu == "S" or ataque_pikachu == "s":
                        print("JUGADOR, ha pasado el turno")

                    porcentage_trainer = int(vida_actual_trainer * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_RATTATAT)
                    barra_trainer = ("#" * porcentage_trainer) + (
                            "." * (TAMAÑO_BARRA_VIDA - porcentage_trainer))
                    if vida_actual_trainer < 0:
                        vida_actual_trainer = 0

                    time.sleep(1)
                    os.system('cls')

                    print("\n" + encabezado)
                    print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[   -RATTATAT-    ]" + " " *
                           int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                    print(encabezado + "\n")

                    # ART:
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                          "(", vida_actual_trainer, "/", VIDA_INICIAL_RATTATAT, ")" +
                          (((MEDIO_X * 3) - 8) * " "))
                    print(ascii_battle)
                    print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "),
                          "(",
                          vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                    print("+" + "-" * MAP_WIDTH * 3 + "+")

                    input("Enter para continuar...\n\n")
                    time.sleep(0.5)
                    os.system('cls')

        # Round 3:
        else:
            vida_actual_trainer = VIDA_INICIAL_PIDGEY
            porcentage_trainer = int(vida_actual_trainer * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIDGEY)
            barra_trainer = "#" * porcentage_trainer

            while vida_actual_trainer > 0 and vida_actual_pikachu > 0:

                print("\n" + encabezado)
                print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[     -PIDGEY-     ]" + " " *
                       int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                print(encabezado + "\n")

                # ART:
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                      "(", vida_actual_trainer, "/", VIDA_INICIAL_PIDGEY, ")" +
                      (((MEDIO_X * 3) - 8) * " "))
                print(ascii_battle)
                print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "), "(",
                      vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("Es el turno de PIDGEY    ")

                time.sleep(0.5)
                ataque_trainer = random.randint(1, 3)

                if ataque_trainer == 1:
                    print("PIDGEY ataca con PICOTAZO!")
                    vida_actual_pikachu -= 10
                if ataque_trainer == 2:
                    print("PIDGEY ataca con ALETEO!")
                    vida_actual_pikachu -= 8
                else:
                    print("PIDGEY ataca con TORBELLINO!")
                    vida_actual_pikachu -= 10
                input("Enter para continuar...\n")

                porcentage_pikachu = int(vida_actual_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
                barra_pikachu = ("#" * porcentage_pikachu) + (
                        "." * (TAMAÑO_BARRA_VIDA - porcentage_pikachu))

                if vida_actual_pikachu < 0:
                    vida_actual_pikachu = 0
                    break

                os.system('cls')
                print("\n" + encabezado)
                print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[     -PIDGEY-     ]" + " " *
                       int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                print(encabezado + "\n")

                # ART:
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                      "(", vida_actual_trainer, "/", VIDA_INICIAL_PIDGEY, ")" +
                      (((MEDIO_X * 3) - 8) * " "))
                print(ascii_battle)
                print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "), "(",
                      vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))

                time.sleep(0.5)
                os.system('cls')

                ####################################################################
                ataques_pikachu = ["P", "O", "R", "S", "p", "o", "r", "s"]
                ataque_pikachu = None
                while ataque_pikachu not in ataques_pikachu:
                    print("\n" + encabezado)
                    print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[     -PIDGEY-     ]" + " " *
                           int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                    print(encabezado + "\n")

                    # ART:
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                          "(", vida_actual_trainer, "/", VIDA_INICIAL_PIDGEY, ")" +
                          (((MEDIO_X * 3) - 8) * " "))
                    print(ascii_battle)
                    print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "),
                          "(",
                          vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print("Es tu turno!    PIKACHU    ")
                    ataque_pikachu = input("Que ataque deseas realizar?\n"
                                           " - [P]lacaje\n"
                                           " - [O]nda Trueno\n"
                                           " - [R]ayo\n"
                                           " - Pa[S]ar Turno\n")

                    if ataque_pikachu == "P" or ataque_pikachu == "p":
                        print("PIKACHU ataca con PLACAJE!")
                        vida_actual_trainer -= 10
                    elif ataque_pikachu == "O" or ataque_pikachu == "o":
                        print("PIKACHU ataca con ONDA TRUENO!")
                        vida_actual_trainer -= 12
                    elif ataque_pikachu == "R" or ataque_pikachu == "r":
                        print("PIKACHU ataca con RAYO!")
                        vida_actual_trainer -= 14
                    elif ataque_pikachu == "S" or ataque_pikachu == "s":
                        print("JUGADOR, ha pasado el turno")

                    porcentage_trainer = int(vida_actual_trainer * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIDGEY)
                    barra_trainer = ("#" * porcentage_trainer) + (
                            "." * (TAMAÑO_BARRA_VIDA - porcentage_trainer))
                    if vida_actual_trainer < 0:
                        vida_actual_trainer = 0

                    time.sleep(1)
                    os.system('cls')

                    print("\n" + encabezado)
                    print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[     -PIDGEY-     ]" + " " *
                           int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                    print(encabezado + "\n")

                    # ART:
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                          "(", vida_actual_trainer, "/", VIDA_INICIAL_PIDGEY, ")" +
                          (((MEDIO_X * 3) - 8) * " "))
                    print(ascii_battle)
                    print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "),
                          "(",
                          vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                    print("+" + "-" * MAP_WIDTH * 3 + "+")
                    print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                    print("+" + "-" * MAP_WIDTH * 3 + "+")

                    input("Enter para continuar...\n\n")
                    time.sleep(0.5)
                    os.system('cls')

        if vida_actual_trainer == 0:

                print("\n" + encabezado)
                print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "    -HAS GANADO-   " + " " *
                       int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                print(encabezado + "\n")

                # ART:
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                      "(", vida_actual_trainer, "/", VIDA_INICIAL_PSYDUCK, ")" +
                      (((MEDIO_X * 3) - 8) * " "))
                print(ascii_battle)
                print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "),
                      "(",
                      vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                print("+" + "-" * MAP_WIDTH * 3 + "+")

                print("Has ganado!, cada vez estas mas cerca de la copa POKEMON!")
                input("Enter para continuar...")



        elif vida_actual_pikachu == 0:
                print("\n" + encabezado)
                print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "   -HAS PERDIDO-   " + " " *
                       int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
                print(encabezado + "\n")

                # ART:
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print(("| ") + ("[") + (barra_trainer) + ("]") + (" "),
                      "(", vida_actual_trainer, "/", VIDA_INICIAL_PSYDUCK, ")" +
                      (((MEDIO_X * 3) - 8) * " "))
                print(ascii_battle)
                print(("|") + (((MEDIO_X * 3) - 8) * " ") + ("[") + (barra_pikachu) + ("]") + (" "),
                      "(",
                      vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")" + "|")
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("[P]ause" + (" " * int((MAP_WIDTH * 3 + 2) - 13) + "[Q]uit"))
                print("+" + "-" * MAP_WIDTH * 3 + "+")
                print("Entrenador pokemon: Te he ganado!, cuando quieras vuelve y hacemos la revancha")
                input("Enter para continuar...")

    if len(pokemon_trainers) == 0:
        break

    elif direction == "q":
        quit = input("De verdad quieres salir?\n [S]i / [N]o")
        if quit == "s" or  quit == "S":
            exit()

    elif direction == "p":
        os.system('cls')
        print("\n" + encabezado)
        print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "     -[PAUSE]-   " + " " *
               int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
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
print((" " * int(((MAP_WIDTH * 3 + 2) - 18) / 2) + "[PUEBLO RASTRILLO]" + " " *
               int(((MAP_WIDTH * 3 + 2) - 18) / 2)))
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
print("Has superado PUEBLO RASTRILLO")
input("Presiona Enter para continuar...")
exit()
