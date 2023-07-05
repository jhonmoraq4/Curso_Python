lenguajes = ["python", "ruby", "php", "JavaScript", "Java"]

i = 0

while i < len(lenguajes):
    print(lenguajes[i])
    i += 1
    #i=i+1

print("Fin")

comando = ""
while comando.lower() != "salir":
    comando = input("Ingrese una palabra: ")
    print(comando)


while True:
    Test = input("Ingrese una palabra: ")
    if Test.lower() == "salir":
        break
    print(Test)