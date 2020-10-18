print("el texto debe ser hasta de 100 caracteres.")
texto1=input("Ingrese un texto: ")

while len(texto1)>100:
    print("Ingrese de nuevo.")
    texto1=input("Ingrese un texto: ")

texto1=texto1.upper()

print(texto1)
