car=input("Ingrese un caracter: ")
texto=input("Ingrese un texto: ")

while len(texto)>30:
    print("Texto invalido.")
    texto=input("Ingrese un texto")


texto=texto.capitalize()

t=texto.replace(car,"*")


print(t)
