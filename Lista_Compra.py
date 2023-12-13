import os
import time

cesta = []
salir = None

print("--------------------------\n")
print("Crea tu lista de la compra\n")
print("--------------------------\n")

input("Enter para continuar...")
os.system('cls')

while salir != "N":
    print("\n\n____________________________________________________")
    ingrediente = input("Que desea añadir a su cesta de la compra?\n"
                        "[Q] para salir\n"
                        "- ")
    if ingrediente == "Q":
        print("\n\n________________________________________________")
        salir = input("Esta seguro que desea salir?\n"
                      "[S]i / [N]o\n"
                      "- ")
        if salir == "S":
              print("Hay " +  str(len(cesta)) + " productos en tu cesta\n")
              time.sleep(0.5)
              print("La lista de la compra es:")
              print(cesta)
              input("Enter para salir...")
              os.system('cls')
              exit()
    else:
        if ingrediente in cesta:
            print("{} ya esta en la lista".format(ingrediente))
        else:
            if input("Añadir {} a la lista?\n".format(ingrediente) +
                     "[S]i /[N]o\n"
                     "- ") == "S":
                cesta.append(ingrediente)
                print("Se ha añadido " + ingrediente + " a tu lista de la compra")
                time.sleep(1)
                os.system('cls')

