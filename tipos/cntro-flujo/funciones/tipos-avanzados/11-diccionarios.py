punto = {"X": 25, "y": 50}
print(punto)
print(punto["X"])
print(punto["y"])

punto["z"] = 45
# print(punto, punto["lala"])
if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("X",))
print(punto.get("lala", 97))
del punto["X"]
del (punto["y"])
print(punto)
punto["X"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Fekiz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},

]
for usuario in usuarios:
    print(usuario["nombre"])
