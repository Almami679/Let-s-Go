import os



numeros_usuario = []
numero_intorducido = int(input("Introduzca un numero en la lista\n"
                           "- "))
numeros_usuario.append(numero_intorducido)

while input("desea introducir mas numeros?"
            "[S]i / [N]o\n"
            "- ") == "S":
    numero_intorducido = int(input("Introduzca un numero en la lista\n"
                               "- "))
    numeros_usuario.append(numero_intorducido)
print("tus numeros son:")
print(numeros_usuario)

mas_pequenio = numeros_usuario[0]
mas_grande = numeros_usuario[0]

for numero in numeros_usuario[1:]:#filtrado de lista, recorrera todas las posiciones asignadas entre [_:_]
    if mas_pequenio > numero:
        mas_pequenio = numero
    if mas_grande < numero:
        mas_grande = numero
print("De tus numeros introducidos, el mas pequeño es {}, y el mas grande es {}"
      .format(mas_pequenio, mas_grande))



"""
######################### LIKE A PRO #########################################

numeros_introducidos = input("Introduzca sus numeros separados por coma: \n"
                             "- ")
numeros_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")] #list compreheision
             
             #todo lo introducido por el usuario, lo separa segun las comas y lo transforma en lista
             y cada uno lo transforma en entero)

print("tus numeros son:")
print(numeros_de_usuario)

"""