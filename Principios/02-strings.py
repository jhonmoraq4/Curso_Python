texto="Hola Mundo"
print(texto.upper())
print(texto.lower())
print(texto.find("M")) # shift + alt + down arrow
nuevo_texto=texto.replace("M", "m")
print(nuevo_texto," , ",texto)
print(texto.count("M"))
print(texto.startswith("Hola"))
print(texto.endswith("M"))
print(texto.isalnum())
print(texto.isalpha())
print("Mundo" in texto)