contador=1
numero1=0

num1 = input("Ingrese el primer número: ")
while num1.isdigit() == False:
        print("La variable 'num1' no es un número.")
        num1 = input("Ingrese el primer número: ")

print("Las operaciones posibles son suma, resta, multiplicacion, division")
op = input("Ingrese una operacion: ")

numero1=int(num1)

while op.lower()!= "salir":

    if contador >1:
        print("Las operaciones posibles son suma, resta, multiplicacion, division")
        op = input("Ingrese una operacion: ")

    num2 = input("Ingrese el siguiente número: ")
    
    contador =1+contador

    while num2.isdigit() == False:
        print("La variable 'num2' no es un número.")
        num2 = input("Ingrese el siguiente número: ")
    
    numero2=int(num2)
     
    if op.lower() == "suma" :
        numero1 = numero1 + numero2
        print("la suma es: ", numero1)

    elif op.lower() == "resta":
        print("la resta es: ", numero1 - numero2)

    elif op.lower() == "multiplicacion":
        print("la multiplicacion es: ", numero1 * numero2)
        
    elif op.lower() == "division":
        print("la division es: ", numero1 / numero2)

    elif op.lower() == "salir":
        print("Gracias por usar el programa")

    else:
        print("la operacion ingresada no existe")