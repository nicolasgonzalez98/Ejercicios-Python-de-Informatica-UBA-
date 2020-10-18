caracter=input("Ingrese un caracter: ")
texto1=input("Ingrese un texto: ")

contador=0

for i in range(len(texto1)):
    if texto1[i]==caracter:
        contador=contador+1


print(caracter, "aparece", contador,"veces")
