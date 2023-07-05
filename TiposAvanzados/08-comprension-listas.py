mascotas= [["mascota1",4], ["mascota2",2], ["mascota3",3],["mascota4",1]]

nombres=[mascota[0] for mascota in mascotas]
print(nombres)

nombres=[mascota[0] for mascota in mascotas if mascota[1]>2]
print(nombres)

nombres =list (map(lambda mascota: mascota[0], mascotas))
print(nombres)

nombres =list (filter(lambda mascota: mascota[1]>2, mascotas))
print(nombres)