numeros=set()
suma=0

while len(numeros)<21:
    num=int(input("Ingrese un numero: "))
    if num not in numeros:
        suma=suma+num
    numeros.add(num)

print(suma)





    

    
