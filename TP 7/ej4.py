def cont_vocales(a):
    a=a.upper()
    vocales=("A","E","I","O","U")
    cont=0
    for i in range(len(a)):
        if a[i] in vocales:
            cont=cont+1
    print("El texto ingresado tiene %s vocales."%cont)




b=input("Ingrese algO: ")
cont_vocales(b)
        
