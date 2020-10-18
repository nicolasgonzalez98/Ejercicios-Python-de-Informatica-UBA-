texto1=input("Ingrese el primer texto: ")
texto2=input("Ingrese el segundo texto: ")

i=len(texto1)
g=len(texto2)

if i<g:
    print("El texto mas largo es el segundo.")
elif g<i:
    print("El texto mas largo es el primero.")
else:
    print("Ambos textos son iguales.")
    
