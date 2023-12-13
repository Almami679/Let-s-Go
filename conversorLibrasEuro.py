

dolar_euro = 0.91
libra_euro = 1.18
print("\n")
print("Bienvenido al conversor mas cutre que existe de Libras(&)/Dolares($) a Euro (€)\n")
opcion = input("que divisa quieres cambiar? \nDolar -D-/Libra -L-/Euro -E-\n")
if opcion == "D":
    valor = float(input('que cantidad de Dolares ($) quieres convertir a (€)Euros?\n'))
    resultado = (valor * dolar_euro)
    print("{}".format(valor) + "$ dolares equivalen a {}".format(resultado) + "€ Euros\n")
elif opcion == "L":
    valor = float(input("que cantidad de Libras(&) quieres convertir a Euros(€)?\n"))
    resultado = (valor * libra_euro)
    print("{}".format(valor) + "& Libras equivalen a {}".format(resultado) + "€ Euros\n")
elif opcion == "E":
    cambio = input("A que moneda quieres cambiar el Euro(€) (Libras -L-/Dolares -D-\n")
    if cambio == "L":
        valor = float(input("que cantidad de Euros(€) quieres cambiar a Libras(&)\n"))
        resultado = (valor/libra_euro)
        print("{}".format(valor) + "€ Euros equivalen a " + "{}".format(resultado) + "& Libras\n")
    elif cambio == "D":
        valor = float(input("que cantidad de Euros(€) quieres cambiar a dolares($)\n"))
        resultado = (valor/dolar_euro)
        print("{}".format(valor) + "€ Euros equivalen a " + "{}".format(resultado) + "$ Dolares\n")
    elif opcion != "D" or "L":
        print("Las unicas opciones disponibles son D y L")
        print('gracias por usar el guugleconverter')
        exit()
elif opcion != "D" or "L" or "E":
    print("Las unicas opciones disponibles son D, L y E")
    print('gracias por usar el guugleconverter')
    exit()
print("gracias por usar el Guugleconverter")

