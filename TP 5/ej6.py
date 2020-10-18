lista=[]

while len(lista)<20:
    num=int(input("Ingrese un numero positivo: "))
    if num>0:
        if num not in lista:
            lista.append(num)

i=True
while i:
    dato=int(input("Ingrese el numero a buscar (Pulse 0 para salir): "))
    if dato==0:
        print("Gracias, vuelvas prontos")
        i=False
    elif dato in lista:
        index=lista.index(dato)
        print("Si, a",dato,"lo tengo, esta en el indice",index)
    elif dato not in lista:
        print("No, ",dato,"no lo tengo")

    
        
        
        



        


