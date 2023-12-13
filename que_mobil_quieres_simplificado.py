
movil_ideal = "ninguno"

respuesta = "[S] si / [N] no"

print("Bienvenido al Asistente de compra de MiTelefonoNuevo.com\n")
print("que sistema operativo buscas?\n")
opcion = input("[I] iOS o [A] Android?")
if opcion == "I":
    opcion = input("tienes dinero?\n"
                   + respuesta)
    if opcion == "S":
        movil_ideal = "Iphone pro max 3865"
    else:
        movil_ideal = "iphone de aliexpres"
elif opcion == "A":
    opcion = input("tienes dinero?\n"
                   + respuesta)
    if opcion == "S":
        opcion = input("te importa la camara?\n"
                       + respuesta)
        if opcion == "S":
            movil_ideal = "Google Pixel Supercamera"
        else:
            movil_ideal = "Xiaomi i20"
    else: "Movil Xino de Aliexpres\n"
print("tu movil ideal es " + movil_ideal)
print("gracias por confiar en nosotros")
exit()





