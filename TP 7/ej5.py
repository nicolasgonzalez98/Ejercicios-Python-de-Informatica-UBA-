def cont_consonantes(a):
    a=a.upper()
    vocales=("A","E","I","O","U"," ")
    cont=0
    for i in range(len(a)):
        if a[i] not in vocales:
            cont=cont+1
    if cont%2==0:
        print("Hay un numero par de consonantes.")
    else:
        print("Hay un numero impar de consonantes.")
    

texto=input("Ingrese un texto: ")
cont_consonantes(texto)
    
