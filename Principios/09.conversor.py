temperatura= input("Ingrese la temperatura a convertir: ")
typoTemperatura= input ("Es celsiu (C) o fahrenheit (F): ")
tipoTemperatura= typoTemperatura.upper()

if tipoTemperatura == "C":
    temperatura= float(temperatura)
    temperatura= (temperatura*9/5)+32
    print ("La temperatura es: ",temperatura)
elif tipoTemperatura == "F":
    temperatura= float(temperatura)
    temperatura= (temperatura-32)*5/9
    print ("La temperatura es: ",temperatura)
else:
    print ("El tipo de temperatura es incorrecto")


