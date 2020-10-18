num=int(input("Ingrese un numero positivo: "))
par=int(num%2)


if num>0 and par==0:
    print("Próximo par es: ", num+2)
else:
    print("Próximo par es: ", num+1)
