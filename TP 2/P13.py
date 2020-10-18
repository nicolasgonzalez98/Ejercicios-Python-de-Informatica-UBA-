num=int(input("Ingrese un numero entero positivo: "))

if num>0:
    if num%5==0:
        mul=int(input('Ingrese un numero menor a %s: '%num))
        if mul<num:
            print("Es correcto")
        else:
            print("Es incorrecto")
    else:
        n=int(input("Ingrese un numero mayor a %s: "%num))
        if n<num:
            print("Es incorrecto")
        else:
            print("Es correcto")
            
else:
    print("Ingresaste un numero que es 0 o negativo")
