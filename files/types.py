
print(type(32))
print(type(2.3))
print(type(True))
print(type("hola"))
'''
un tipo entero se refiere a un numero entero ya sea positivo, negativo o cero,
un float es un una aproximacion de python a los numeros reales, estos consisten de una parte real y
de una parte decimal. Un String es un tipo de dato en cadena de texto, este consiste en una secuencia
de caracteres. Finalmente, un booleano un tipo de dato binario, esto quiere decir que un booleano
solo puede tomar dos valores: True o False.
'''

'''
los datos en python son guardados como objetos con su respectivo id en memoria, en este sentido Python
es de tipado fuerte, aunque el id en memoria puede cambiar con respecto a la ejecucion
'''

z = 12
print(id(z))

z = "h"
print(id(z))

a = "hola"
b = "H" + a[1:]
print(b)

print(id(int)) # este id no cambia con respecto al tiempo, ya que es un objeto