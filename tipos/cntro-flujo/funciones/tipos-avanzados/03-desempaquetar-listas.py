numeros = [1, 2, 3]
# feo
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# primero, segundo, tercero = numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, penu, ultimo = numeros
# primero, segundo, *otros = numeros

primero, *otros, ultimo = numeros

# print(primero, otros)
print(primero, segundo, otros)
# print(primero, segundo)

# print(primero, segundo, tercero)
print(segundo, penu, otros)
