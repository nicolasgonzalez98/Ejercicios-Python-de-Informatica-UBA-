text=input("ingrese un texto: ")

texto=text.split()

for i in range(len(texto)):
    print(texto[i].capitalize(), end=" ")
