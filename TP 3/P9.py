num=int(input("Ingrese el numero a factorizar: "))
fact=int(num-1)
if num>0:
    res=num*fact
    i=True
    while i:
        if fact==1:
            print("El factorial de",num,"es:",res)
            i=False
        else:
            fact=fact-1
            res=res*fact
elif num==0:
    print("El factorial de",num,"es: 1")
else:
    print("No se puede calcular el factorial de un número negativo")
    
            

        
