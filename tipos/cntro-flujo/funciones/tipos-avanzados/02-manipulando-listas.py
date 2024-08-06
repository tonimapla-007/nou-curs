mascotas = ["Wolfgand", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho"
print(mascotas[0])
print(mascotas[0:3])
print(mascotas[2:])
print(mascotas[-1])
print(mascotas[::2])
print(mascotas[1::2])
print(mascotas[1:2:2])

numeros = list(range(1, 21))  # hace lo mismo que el siguiente print
# print(numeros)
print(numeros[1::2])  # imprime los numeros impares
print(numeros[::2])  # imprime los numeros pares
