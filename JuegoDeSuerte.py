import random
numero_ganador = random.randint (1, 10)
titulo = 'Buenas, has sido seleccionado para participar en un sencillo juego de azar'
print(titulo)
print('en el rango entre los numeros 1 y 10, escoge uno')
que_numero = input('que numero escoges? (1/2/3/4/5/6/7/8/9/10)')
if que_numero == numero_ganador:
    print('y el numero correcto era {}'.format (numero_ganador))
    print('Felicidades! has ganado un iphone XIII')
if que_numero != numero_ganador:
    print('y el numero correcto era {}'.format (numero_ganador))
    print('lo sentimos, solo te has llevado un troyano mas')


