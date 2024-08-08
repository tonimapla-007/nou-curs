mascotas = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chancito feliz"
]

mascotas.insert(1, "Melvin")  # inserta "Melvin" en el puesto indicado
mascotas.append("Chanchito triste")  # inserta el elemento al final de la lista

mascotas.remove("Pulga")  # elimina "Pulga"

# sin numero elimina el ultimo elemento, con numero elimina el elemento indicado
mascotas.pop(1)
del mascotas[0]     # borra  el elemeto indicado
mascotas.clear()    # borra toda la lista
print(mascotas)
