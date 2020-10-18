def cambiavocal(a,caracter):
    a=a.upper()
    vocales=("A","E","I","O","U","Á","É","Í","Ó","Ú")
    b=list(a)
    for i in range(len(b)):
        if b[i] in vocales:
            b[i]=caracter
    cadena="".join(b)
    print(cadena.capitalize())

        


texto=input("Ingrese texto: ")
caracter=input("ingrese caracter: ")
cambiavocal(texto,caracter)
