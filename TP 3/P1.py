num=int(input("Ingrese un numero entero: "))

n=2


while n<num:
    prim=num%n
    if num==2:
        print("Es primo")
        exit()
    elif prim==0:
        print("No es primo")
        exit()
    else:
         n=n+1

print("Es primo")
exit()

    

    
    
    
    
