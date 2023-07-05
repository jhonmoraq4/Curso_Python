mascotas= ["mascota1", "mascota2", "mascota3", "mascota4"]

for mascota in mascotas:
    print(mascota)

print()

for mascota in enumerate(mascotas):
    print(mascota)

print()

for mascota in enumerate(mascotas):
    print(mascota[0])

print()

for indice, mascota in enumerate(mascotas):
    print(indice,mascota)