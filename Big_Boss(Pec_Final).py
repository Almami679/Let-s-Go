import random

final_A = ("\n[Has Muerto]\n") + ("\n[FIN]\n")
final_B = ("\n[Has Sobrevivido]\n") + ("\n[FIN]\n")
print("\n\nPROBLEMAS EN EL PLANETA ROJO\n"
      "----------------------------\n"
      "\n"
      "Estas en la Base espacial de Marte (Mark_1-Mart),\n" ""
      "tras un error en la programacion del deposito de energia\n"
      "este va a explotar por sobrecarga y con lo cual la estacion esta en peligro.\n")
inventario_herramientas = False
inventario_taser = False
print("En la mesa de tu habitacion tienes un maletin de herramientas y una pistola taser\n"
      " pero solo puedes llevar una cosa ya que necesitas una mano libre\n")
opcion = input("Con cual te quedas?\n"
      "[A] Maletin de Herramientas\n"
      "[B] Pistola taser\n")
if opcion == "A":
    inventario_herramientas = True
elif opcion == "B":
    inventario_taser = True
else:
    print("no decides coger nada?, tu mismo")
print("\nDispones de 5 minutos para poder escapar de dicha estacion,\n"
      "y ya equipado, se plantean dos opciones de escapatoria\n")
opcion = input("que opcion escojes?\n"
               "[A] Correr hasta la sala de capsulas de escape\n"
               "[B] Correr al vestibulo principal para escapar al exterior\n")
if opcion == "A":
    print("Llegas a la sala de capsulas de escape,\n"
          "pero todas las capsulas estan selladas por seguridad \n"
          "y a lo lejos ves la terminal central de control\n")
    opcion = input("Que decides hacer?")
    if opcion == "A":
        print("Intentas emplear todo tu potencial mental en piratear la centralita,\n"
              "pero a ti te contrataron para investigar el crecimiento \n"
              "de plantas en el planeta, esto se te queda corto, \n"
              "pasas los cinco minutos intentando desbloquear las capsulas\n"
              "pero sin exito acaba explotando la base espacial contigo dentro.\n"
              + final_A)
    elif opcion == "B":
        print("Siempre has sido mañoso, pero, cogiste las herramientas de tu habitacion?\n")
        if inventario_herramientas == True:
            print("Consigues demontar la puerta cuando queda un minuto para la explosion,\n"
                  " subes a la capsula y despegas con la esperanza de llegar al satelite mas cercano.\n"
                  + final_B)
        elif inventario_herramientas == False:
            print("Haber cogido la pistola es algo que no va contigo y a parte una mala eleccion,\n"
                  " mientras te lamentas pasan los cinco minutos y explota todo" + final_A)
elif opcion == "B":
    print("Llegas al vestibulo, pero alli te encuentras a Tim, tu compañero ludopata\n"
          "que siempre ha disfrutado con el juego y el cual dispone del ultimo traje espacial\n"
          "en buen estado para poder salir al exterior.\n"
          "\nTim te plantea un juego para saber quien es el que se queda finalmente con el traje,\n"
          "haciendote adivinar cuantos dolares lunares lleva en el bolsillo.")
    resultado_juego = random.randint(1, 300)
    resultado = input("Cuantos dolares crees que tiene Tim?")
    if resultado == resultado_juego:
        print("Vaya! lo hacertaste!\n"
              "Tim tiene mal perder, y siempre lo tuvo, saca una pistola,\n"
              " te vuela los sesos y sale huyendo de la estacion." + final_A)
    else:
        print("Vaya! Has fallado!\n"
              "Tim regodeandose de que ha ganado el juego te deja el traje como agradecimiento\n"
              "de haberle brindado su ultima victoria en vida.\n"
              "\nTe pones el traje y sales a falta de un minuto para la explosion.\n"
              "\nAl salir al exterior del planeta rojo te encuentras cara a cara con una criatura\n"
              "que no habias visto antes, una especie de lobo espacial con dientes afilados\n"
              "que se abalanza sobre ti para intentar deborarte.")
        if inventario_taser == False:
            print("Al haber cogido las herramientas en lugar otra arma mas contundente,\n"
                  "no tienes nada que hacer contra un animal de tal calibre.\n"
                  "\nAcaba rasgandote la yugular provocando tu muerte en el acto." + final_A)
        elif inventario_taser == True:
            print("Suerte que eres precavido y cojiste un taser de tu habitacion,\n"
                  "justo cuando el lobo esta a 20cmt de tu cuello, le pegas tal aturdida\n"
                  "que cae desplomado al suelo\n")
            print("\nTras la batalla, tienes dos posibilidades de continuar tu viaje:\n")
            opcion = input("que decides?\n"
                           "[A] Seguir unas huellas de neumatico marcadas en el suelo\n"
                           "[B] Ir hacia un destello que se ve tras la montaña\n")
            if opcion == "A":
                print("Ves unas huellas en el suelo de lo que podria ser un vehiculo espacial,\n"
                      "las sigues y tras caminar 2 horas por el paramo rojo,\n"
                      "resultaron ser un camino hacia otra base Rusa.")
                print("Picas a la puerta desesperado, y te abren unos centificos muy hospitalarios.\n"
                      "\nOs pasais toda la noche bebiendo vodka y jugando al poker.\n"
                      + final_B)
            elif opcion == "B":
                print("Ves lo que parece ser un destello de luz intenso tras la montaña mas cercana,\n"
                      "vas hacia alli con la esperanza de que no sean extraterrestres.\n")
                print("La suerte parece estar de tu lado amigo,\n"
                      "no es nada mas ni nada menos que la nave de evacuacion.\n"
                      "\nConsigues subir antes de que despegue.\n" + final_B)





