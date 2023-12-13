titulo = "Bienvenido al Test del Cocinillas"
print("\n" + titulo)
print("-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("1ª pregunta: Cuando vas al super lo primero que coges es:\n"
               "A - Dos botes de Ketchup \n"
               "B - Cereales y leche \n"
               "C - Ajos, cebollas y pimineto \n")
if opcion == 'A':
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("esa opcion no esta entre las sugeridas")
    opcion = input("introduce unas de las opciones disponibles\n")
print("\n")
opcion = input("2ª pregunta: Es la hora de comer, Que haces?\n"
               "A - Coger el telefono y pedir un Glovo\n"
               "B - Ensaladita, unos tomates, enfin algo rapido y sano\n"
               "C - Menuda paella que se viene... Pedazo de sofrito\n")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("sigues sin pillar lo de que solo hay 3 opciones")
    opcion = input("introduce unas de las opciones disponibles\n")
print("\n")
opcion = input("3ª pregunta: Hoy es la fiesta de inauguracion de mi piso de estudiante...\n"
               "A - en el paki de abajo venden chips y pizza tarradelles, un lujo...\n"
               "B - una tortilla casera como me enseño mi abuela y alguna croqueta \n"
               "C - Un menu cocktail que ni Ferran Adria\n")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("eres mas corto que las mangas de un chaleco")
    opcion = input("introduce unas de las opciones disponibles\n")
print("\n")
opcion = input("Ultima pregunta: Domingo por la noche... y mañana se curra...\n"
               "A - Domingo? Peli y palomitas, vas que te matas\n"
               "B - Una tablita de embutidos con su pan con tomate\n"
               "C - Aunque da palo, algo haremos con lo que queda en la nevera\n")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("ya me he cansado de tus tonterias")
    exit()
print("\n")
print("tu puntuacion es: {}" .format(puntuacion) + " puntos\n")
if puntuacion >= 35:
    print("Felicidades! eres una joven promesa Michelin")
elif puntuacion >= 25:
    print("Bueno... no esta tan mal, no te morirías de hambre en un apocalipsis zombie")
else:
    print("NO TE INDEPENDICES NUNCA AMIGO")











