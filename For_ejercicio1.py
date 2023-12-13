import string

espacios = " "
puntos = "."
comas = ","
espacios_encontrados = 0
puntos_encontrados = 0
comas_encontradas = 0
mayusuculas = 0
caracteres_encontrados = 0

texto_usuario = input("Que quieres que analice?\n"
                      "- ")
for caracter in texto_usuario:
    if caracter in espacios:
        espacios_encontrados += 1
    elif caracter in puntos:
        puntos_encontrados += 1
    elif caracter in comas:
        comas_encontradas += 1
    elif caracter in string.ascii_uppercase:
        mayusuculas += 1
    if caracter in caracter:
        caracteres_encontrados += 1


print("Espacios encontrados: {}\n"
      "Puntos encontrados: {}\n"
      "Comas encontradas: {}\n"
      "Mayusuculas totales: {}\n"
      "Caracteres totales: {}".format(espacios_encontrados, puntos_encontrados, comas_encontradas,
                                          mayusuculas, caracteres_encontrados))
