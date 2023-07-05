def get_product(**datos):
    print(datos)
    print(datos['name'])

get_product(id="id",
            name="iPhone",
            description="Esto es un product")