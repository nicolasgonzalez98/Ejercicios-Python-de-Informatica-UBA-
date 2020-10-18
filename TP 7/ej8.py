def par_impar():
    par=[]
    impar=[]
    b=True
    while b:
        num=int(input("Ingrese un numero entero positivo (pulse 0 para salir): "))
        while num<0:
            print("Ingresaste un numero incorrecto.")
            num=int(input("Ingrese un numero entero positivo (pulse 0 para salir): "))
        if num==0:
            b=False
        elif num%2==0:
            par.append(num)
        else:
            impar.append(num)
    numeros=par+impar
    return numeros
        
print(par_impar())



