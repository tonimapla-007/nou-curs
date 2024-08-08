numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort()      #ordena los elementos de la lista
# numeros.sort(reverse=True)      #ordena los elementos de la lista al reves
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

"""                                 #ordena elementos por su "id"
usuarios = [[4, "Chanchito"],
            [1, "Felipe"],
            [5, "Pulga"]
            ]
usuarios.sort()
"""

usuarios = [["Chanchito", 4],  # no ordena ya que el primer campo no es ordenable
            ["Felipe", 1],
            ["Pulga", 5]
            ]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena, reverse=True)
print(usuarios)
