dinero = "Tienes dinero para comprarlo?"
iOS_caro = "Iphone Pro Ultra Max"
resultado = "Tu mejor opcion es "
iOS_barato = "iPhone de segunda mano de Aliexpres"
respuesta = "si (S) / no (N)"



print("Bienvenido al Asistente de compra de MiTelefonoNuevo.com\n")
opcion = input("Que sistema operativo quieres para tu nuevo dispositivo?\n"
    "A - iOS\n"
    "B - Andriod\n")
if opcion == "A":
    presupuesto = input(dinero + "\n"
                        + respuesta + "\n")   #pregunta sobre si tiene dinero o no
    if presupuesto == "S":
        print(resultado + iOS_caro)
    elif presupuesto == "N":
        print(resultado + iOS_barato)
    else:
        print("si no sabes cuanto dinero tienes, aqui acaba todo")
        exit()
if opcion == "B":
    presupuesto = input(dinero + "\n"
                         + respuesta + "\n")
    if presupuesto == "S":
        camara = input("Te importa la camara del mobil" + "\n"
                       + respuesta + "\n")
        if camara == "S":
            print(resultado + "Google pixel Supermacara")
        elif camara == "N":
            print(resultado + "un android i20 por 199€")
        else:
            print("debes contestar a la pregunta con S o N")
            exit()

    elif presupuesto == "N":
        print(resultado + "Android chino de 100€")
    else:
        print("debes contestar a la pregunta con S o N")
        exit()
print("\n" + "gracias por tu participacion, esperamos ser de ayuda")



