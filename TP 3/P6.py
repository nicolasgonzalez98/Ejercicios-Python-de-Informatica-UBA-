n=True
primero=int(input("Ingrese un numero: "))
mayor=primero
menor=primero



while n:
    num=int(input("Ingrese un numero (Ingrese 0 para salir): "))
    if num==0:
        n=False
    elif num>0:
        if num>mayor:
            mayor=num
        elif num<menor:
            menor=num
    else:
        print("No ingresaste un numero valido.")


print("El mayor numero es ", mayor)
print("El menor numero es ", menor)
        
    
