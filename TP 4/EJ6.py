car=input("Ingrese un caracter: ")
texto=input("Ingrese un texto: ")

while len(texto)>30:
    print("Texto invalido.")
    texto=input("Ingrese un texto")


texto=texto.capitalize()

for i in range(len(texto)):
    if texto[i]==car:
        texto=texto.replace(texto[i], "")


print(texto)
