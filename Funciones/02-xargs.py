def suma(*numeros): # puedo mandar todos los numeros que queremos sumar gracias al *
    resultado=0
    for numero in numeros:
        resultado+=numero
    print(resultado)

suma(2,2,2)