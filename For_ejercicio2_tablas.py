import os
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


numero = int(input("De que numero quieres que te de la tabla?\n"
      "- "))#introduce el (numero) y se transforma en entero

#por cada (item) dentro de la lista (numeros) o en el rango(range) entre (1 y 11)
for item in range(1, 11):
    resultado = (numero * item)#operacion
    print("{} x {} = {}".format(numero, item, resultado))
    # imprime el (numero), imprime el (item) e imprime el (resultado)
multiplos = input("Quieres que te de los multiplos de dos que contiene esta tabla?\n"
                  "[S]i / [N]o\n"
                  "- ")
if multiplos == "S":
    os.system('cls')
    print("Estos son los multiplos de dos \n")
    for item in range(1, 11):
        resultado = (numero * item)#operacion
        if item % 2 == 0:
            # "%" es la operacion modulo, (comprueba los decimales)
            print("{} x {} = {}".format(numero, item, resultado))

else:
    exit()



