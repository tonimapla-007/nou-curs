
usuarios = [["Chanchito", 4],
            ["Felipe", 1],
            ["Pulga", 5]
            ]


"""
nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)
"""
# comprension de listas
# nombres = [usuario[0] for usuario in usuarios]

# filtrar
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# utilizando map()
# nombres = list(map(lambda usuario: usuario[0], usuarios))

# utilizando filter()
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))


print(menosUsuarios)
