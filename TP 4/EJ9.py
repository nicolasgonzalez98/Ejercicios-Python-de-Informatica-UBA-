texto=input("Ingrese un texto: ")

print("Este es el texto recortado: ")
for i in range(len(texto)):
    if i%2==0:
        print(texto[i], end="")
