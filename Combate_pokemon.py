from random import randint
import os
import time


VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 85
TAMAÑO_BARRA_VIDA = 15
vida_actual_pikachu = VIDA_INICIAL_PIKACHU
vida_actual_squirtle = VIDA_INICIAL_SQUIRTLE
porcentage_squirtle = int(vida_actual_squirtle * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
porcentage_pikachu = int(vida_actual_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
barra_pikachu = "#" * porcentage_pikachu
barra_squirtle = "#" * porcentage_squirtle
print("\nHas encontrado un Pikachu salvaje!\n"
      "----------------------------------\n")
print("           \:.             .:/\n"
      "            \``._________.''/ \n"
      "             \             /\n" 
      "     .--.--, / .':.   .':. \ \n"
      "    /__:  /  | '::' . '::' |\n"
      "       / /  | `.   ._.   .'|\n"
      "      / /    |.'         '.|\n"
      "     /___-_-,|.\  \   /  /.|\n"
      "          // |''\.;   ;,/ '|\n"
      "          `==|:=         =:|\n"
      "              `.          .'\n"
      "               :-._____.-:\n"
      "              `''       `''\n")

input("Enter para continuar...\n\n")
######################################################################
time.sleep(0.5)
os.system('cls')

print("Player juega con Squirtle!\n")
print("Comienza el combate!\n"
      "''''''''''''''''''''\n")

while vida_actual_squirtle > 0 and vida_actual_pikachu > 0:
      print(("Es el turno de Pikachu    ") + ("[") + (barra_pikachu) + ("]") + (" "),
            "(", vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")")

      ataque_pikachu = randint (1, 2)
      if ataque_pikachu == 1:
            print("Pikachu ataca con Bola Voltio!")
            vida_actual_squirtle -= 10
      else:
            print("Pikachu ataca con Onda Trueno!")
            vida_actual_squirtle -= 11
      input("Enter para continuar...\n")
      porcentage_squirtle = int(vida_actual_squirtle * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
      barra_squirtle = ("#" * porcentage_squirtle) + ("." * (TAMAÑO_BARRA_VIDA - porcentage_squirtle))
      if vida_actual_squirtle < 0:
            vida_actual_squirtle = 0
      print(("Squirtle ") + ("[") + (barra_squirtle) + ("]") + (" "), "(",
            vida_actual_squirtle, "/", VIDA_INICIAL_SQUIRTLE, ")")
      print(("Pikachu  ") + ("[") + (barra_pikachu) + ("]") + (" "),
                  "(", vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")")

      input("Enter para continuar...\n\n")
      time.sleep(0.5)
      os.system('cls')

      ####################################################################
      ataque_squirtle = None
      while ataque_squirtle not in ["P", "A", "B", "S"]:
            print(("Es el turno de Squirtle    ") + ("[") + (barra_squirtle) + ("]") + (" "), "(",
            vida_actual_squirtle, "/", VIDA_INICIAL_SQUIRTLE, ")\n")
            ataque_squirtle = input("Que ataque deseas realizar?\n"
                                    " - [P]lacaje\n"
                                    " - Pistola [A]gua\n"
                                    " - [B]urbuja\n"
                                    " - Pa[S]ar Turno\n")
            if ataque_squirtle == "P":
                  print("Squirtle ataca con Placaje!")
                  vida_actual_pikachu -= 10
            elif ataque_squirtle == "A":
                  print("Squirtle ataca con Pistola Agua!")
                  vida_actual_pikachu -= 12
            elif ataque_squirtle == "B":
                  print("Squirtle ataca con Burbuja!")
                  vida_actual_pikachu -= 9
            elif ataque_squirtle == "S":
                  print("Player 1, ha pasado el turno")
            porcentage_pikachu = int(vida_actual_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
            barra_pikachu = ("#" * porcentage_pikachu) + ("." * (TAMAÑO_BARRA_VIDA - porcentage_pikachu))
            if vida_actual_pikachu < 0:
                  vida_actual_pikachu = 0
            print(("Squirtle ") + ("[") + (barra_squirtle) + ("]") + (" "), "(",
                  vida_actual_squirtle, "/", VIDA_INICIAL_SQUIRTLE, ")")
            print(("Pikachu  ") + ("[") + (barra_pikachu) + ("]") + (" "),
                  "(", vida_actual_pikachu, "/", VIDA_INICIAL_PIKACHU, ")")

            input("Enter para continuar...\n\n")
            time.sleep(0.5)
            os.system('cls')

      ############################################################################
if vida_actual_pikachu < vida_actual_squirtle:
      print("\nSquirtle gana la batalla!\n"
            "-------------------------\n")
else:
      print("\nPikachu gana la batalla!\n"
            "------------------------\n"
            "[Has Perdido]")
time.sleep(0.5)
os.system('cls')

############################################################################################

exit()
